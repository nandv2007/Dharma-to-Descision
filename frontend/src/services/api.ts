import {
  StorySummary,
  StoryDetail,
  DecisionSubmitRequest,
  DecisionAnalysisResponse,
  ModernDecisionSubmitRequest,
  ModernDecisionResponse,
  ReflectionSubmitRequest,
} from '../types';

const rawApiUrl = import.meta.env.VITE_API_URL;
const normalizedApiUrl = rawApiUrl
  ? (rawApiUrl.startsWith('http://') || rawApiUrl.startsWith('https://') ? rawApiUrl : `https://${rawApiUrl}`)
  : '';

const API_BASE = normalizedApiUrl || (typeof window !== 'undefined' && window.location.port === '5173' ? 'http://127.0.0.1:8000' : '');

export function getSessionId(): string {
  let sid = localStorage.getItem('dharma_session_id');
  if (!sid) {
    sid = 'reader_' + Math.random().toString(36).substring(2, 9);
    localStorage.setItem('dharma_session_id', sid);
  }
  return sid;
}

export const api = {
  async getStories(): Promise<StorySummary[]> {
    const res = await fetch(`${API_BASE}/api/cases`);
    if (!res.ok) throw new Error('Failed to load stories');
    return res.json();
  },

  async getStoryDetail(storyId: string): Promise<StoryDetail> {
    const res = await fetch(`${API_BASE}/api/cases/${storyId}`);
    if (!res.ok) throw new Error(`Failed to load story ${storyId}`);
    return res.json();
  },

  async submitDecision(data: DecisionSubmitRequest): Promise<DecisionAnalysisResponse> {
    const res = await fetch(`${API_BASE}/api/decisions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error('Failed to record decision');
    return res.json();
  },

  async submitModernDecision(data: ModernDecisionSubmitRequest): Promise<ModernDecisionResponse> {
    const res = await fetch(`${API_BASE}/api/decisions/modern`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error('Failed to record modern decision');
    return res.json();
  },

  async saveReflection(data: ReflectionSubmitRequest): Promise<any> {
    const res = await fetch(`${API_BASE}/api/reflections`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error('Failed to save reflection');
    return res.json();
  },

  async getGitaVerses(): Promise<import('../types').GitaVerse[]> {
    const res = await fetch(`${API_BASE}/api/gita/verses`);
    if (!res.ok) throw new Error('Failed to load verses');
    return res.json();
  },

  async getGitaVerseById(verseId: string): Promise<import('../types').GitaVerse> {
    const res = await fetch(`${API_BASE}/api/gita/verses/${verseId}`);
    if (!res.ok) throw new Error(`Failed to load verse ${verseId}`);
    return res.json();
  },

  async getGitaPerspective(question: string): Promise<import('../types').GitaPerspectiveResponse> {
    const res = await fetch(`${API_BASE}/api/gita/perspective`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Failed to find perspective');
    }
    return res.json();
  },
};
