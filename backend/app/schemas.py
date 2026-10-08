from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Stakeholder(BaseModel):
    name: str
    role: str
    interests: str
    risks: str
    expectations: str
    icon_name: Optional[str] = "users"

class CompetingValue(BaseModel):
    name: str
    sanskrit_term: Optional[str] = None
    description: str
    polarity: str  # e.g., "Duty (Kartavya) vs Compassion (Karuna)"
    initial_weight: int = 50

class OptionConsequence(BaseModel):
    immediate_effect: str
    secondary_consequence: str
    stakeholder_impact: Dict[str, str]
    strategic_impact: str
    ethical_tradeoff: str
    long_term_risk: str
    unintended_consequence: str

class ReasoningDimensions(BaseModel):
    responsibility: int = Field(..., ge=0, le=100)
    strategic_thinking: int = Field(..., ge=0, le=100)
    stakeholder_awareness: int = Field(..., ge=0, le=100)
    long_term_thinking: int = Field(..., ge=0, le=100)
    ethical_consistency: int = Field(..., ge=0, le=100)
    risk_awareness: int = Field(..., ge=0, le=100)

class DecisionOption(BaseModel):
    id: str  # "A", "B", "C", "D"
    title: str
    description: str
    core_rationale: str
    advantages: List[str]
    risks: List[str]
    reasoning_dimensions: ReasoningDimensions
    consequence: OptionConsequence

class Principle(BaseModel):
    id: str
    name: str
    sanskrit_term: str
    definition: str
    episode_connection: str
    modern_application: str
    key_insight: str

class ScholarlySource(BaseModel):
    text: str
    parva: str
    chapter_section: str
    critical_edition_ref: Optional[str] = None
    scholar_translation: str
    scholarly_note: str
    archive_link: Optional[str] = None

class ModernOption(BaseModel):
    id: str
    title: str
    description: str
    primary_tradeoff: str
    consequence_preview: str

class ModernScenario(BaseModel):
    id: str
    title: str
    domain: str  # "Academic Integrity", "Corporate Leadership", "Team Dynamics", etc.
    context: str
    dilemma: str
    parallel_to_epic: str
    options: List[ModernOption]

class CaseSummary(BaseModel):
    id: str
    title: str
    subtitle: Optional[str] = None
    parva: str
    chapter_reference: str
    characters: List[str]
    category: str
    strategic_themes: List[str]
    ethical_themes: List[str]
    difficulty: str
    estimated_time: str
    order_index: int

class CaseDetail(CaseSummary):
    context: str
    dilemma: str
    why_difficult: str
    stakeholders: List[Stakeholder]
    competing_values: List[CompetingValue]
    known_information: List[str]
    uncertain_information: List[str]
    assumptions: List[str]
    options: List[DecisionOption]
    principles: List[Principle]
    modern_scenario: ModernScenario
    sources: List[ScholarlySource]

# Decision flow schemas
class DecisionSubmitRequest(BaseModel):
    session_id: str
    case_id: str
    chosen_option_id: str
    value_priorities: Dict[str, int] = Field(default_factory=dict)
    reasoning_tags: List[str] = Field(default_factory=list)
    reasoning_text: str = ""

class DecisionAnalysisResponse(BaseModel):
    decision_id: str
    case_id: str
    chosen_option: DecisionOption
    reasoning_scores: ReasoningDimensions
    consequence: OptionConsequence
    analysis_breakdown: Dict[str, Any]
    mahabharata_principle: Principle
    modern_scenario: ModernScenario

class ModernDecisionSubmitRequest(BaseModel):
    decision_id: str
    session_id: str
    case_id: str
    modern_option_id: str
    modern_reasoning: str = ""

class ModernDecisionResponse(BaseModel):
    decision_id: str
    modern_option_id: str
    evaluation_summary: str
    bridge_insight: str

class ReflectionSubmitRequest(BaseModel):
    session_id: str
    case_id: str
    decision_id: str
    answers: Dict[str, str]
    synthesized_takeaway: Optional[str] = None
    personal_commitment: Optional[str] = None

class ReflectionReportResponse(BaseModel):
    id: str
    case_id: str
    case_title: str
    parva: str
    epic_option_chosen: str
    epic_option_title: str
    modern_option_chosen: Optional[str]
    reasoning_scores: ReasoningDimensions
    answers: Dict[str, str]
    synthesized_takeaway: Optional[str]
    personal_commitment: Optional[str]
    created_at: datetime
    strengths: List[str]
    blind_spots: List[str]
    core_principle: Principle

# Evaluation module
class PrePostEvaluationSubmit(BaseModel):
    session_id: str
    test_type: str  # "pre" or "post"
    answers: Dict[str, Any]

class SUsFeedbackSubmit(BaseModel):
    session_id: str
    responses: Dict[str, int]  # 1 to 5 scale for 10 SUS questions
    qualitative_feedback: Optional[str] = None

# Knowledge Graph schemas
class GraphNode(BaseModel):
    id: str
    label: str
    type: str  # "character", "parva", "dilemma", "principle", "modern_scenario", "value"
    description: Optional[str] = None

class GraphEdge(BaseModel):
    source: str
    target: str
    relation: str  # "APPEARS_IN", "CONTAINS", "INVOLVES", "ILLUSTRATES", "APPLIES_TO"

class KnowledgeGraphData(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]

# Gita Perspective schemas
class GitaVerse(BaseModel):
    id: str
    chapter: int
    verse: str
    sanskrit: str
    transliteration: str
    translation: str
    themes: List[str]
    short_context: str
    teaching_explanation: str
    modern_reflection: str
    reflection_question: str

class GitaQuestionRequest(BaseModel):
    question: str

class GitaPerspectiveResponse(BaseModel):
    verse: GitaVerse
    why_relevant: str
    reflection_question: str
    matched_themes: List[str]
    crisis_notice: Optional[str] = None
