import os
import json
import uuid
from typing import List, Optional, Dict, Any
from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, get_db, Base
from .models import CaseModel, SimulationDecisionModel, ReflectionModel, EvaluationResponseModel
from .schemas import (
    CaseSummary, CaseDetail, DecisionSubmitRequest, DecisionAnalysisResponse,
    ModernDecisionSubmitRequest, ModernDecisionResponse, ReflectionSubmitRequest,
    ReflectionReportResponse, PrePostEvaluationSubmit, SUsFeedbackSubmit,
    KnowledgeGraphData, GraphNode, GraphEdge, ReasoningDimensions,
    GitaVerse, GitaQuestionRequest, GitaPerspectiveResponse
)
from .seed_data import SEED_CASES
from .gita_data import GITA_VERSES, find_gita_perspective

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dharma to Decisions API",
    description="Interactive Decision-Learning Simulation Framework Inspired by the Mahābhārata",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def seed_database_if_empty(db: Session):
    count = db.query(CaseModel).count()
    if count == 0:
        print("[Database] Seeding initial Mahābhārata cases...")
        for case_data in SEED_CASES:
            case_obj = CaseModel(
                id=case_data["id"],
                title=case_data["title"],
                subtitle=case_data.get("subtitle", ""),
                parva=case_data["parva"],
                chapter_reference=case_data["chapter_reference"],
                characters=json.dumps(case_data["characters"]),
                category=case_data["category"],
                strategic_themes=json.dumps(case_data["strategic_themes"]),
                ethical_themes=json.dumps(case_data["ethical_themes"]),
                difficulty=case_data.get("difficulty", "Intermediate"),
                estimated_time=case_data.get("estimated_time", "12-15 min"),
                context=case_data["context"],
                dilemma=case_data["dilemma"],
                why_difficult=case_data["why_difficult"],
                stakeholders=json.dumps(case_data["stakeholders"]),
                competing_values=json.dumps(case_data["competing_values"]),
                known_information=json.dumps(case_data["known_information"]),
                uncertain_information=json.dumps(case_data["uncertain_information"]),
                assumptions=json.dumps(case_data["assumptions"]),
                options=json.dumps(case_data["options"]),
                principles=json.dumps(case_data["principles"]),
                modern_scenario=json.dumps(case_data["modern_scenario"]),
                sources=json.dumps(case_data["sources"]),
                order_index=case_data.get("order_index", 0),
                is_published=True
            )
            db.add(case_obj)
        db.commit()
        print(f"[Database] Successfully seeded {len(SEED_CASES)} cases.")

@app.on_event("startup")
def startup_event():
    db = next(get_db())
    try:
        seed_database_if_empty(db)
    finally:
        db.close()

# -------------------------------------------------------------
# CASE ENDPOINTS
# -------------------------------------------------------------

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "app": "Dharma to Decisions",
        "timestamp": datetime.utcnow().isoformat(),
        "cases_seeded": len(SEED_CASES)
    }

