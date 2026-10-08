export interface ScholarlySource {
  text: string;
  parva: string;
  chapter_section: string;
  critical_edition_ref?: string;
  scholar_translation: string;
  scholarly_note: string;
  archive_link?: string;
  case_id?: string;
  case_title?: string;
}

export interface ModernOption {
  id: string;
  title: string;
  description: string;
  primary_tradeoff: string;
  consequence_preview: string;
}

export interface ModernScenario {
  id: string;
  title: string;
  domain: string;
  context: string;
  dilemma: string;
  parallel_to_epic: string;
  options: ModernOption[];
}

export interface OptionConsequence {
  immediate_effect: string;
  secondary_consequence: string;
  stakeholder_impact: Record<string, string>;
  strategic_impact: string;
  ethical_tradeoff: string;
  long_term_risk: string;
  unintended_consequence: string;
}

export interface DecisionOption {
  id: string;
  title: string;
  description: string;
  core_rationale: string;
  advantages: string[];
  risks: string[];
  consequence: OptionConsequence;
}

export interface Principle {
  id: string;
  name: string;
  sanskrit_term: string;
  definition: string;
  episode_connection: string;
  modern_application: string;
  key_insight: string;
}

export interface StorySummary {
  id: string;
  title: string;
  subtitle?: string;
  parva: string;
  chapter_reference: string;
  characters: string[];
  category: string;
  order_index: number;
}

export interface StoryDetail extends StorySummary {
  context: string;
  dilemma: string;
  why_difficult: string;
  options: DecisionOption[];
  principles: Principle[];
  modern_scenario: ModernScenario;
  sources: ScholarlySource[];
}

export interface DecisionSubmitRequest {
  session_id: string;
  case_id: string;
  chosen_option_id: string;
  reasoning_text?: string;
}

export interface DecisionAnalysisResponse {
  decision_id: string;
  case_id: string;
  chosen_option: DecisionOption;
  consequence: OptionConsequence;
  mahabharata_principle: Principle;
  modern_scenario: ModernScenario;
}

export interface ModernDecisionSubmitRequest {
  decision_id: string;
  session_id: string;
  case_id: string;
  modern_option_id: string;
  modern_reasoning?: string;
}

export interface ModernDecisionResponse {
  decision_id: string;
  modern_option_id: string;
  evaluation_summary: string;
  bridge_insight: string;
}

export interface ReflectionSubmitRequest {
  session_id: string;
  case_id: string;
  decision_id: string;
  answers: Record<string, string>;
  personal_commitment?: string;
}

export interface GitaVerse {
  id: string;
  chapter: number;
  verse: string;
  sanskrit: string;
  transliteration: string;
  translation: string;
  themes: string[];
  short_context: string;
  teaching_explanation: string;
  modern_reflection: string;
  reflection_question: string;
}

export interface GitaPerspectiveResponse {
  verse: GitaVerse;
  why_relevant: string;
  reflection_question: string;
  matched_themes: string[];
  crisis_notice?: string | null;
}
