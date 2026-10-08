from datetime import datetime
import json
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class CaseModel(Base):
    __tablename__ = "cases"

    id = Column(String(64), primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    subtitle = Column(String(512), nullable=True)
    parva = Column(String(128), nullable=False)
    chapter_reference = Column(String(256), nullable=False)
    characters = Column(Text, nullable=False)  # JSON list
    category = Column(String(128), nullable=False)
    strategic_themes = Column(Text, nullable=False)  # JSON list
    ethical_themes = Column(Text, nullable=False)  # JSON list
    difficulty = Column(String(32), default="Intermediate")
    estimated_time = Column(String(32), default="12-15 min")
    
    context = Column(Text, nullable=False)
    dilemma = Column(Text, nullable=False)
    why_difficult = Column(Text, nullable=False)
    
    stakeholders = Column(Text, nullable=False)  # JSON list of objects
    competing_values = Column(Text, nullable=False)  # JSON list
    known_information = Column(Text, nullable=False)  # JSON list
    uncertain_information = Column(Text, nullable=False)  # JSON list
    assumptions = Column(Text, nullable=False)  # JSON list
    
    options = Column(Text, nullable=False)  # JSON list of 4 options
    principles = Column(Text, nullable=False)  # JSON list of principles
    modern_scenario = Column(Text, nullable=False)  # JSON object
    sources = Column(Text, nullable=False)  # JSON list of scholarly sources
    
    order_index = Column(Integer, default=0)
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    decisions = relationship("SimulationDecisionModel", back_populates="case", cascade="all, delete-orphan")
    reflections = relationship("ReflectionModel", back_populates="case", cascade="all, delete-orphan")

class SimulationDecisionModel(Base):
    __tablename__ = "simulation_decisions"

    id = Column(String(64), primary_key=True, index=True)
    session_id = Column(String(64), index=True, nullable=False)
    case_id = Column(String(64), ForeignKey("cases.id"), nullable=False)
    chosen_option_id = Column(String(32), nullable=False)
    value_priorities = Column(Text, nullable=True)  # JSON dict
    reasoning_tags = Column(Text, nullable=True)  # JSON list
    reasoning_text = Column(Text, nullable=True)
    reasoning_scores = Column(Text, nullable=False)  # JSON dict of 6 dimensions
    consequences = Column(Text, nullable=False)  # JSON object of generated consequence breakdown
    
    # Modern scenario bridge decision
    modern_option_id = Column(String(32), nullable=True)
    modern_reasoning = Column(Text, nullable=True)
    modern_consequences = Column(Text, nullable=True)  # JSON object
    
    created_at = Column(DateTime, default=datetime.utcnow)

    case = relationship("CaseModel", back_populates="decisions")
    reflections = relationship("ReflectionModel", back_populates="decision", cascade="all, delete-orphan")

class ReflectionModel(Base):
    __tablename__ = "reflections"

    id = Column(String(64), primary_key=True, index=True)
    session_id = Column(String(64), index=True, nullable=False)
    case_id = Column(String(64), ForeignKey("cases.id"), nullable=False)
    decision_id = Column(String(64), ForeignKey("simulation_decisions.id"), nullable=False)
    
    answers = Column(Text, nullable=False)  # JSON dict of question_id -> response
    synthesized_takeaway = Column(Text, nullable=True)
    personal_commitment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    case = relationship("CaseModel", back_populates="reflections")
    decision = relationship("SimulationDecisionModel", back_populates="reflections")

class EvaluationResponseModel(Base):
    __tablename__ = "evaluation_responses"

    id = Column(String(64), primary_key=True, index=True)
    session_id = Column(String(64), index=True, nullable=False)
    test_type = Column(String(32), nullable=False)  # 'pre', 'post', 'sus'
    score = Column(Float, nullable=True)
    answers = Column(Text, nullable=False)  # JSON dict
    created_at = Column(DateTime, default=datetime.utcnow)