@app.get("/api/cases", response_model=List[CaseSummary])
def get_cases(
    category: Optional[str] = None,
    parva: Optional[str] = None,
    difficulty: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(CaseModel).filter(CaseModel.is_published == True).order_index_by = CaseModel.order_index
    cases = db.query(CaseModel).filter(CaseModel.is_published == True).order_by(CaseModel.order_index.asc()).all()
    
    results = []
    for c in cases:
        if category and category.lower() not in c.category.lower():
            continue
        if parva and parva.lower() not in c.parva.lower():
            continue
        if difficulty and difficulty.lower() != c.difficulty.lower():
            continue

        results.append(CaseSummary(
            id=c.id,
            title=c.title,
            subtitle=c.subtitle,
            parva=c.parva,
            chapter_reference=c.chapter_reference,
            characters=json.loads(c.characters),
            category=c.category,
            strategic_themes=json.loads(c.strategic_themes),
            ethical_themes=json.loads(c.ethical_themes),
            difficulty=c.difficulty,
            estimated_time=c.estimated_time,
            order_index=c.order_index
        ))
    return results

@app.get("/api/cases/{case_id}", response_model=CaseDetail)
def get_case_detail(case_id: str, db: Session = Depends(get_db)):
    c = db.query(CaseModel).filter(CaseModel.id == case_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Case not found")

    return CaseDetail(
        id=c.id,
        title=c.title,
        subtitle=c.subtitle,
        parva=c.parva,
        chapter_reference=c.chapter_reference,
        characters=json.loads(c.characters),
        category=c.category,
        strategic_themes=json.loads(c.strategic_themes),
        ethical_themes=json.loads(c.ethical_themes),
        difficulty=c.difficulty,
        estimated_time=c.estimated_time,
        order_index=c.order_index,
        context=c.context,
        dilemma=c.dilemma,
        why_difficult=c.why_difficult,
        stakeholders=json.loads(c.stakeholders),
        competing_values=json.loads(c.competing_values),
        known_information=json.loads(c.known_information),
        uncertain_information=json.loads(c.uncertain_information),
        assumptions=json.loads(c.assumptions),
        options=json.loads(c.options),
        principles=json.loads(c.principles),
        modern_scenario=json.loads(c.modern_scenario),
        sources=json.loads(c.sources)
    )

# -------------------------------------------------------------
# SIMULATION & DECISION ENGINE
# -------------------------------------------------------------

@app.post("/api/decisions", response_model=DecisionAnalysisResponse)
def submit_epic_decision(req: DecisionSubmitRequest, db: Session = Depends(get_db)):
    case = db.query(CaseModel).filter(CaseModel.id == req.case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")

    options_list = json.loads(case.options)
    chosen_opt = next((opt for opt in options_list if opt["id"] == req.chosen_option_id), None)
    if not chosen_opt:
        raise HTTPException(status_code=400, detail="Invalid option selected")

    base_scores = chosen_opt["reasoning_dimensions"]
    adjusted_scores = dict(base_scores)

    # Contextual adjustment based on prioritized user values
    priorities = req.value_priorities
    if priorities:
        # If user explicitly prioritized duty/justice, slight boost in responsibility
        if priorities.get("Duty vs Compassion", 50) > 70:
            adjusted_scores["responsibility"] = min(100, adjusted_scores["responsibility"] + 3)
        if priorities.get("Prudent Strategy vs Desperate Heroism", 50) > 70:
            adjusted_scores["risk_awareness"] = min(100, adjusted_scores["risk_awareness"] + 3)

    principles_list = json.loads(case.principles)
    lead_principle = principles_list[0] if principles_list else None
    modern_scen = json.loads(case.modern_scenario)

    decision_id = str(uuid.uuid4())
    decision_record = SimulationDecisionModel(
        id=decision_id,
        session_id=req.session_id,
        case_id=req.case_id,
        chosen_option_id=req.chosen_option_id,
        value_priorities=json.dumps(req.value_priorities),
        reasoning_tags=json.dumps(req.reasoning_tags),
        reasoning_text=req.reasoning_text,
        reasoning_scores=json.dumps(adjusted_scores),
        consequences=json.dumps(chosen_opt["consequence"])
    )
    db.add(decision_record)
    db.commit()

    # Analytical diagnosis of strengths, blindspots, and trade-offs
    analysis = {
        "profile_statement": "This profile maps cognitive and moral reasoning patterns, not moral worth.",
        "dominant_strength": (
            "Exceptional systemic responsibility and adherence to collective duty."
            if adjusted_scores["responsibility"] >= 80 else
            "Strong strategic caution and awareness of immediate human vulnerability."
        ),
        "primary_blindspot": (
            "May risk severe emotional sorrow and high collateral burden on close relationships."
            if adjusted_scores["responsibility"] >= 85 and adjusted_scores["long_term_thinking"] >= 80 else
            "Short-term risk aversion may sacrifice long-term structural integrity and justice."
        ),
        "tradeoff_summary": chosen_opt["consequence"]["ethical_tradeoff"]
    }

    return DecisionAnalysisResponse(
        decision_id=decision_id,
        case_id=req.case_id,
        chosen_option=chosen_opt,
        reasoning_scores=ReasoningDimensions(**adjusted_scores),
        consequence=chosen_opt["consequence"],
        analysis_breakdown=analysis,
        mahabharata_principle=lead_principle,
        modern_scenario=modern_scen
    )

@app.post("/api/decisions/modern", response_model=ModernDecisionResponse)
def submit_modern_decision(req: ModernDecisionSubmitRequest, db: Session = Depends(get_db)):
    decision_record = db.query(SimulationDecisionModel).filter(
        SimulationDecisionModel.id == req.decision_id
    ).first()
    if not decision_record:
        raise HTTPException(status_code=404, detail="Decision session record not found")

    case = db.query(CaseModel).filter(CaseModel.id == req.case_id).first()
    modern_scenario = json.loads(case.modern_scenario)
    chosen_mod = next((m for m in modern_scenario["options"] if m["id"] == req.modern_option_id), None)
    if not chosen_mod:
        raise HTTPException(status_code=400, detail="Invalid modern option selected")

    decision_record.modern_option_id = req.modern_option_id
    decision_record.modern_reasoning = req.modern_reasoning
    decision_record.modern_consequences = json.dumps({
        "option_title": chosen_mod["title"],
        "tradeoff": chosen_mod["primary_tradeoff"],
        "preview": chosen_mod["consequence_preview"]
    })
    db.commit()

    return ModernDecisionResponse(
        decision_id=req.decision_id,
        modern_option_id=req.modern_option_id,
        evaluation_summary=f"You chose '{chosen_mod['title']}'. Tradeoff: {chosen_mod['primary_tradeoff']}",
        bridge_insight=(
            f"Your modern choice reflects the same tension examined in the Mahābhārata: balancing "
            f"immediate personal loyalty with institutional accountability and cosmic equity."
        )
    )

# -------------------------------------------------------------
# REFLECTION ENGINE
# -------------------------------------------------------------

@app.post("/api/reflections", response_model=ReflectionReportResponse)
def save_reflection(req: ReflectionSubmitRequest, db: Session = Depends(get_db)):
    decision = db.query(SimulationDecisionModel).filter(SimulationDecisionModel.id == req.decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Associated decision not found")

    case = db.query(CaseModel).filter(CaseModel.id == req.case_id).first()
    options_list = json.loads(case.options)
    chosen_opt = next((opt for opt in options_list if opt["id"] == decision.chosen_option_id), None)
    principles_list = json.loads(case.principles)

    ref_id = str(uuid.uuid4())
    ref_record = ReflectionModel(
        id=ref_id,
        session_id=req.session_id,
        case_id=req.case_id,
        decision_id=req.decision_id,
        answers=json.dumps(req.answers),
        synthesized_takeaway=req.synthesized_takeaway,
        personal_commitment=req.personal_commitment
    )
    db.add(ref_record)
    db.commit()

    scores_dict = json.loads(decision.reasoning_scores)

    strengths = [
        "Identified key stakeholders early in the deliberation process.",
        "Articulated reasoned trade-offs rather than evading conflict.",
        "Demonstrated reflective openness to alternative outcomes."
    ]
    blind_spots = [
        "Consider how long-term second-order effects might ripple outward to silent stakeholders.",
        "Notice where personal affection or fear of blame may introduce unconscious bias."
    ]

    return ReflectionReportResponse(
        id=ref_id,
        case_id=case.id,
        case_title=case.title,
        parva=case.parva,
        epic_option_chosen=decision.chosen_option_id,
        epic_option_title=chosen_opt["title"] if chosen_opt else "Custom Option",
        modern_option_chosen=decision.modern_option_id,
        reasoning_scores=ReasoningDimensions(**scores_dict),
        answers=req.answers,
        synthesized_takeaway=req.synthesized_takeaway,
        personal_commitment=req.personal_commitment,
        created_at=datetime.utcnow(),
        strengths=strengths,
        blind_spots=blind_spots,
        core_principle=principles_list[0] if principles_list else None
    )

@app.get("/api/reflections/{decision_id}", response_model=ReflectionReportResponse)
def get_reflection_by_decision(decision_id: str, db: Session = Depends(get_db)):
    ref_record = db.query(ReflectionModel).filter(ReflectionModel.decision_id == decision_id).first()
    if not ref_record:
        raise HTTPException(status_code=404, detail="Reflection record not found")

    decision = db.query(SimulationDecisionModel).filter(SimulationDecisionModel.id == decision_id).first()
    case = db.query(CaseModel).filter(CaseModel.id == decision.case_id).first()
    options_list = json.loads(case.options)
    chosen_opt = next((opt for opt in options_list if opt["id"] == decision.chosen_option_id), None)
    principles_list = json.loads(case.principles)
    scores_dict = json.loads(decision.reasoning_scores)

    return ReflectionReportResponse(
        id=ref_record.id,
        case_id=case.id,
        case_title=case.title,
        parva=case.parva,
        epic_option_chosen=decision.chosen_option_id,
        epic_option_title=chosen_opt["title"] if chosen_opt else "",
        modern_option_chosen=decision.modern_option_id,
        reasoning_scores=ReasoningDimensions(**scores_dict),
        answers=json.loads(ref_record.answers),
        synthesized_takeaway=ref_record.synthesized_takeaway,
        personal_commitment=ref_record.personal_commitment,
        created_at=ref_record.created_at,
        strengths=["Clear articulation of ethical constraints.", "High stakeholder empathy."],
        blind_spots=["Re-evaluating decisions under asymmetrical information."],
        core_principle=principles_list[0] if principles_list else None
    )

# -------------------------------------------------------------
# DASHBOARD & LEARNING ANALYTICS
# -------------------------------------------------------------

@app.get("/api/analytics/dashboard")
def get_dashboard_analytics(session_id: Optional[str] = None, db: Session = Depends(get_db)):
    total_cases = db.query(CaseModel).count()
    
    query = db.query(SimulationDecisionModel)
    if session_id:
        decisions = query.filter(SimulationDecisionModel.session_id == session_id).all()
    else:
        decisions = query.all()

    completed_case_ids = list(set([d.case_id for d in decisions]))
    completed_count = len(completed_case_ids)

    # Compute aggregate reasoning dimensions across decisions
    dimension_totals = {
        "responsibility": 0,
        "strategic_thinking": 0,
        "stakeholder_awareness": 0,
        "long_term_thinking": 0,
        "ethical_consistency": 0,
        "risk_awareness": 0
    }
    
    if decisions:
        for d in decisions:
            scores = json.loads(d.reasoning_scores)
            for k in dimension_totals:
                dimension_totals[k] += scores.get(k, 50)
        avg_dimensions = {k: round(v / len(decisions), 1) for k, v in dimension_totals.items()}
    else:
        # Default baseline
        avg_dimensions = {
            "responsibility": 0,
            "strategic_thinking": 0,
            "stakeholder_awareness": 0,
            "long_term_thinking": 0,
            "ethical_consistency": 0,
            "risk_awareness": 0
        }

    # Earned badges
    badges = []
    if completed_count >= 1:
        badges.append({
            "id": "first-decision",
            "title": "First Decision",
            "description": "Entered the crucible and committed your first difficult choice.",
            "icon": "compass",
            "earned": True
        })
    else:
        badges.append({
            "id": "first-decision",
            "title": "First Decision",
            "description": "Enter the crucible and commit your first difficult choice.",
            "icon": "compass",
            "earned": False
        })

    if avg_dimensions["strategic_thinking"] >= 75 and completed_count >= 1:
        badges.append({
            "id": "strategic-thinker",
            "title": "Strategic Thinker",
            "description": "Demonstrated nuanced foresight and consequence balancing.",
            "icon": "shield",
            "earned": True
        })
    else:
        badges.append({
            "id": "strategic-thinker",
            "title": "Strategic Thinker",
            "description": "Attain over 75 in strategic consequence reasoning.",
            "icon": "shield",
            "earned": False
        })

    if avg_dimensions["stakeholder_awareness"] >= 80 and completed_count >= 1:
        badges.append({
            "id": "stakeholder-analyst",
            "title": "Stakeholder Analyst",
            "description": "Accurately weighted multi-party interests across the ecosystem.",
            "icon": "users",
            "earned": True
        })
    else:
        badges.append({
            "id": "stakeholder-analyst",
            "title": "Stakeholder Analyst",
            "description": "Deeply evaluate multi-party stakeholder impacts.",
            "icon": "users",
            "earned": False
        })

    reflections_count = db.query(ReflectionModel).count()
    if reflections_count >= 1:
        badges.append({
            "id": "reflection-master",
            "title": "Reflection Practitioner",
            "description": "Transferred epic principles into practical modern commitments.",
            "icon": "book-open",
            "earned": True
        })
    else:
        badges.append({
            "id": "reflection-master",
            "title": "Reflection Practitioner",
            "description": "Complete and record an in-depth ethical reflection report.",
            "icon": "book-open",
            "earned": False
        })

    if completed_count >= 5:
        badges.append({
            "id": "five-cases",
            "title": "Dharma Explorer",
            "description": "Completed five intricate Mahābhārata simulations.",
            "icon": "award",
            "earned": True
        })
    else:
        badges.append({
            "id": "five-cases",
            "title": "Dharma Explorer",
            "description": "Complete at least five cases to earn this distinction.",
            "icon": "award",
            "earned": False
        })

    # Recent activity
    recent_history = []
    for d in decisions[-5:]:
        c = db.query(CaseModel).filter(CaseModel.id == d.case_id).first()
        recent_history.append({
            "decision_id": d.id,
            "case_id": d.case_id,
            "case_title": c.title if c else "Unknown Case",
            "parva": c.parva if c else "",
            "chosen_option": d.chosen_option_id,
            "created_at": d.created_at.isoformat()
        })

    return {
        "total_cases_available": total_cases,
        "cases_completed": completed_count,
        "completion_rate_percentage": round((completed_count / max(1, total_cases)) * 100, 1),
        "reasoning_dimensions": avg_dimensions,
        "badges": badges,
        "recent_history": recent_history,
        "has_formed_profile": completed_count >= 1
    }

# -------------------------------------------------------------
# KNOWLEDGE GRAPH
# -------------------------------------------------------------

@app.get("/api/graph", response_model=KnowledgeGraphData)
def get_knowledge_graph(db: Session = Depends(get_db)):
    nodes: List[GraphNode] = []
    edges: List[GraphEdge] = []
    node_ids = set()

    cases = db.query(CaseModel).all()

    for c in cases:
        # Case / Dilemma Node
        if c.id not in node_ids:
            nodes.append(GraphNode(
                id=c.id,
                label=c.title,
                type="dilemma",
                description=c.category
            ))
            node_ids.add(c.id)

        # Parva Node
        parva_id = f"parva-{c.parva.replace(' ', '-').lower()}"
        if parva_id not in node_ids:
            nodes.append(GraphNode(
                id=parva_id,
                label=c.parva,
                type="parva",
                description=f"Mahābhārata Section: {c.parva}"
            ))
            node_ids.add(parva_id)
        edges.append(GraphEdge(source=parva_id, target=c.id, relation="CONTAINS"))

        # Characters
        chars = json.loads(c.characters)
        for char in chars:
            char_id = f"char-{char.replace(' ', '-').lower()}"
            if char_id not in node_ids:
                nodes.append(GraphNode(
                    id=char_id,
                    label=char,
                    type="character",
                    description=f"Key protagonist in {c.parva}"
                ))
                node_ids.add(char_id)
            edges.append(GraphEdge(source=char_id, target=c.id, relation="APPEARS_IN"))

        # Principles
        principles = json.loads(c.principles)
        for pr in principles:
            pr_id = f"pr-{pr['id']}"
            if pr_id not in node_ids:
                nodes.append(GraphNode(
                    id=pr_id,
                    label=pr["name"],
                    type="principle",
                    description=pr["sanskrit_term"]
                ))
                node_ids.add(pr_id)
            edges.append(GraphEdge(source=c.id, target=pr_id, relation="ILLUSTRATES"))

            # Modern Scenario
            mod = json.loads(c.modern_scenario)
            mod_id = f"mod-{mod['id']}"
            if mod_id not in node_ids:
                nodes.append(GraphNode(
                    id=mod_id,
                    label=mod["title"],
                    type="modern_scenario",
                    description=mod["domain"]
                ))
                node_ids.add(mod_id)
            edges.append(GraphEdge(source=pr_id, target=mod_id, relation="APPLIES_TO"))

    return KnowledgeGraphData(nodes=nodes, edges=edges)

# -------------------------------------------------------------
# SCHOLARLY SOURCES
# -------------------------------------------------------------

@app.get("/api/sources")
def get_all_sources(db: Session = Depends(get_db)):
    cases = db.query(CaseModel).order_by(CaseModel.order_index.asc()).all()
    all_sources = []
    for c in cases:
        sources_list = json.loads(c.sources)
        for s in sources_list:
            all_sources.append({
                "case_id": c.id,
                "case_title": c.title,
                "parva": c.parva,
                **s
            })
    return {
        "methodology": (
            "All Mahābhārata textual episodes are sourced from established Critical Editions (primarily BORI - "
            "Bhandarkar Oriental Research Institute, Pune, 1919-1966) and authoritative academic translations "
            "(J.A.B. van Buitenen, Kisari Mohan Ganguli, Bibek Debroy). Principles are framed using peer-reviewed "
            "Indian Knowledge Systems (IKS) frameworks."
        ),
        "sources": all_sources
    }

# -------------------------------------------------------------
# RESEARCH EVALUATION MODULE (Pre-test, Post-test, SUS)
# -------------------------------------------------------------

@app.post("/api/evaluation/pre")
def submit_pre_test(eval_req: PrePostEvaluationSubmit, db: Session = Depends(get_db)):
    answers = eval_req.answers
    # Objective scoring based on multi-stakeholder & trade-off recognition
    # Each correct multi-dimensional answer gives 25 points out of 100
    score = 0
    if answers.get("q1") == "B": score += 25  # Recognizes competing obligations
    if answers.get("q2") == "C": score += 25  # Identifies secondary consequence
    if answers.get("q3") == "A": score += 25  # Multi-stakeholder triage
    if answers.get("q4") == "D": score += 25  # Distinguishes deontology from emotion

    rec = EvaluationResponseModel(
        id=str(uuid.uuid4()),
        session_id=eval_req.session_id,
        test_type="pre",
        score=float(score),
        answers=json.dumps(answers)
    )
    db.add(rec)
    db.commit()

    return {
        "status": "recorded",
        "test_type": "pre",
        "score": score,
        "message": "Baseline decision-reasoning assessment recorded."
    }

@app.post("/api/evaluation/post")
def submit_post_test(eval_req: PrePostEvaluationSubmit, db: Session = Depends(get_db)):
    answers = eval_req.answers
    score = 0
    if answers.get("q1") == "B": score += 25
    if answers.get("q2") == "C": score += 25
    if answers.get("q3") == "A": score += 25
    if answers.get("q4") == "D": score += 25

    rec = EvaluationResponseModel(
        id=str(uuid.uuid4()),
        session_id=eval_req.session_id,
        test_type="post",
        score=float(score),
        answers=json.dumps(answers)
    )
    db.add(rec)
    db.commit()

    # Compare against user's pre-test if available
    pre = db.query(EvaluationResponseModel).filter(
        EvaluationResponseModel.session_id == eval_req.session_id,
        EvaluationResponseModel.test_type == "pre"
    ).order_by(EvaluationResponseModel.created_at.desc()).first()

    pre_score = pre.score if pre else None
    improvement = (score - pre_score) if pre_score is not None else None

    return {
        "status": "recorded",
        "test_type": "post",
        "post_score": score,
        "pre_score": pre_score,
        "improvement_points": improvement,
        "percentage_gain": round(((score - pre_score) / max(1, pre_score)) * 100, 1) if pre_score else None
    }

@app.post("/api/evaluation/sus")
def submit_sus(sus_req: SUsFeedbackSubmit, db: Session = Depends(get_db)):
    # Calculate System Usability Scale (SUS) score
    # Odd questions: score - 1
    # Even questions: 5 - score
    # Sum * 2.5 gives 0-100 scale
    total = 0
    for i in range(1, 11):
        q_val = sus_req.responses.get(f"q{i}", 3)
        if i % 2 == 1:
            total += (q_val - 1)
        else:
            total += (5 - q_val)
    sus_score = total * 2.5

    rec = EvaluationResponseModel(
        id=str(uuid.uuid4()),
        session_id=sus_req.session_id,
        test_type="sus",
        score=float(sus_score),
        answers=json.dumps({
            "responses": sus_req.responses,
            "qualitative": sus_req.qualitative_feedback
        })
    )
    db.add(rec)
    db.commit()

    return {
        "sus_score": round(sus_score, 1),
        "grade": "Excellent" if sus_score >= 80.3 else ("Good" if sus_score >= 68 else "OK"),
        "status": "recorded"
    }

@app.get("/api/evaluation/stats")
def get_evaluation_stats(db: Session = Depends(get_db)):
    pre_tests = db.query(EvaluationResponseModel).filter(EvaluationResponseModel.test_type == "pre").all()
    post_tests = db.query(EvaluationResponseModel).filter(EvaluationResponseModel.test_type == "post").all()
    sus_tests = db.query(EvaluationResponseModel).filter(EvaluationResponseModel.test_type == "sus").all()

    if len(pre_tests) == 0 and len(post_tests) == 0:
        return {
            "status": "awaiting_data",
            "participant_count": 0,
            "pre_average": None,
            "post_average": None,
            "average_improvement": None,
            "sus_average": None,
            "message": "Awaiting participant cohort data. Complete the Pre-Test and Post-Test to populate live statistics."
        }

    pre_avg = sum([p.score for p in pre_tests]) / max(1, len(pre_tests)) if pre_tests else 0
    post_avg = sum([p.score for p in post_tests]) / max(1, len(post_tests)) if post_tests else 0
    sus_avg = sum([s.score for s in sus_tests]) / max(1, len(sus_tests)) if sus_tests else 0

    return {
        "status": "active",
        "participant_count": len(pre_tests),
        "pre_average": round(pre_avg, 1),
        "post_average": round(post_avg, 1),
        "average_improvement": round(post_avg - pre_avg, 1),
        "sus_average": round(sus_avg, 1),
        "message": f"Based on {len(pre_tests)} recorded research evaluations."
    }

# -------------------------------------------------------------
# A QUESTION FOR THE GITA ENDPOINTS
# -------------------------------------------------------------

@app.get("/api/gita/verses", response_model=List[GitaVerse])
def get_gita_verses():
    """Returns the curated collection of verified Bhagavad Gita verses."""
    return GITA_VERSES

@app.get("/api/gita/verses/{verse_id}", response_model=GitaVerse)
def get_gita_verse_by_id(verse_id: str):
    """Returns a specific verified Bhagavad Gita verse by chapter.verse (e.g. '2.47')."""
    for v in GITA_VERSES:
        if v["id"] == verse_id:
            return v
    raise HTTPException(status_code=404, detail="Verse not found in curated collection")

@app.post("/api/gita/perspective", response_model=GitaPerspectiveResponse)
def get_gita_perspective(request: GitaQuestionRequest):
    """
    Given a user's situation or problem, finds a relevant Bhagavad Gita verse
    from the verified local database and provides a thoughtful perspective.
    Does NOT diagnose, judge, or claim scripture is a magic cure.
    Does NOT store the user's question.
    """
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Please enter a situation or question.")
    
    # 1. Deterministic matching with curated dataset
    result = find_gita_perspective(request.question)
    
    # 2. Optional AI enhancement if an API key is configured
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if openai_key and not result.get("crisis_notice"):
        try:
            import urllib.request
            import json as pyjson
            
            v = result["verse"]
            prompt = (
                f"User situation: {request.question}\n\n"
                f"Selected Bhagavad Gita teaching: Chapter {v['chapter']}, Verse {v['verse']}.\n"
                f"Translation: {v['translation']}\n"
                f"Core theme: {', '.join(v['themes'])}\n\n"
                f"Task: Write 2-3 thoughtful sentences explaining how this teaching may offer a useful perspective on the user's situation.\n"
                f"CRITICAL GUIDELINES:\n"
                f"- Use sensitive, exploratory language like 'One perspective from the Bhagavad Gita is...', 'This teaching may offer a useful way to look at your situation...'\n"
                f"- DO NOT say 'The Gita says you should...', 'The Gita proves...', or 'This verse solves your problem.'\n"
                f"- DO NOT diagnose the user or offer medical/psychological/legal conclusions.\n"
                f"- Keep the tone calm, literary, respectful, and human."
            )
            
            req_data = pyjson.dumps({
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a thoughtful scholar of Indian philosophy and literature offering gentle perspectives from the Bhagavad Gita."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 200
            }).encode("utf-8")
            
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=req_data,
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {openai_key}"}
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                resp_body = pyjson.loads(resp.read().decode("utf-8"))
                ai_text = resp_body["choices"][0]["message"]["content"].strip()
                if ai_text:
                    result["why_relevant"] = ai_text
        except Exception:
            # Gracefully preserve the deterministic curated explanation
            pass

    return result
