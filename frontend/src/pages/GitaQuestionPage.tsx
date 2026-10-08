import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { GitaPerspectiveResponse, GitaVerse } from '../types';
import { BookOpen, Sparkles, ArrowRight, RefreshCw, AlertCircle, Shield } from 'lucide-react';

const SUGGESTED_QUESTIONS = [
  "I'm afraid I won't succeed.",
  "I don't know whether to forgive someone.",
  "I'm struggling to focus on my work.",
  "I have to make a difficult choice.",
  "I keep comparing myself with others."
];

export const GitaQuestionPage: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<GitaPerspectiveResponse | null>(null);
  const [showFullContext, setShowFullContext] = useState(false);

  // Archive of verses
  const [allVerses, setAllVerses] = useState<GitaVerse[]>([]);
  const [showArchive, setShowArchive] = useState(false);
  const [selectedArchiveVerse, setSelectedArchiveVerse] = useState<GitaVerse | null>(null);

  useEffect(() => {
    // Pre-fetch the curated verses for the quiet archive browser
    api.getGitaVerses()
      .then(setAllVerses)
      .catch(() => {});
  }, []);

  const handleSubmit = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError(null);
    setShowFullContext(false);
    setSelectedArchiveVerse(null);

    try {
      const response = await api.getGitaPerspective(question.trim());
      setResult(response);
      // Smooth scroll down to the response
      setTimeout(() => {
        window.scrollTo({ top: 380, behavior: 'smooth' });
      }, 100);
    } catch (err: any) {
      setError(err.message || 'Unable to retrieve a perspective. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectExample = (example: string) => {
    setQuestion(example);
    setError(null);
  };

  const handleReset = () => {
    setResult(null);
    setQuestion('');
    setShowFullContext(false);
    setSelectedArchiveVerse(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-[#F8F5ED] text-[#222421] selection:bg-[#23483D]/10 selection:text-[#23483D] pb-24">
      {/* Header / Intro */}
      <div className="border-b border-[#222421]/10 bg-white/40">
        <div className="max-w-3xl mx-auto px-6 py-16 md:py-20 text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#23483D]/5 border border-[#23483D]/15 text-xs text-[#23483D] font-medium tracking-wide uppercase mb-6">
            <span>Bhagavad Gītā · Timeless Perspectives</span>
          </div>

          <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl text-[#222421] tracking-tight mb-4">
            A Question for the Gita
          </h1>

          <p className="font-serif italic text-xl md:text-2xl text-[#23483D] mb-6">
            Bring a question. Explore a perspective.
          </p>

          <p className="max-w-xl mx-auto text-base text-[#5C605A] leading-relaxed">
            Sometimes a difficult situation needs a different perspective. Enter a challenge or hesitation you are facing today, and read a verified teaching from the Bhagavad Gita offered for reflection.
          </p>
        </div>
      </div>

      <div className="max-w-3xl mx-auto px-6 mt-12">
        {/* Input Card */}
        <div className="bg-white rounded-2xl border border-[#222421]/10 p-6 md:p-8 shadow-sm">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label htmlFor="user-question" className="block text-sm font-medium text-[#222421] mb-2">
                What are you going through?
              </label>
              <textarea
                id="user-question"
                rows={3}
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="What are you going through?"
                className="w-full px-4 py-3 text-base text-[#222421] placeholder-[#5C605A]/50 bg-[#F8F5ED]/40 border border-[#222421]/15 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#23483D] focus:border-transparent transition-all resize-none leading-relaxed"
              />
            </div>

            {/* Example prompts */}
            <div>
              <p className="text-xs text-[#5C605A] mb-2 font-medium">Or explore one of these situations:</p>
              <div className="flex flex-wrap gap-2">
                {SUGGESTED_QUESTIONS.map((example, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => handleSelectExample(example)}
                    className="text-xs px-3 py-1.5 rounded-lg border border-[#222421]/10 bg-[#F8F5ED]/50 text-[#5C605A] hover:text-[#23483D] hover:border-[#23483D]/30 hover:bg-[#23483D]/5 transition-all text-left"
                  >
                    "{example}"
                  </button>
                ))}
              </div>
            </div>

            {/* Privacy notice and Submit button */}
            <div className="pt-2 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="flex items-center gap-1.5 text-xs text-[#5C605A]/80">
                <Shield className="w-3.5 h-3.5 text-[#23483D]" />
                <span>Private & confidential. Your question is not stored or shared.</span>
              </div>

              <button
                type="submit"
                disabled={loading || !question.trim()}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl bg-[#23483D] text-[#F8F5ED] text-sm font-medium hover:bg-[#1a362d] transition-colors disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
              >
                {loading ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    <span>Contemplating...</span>
                  </>
                ) : (
                  <>
                    <span>Find a perspective</span>
                    <ArrowRight className="w-4 h-4" />
                  </>
                )}
              </button>
            </div>
          </form>

          {error && (
            <div className="mt-4 p-3.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-sm flex items-start gap-2">
              <AlertCircle className="w-4 h-4 mt-0.5 flex-shrink-0 text-amber-700" />
              <span>{error}</span>
            </div>
          )}
        </div>

        {/* Perspective Result */}
        {result && (
          <div className="mt-12 space-y-10 animate-fade-in">
            {/* Crisis Notice if applicable */}
            {result.crisis_notice && (
              <div className="p-5 rounded-2xl bg-amber-50/80 border border-amber-200/80 text-[#222421] text-sm leading-relaxed">
                <div className="flex items-center gap-2 font-medium text-amber-900 mb-2">
                  <AlertCircle className="w-4 h-4 text-amber-700" />
                  <span>Caring Support is Available</span>
                </div>
                <div className="whitespace-pre-line text-xs md:text-sm text-stone-700">
                  {result.crisis_notice}
                </div>
              </div>
            )}

            {/* Reading Book Card */}
            <article className="bg-white rounded-3xl border border-[#222421]/10 p-8 md:p-12 shadow-sm space-y-8">
              {/* Header */}
              <div className="border-b border-[#222421]/10 pb-6">
                <span className="text-xs uppercase tracking-widest text-[#B49A62] font-semibold block mb-2">
                  A perspective from the Bhagavad Gita
                </span>
                <h2 className="font-serif text-2xl md:text-3xl text-[#222421]">
                  Bhagavad Gita · Chapter {result.verse.chapter}, Verse {result.verse.verse}
                </h2>
                <div className="flex flex-wrap gap-1.5 mt-3">
                  {result.matched_themes.map((theme, i) => (
                    <span
                      key={i}
                      className="text-xs px-2.5 py-0.5 rounded-full bg-[#23483D]/5 text-[#23483D] border border-[#23483D]/10"
                    >
                      {theme}
                    </span>
                  ))}
                </div>
              </div>

              {/* Sanskrit Verse & Transliteration */}
              <div className="bg-[#F8F5ED]/60 rounded-2xl p-6 md:p-8 border border-[#222421]/5 text-center space-y-4">
                <p className="font-serif text-lg md:text-xl text-[#222421] leading-relaxed whitespace-pre-line tracking-wide">
                  {result.verse.sanskrit}
                </p>
                <p className="font-serif italic text-sm md:text-base text-[#5C605A] leading-relaxed whitespace-pre-line">
                  {result.verse.transliteration}
                </p>
              </div>

              {/* English Translation */}
              <div className="border-l-2 border-[#B49A62] pl-6 py-1">
                <p className="text-xs uppercase tracking-wider text-[#5C605A] font-medium mb-1">Translation</p>
                <p className="font-serif text-lg md:text-xl text-[#222421] leading-relaxed italic">
                  "{result.verse.translation}"
                </p>
              </div>

              {/* Why this may speak to your situation */}
              <div className="pt-2 space-y-3">
                <h3 className="text-xs uppercase tracking-widest text-[#23483D] font-semibold">
                  Why this may speak to your situation
                </h3>
                <p className="text-base text-[#222421] leading-relaxed">
                  {result.why_relevant}
                </p>
              </div>

              {/* A question to reflect on */}
              <div className="bg-[#23483D]/5 rounded-2xl p-6 border border-[#23483D]/10 space-y-2">
                <h3 className="text-xs uppercase tracking-widest text-[#23483D] font-semibold">
                  A question to reflect on
                </h3>
                <p className="font-serif italic text-base md:text-lg text-[#222421] leading-relaxed">
                  "{result.reflection_question}"
                </p>
              </div>

              {/* Context Toggle */}
              <div className="border-t border-[#222421]/10 pt-6">
                {!showFullContext ? (
                  <button
                    type="button"
                    onClick={() => setShowFullContext(true)}
                    className="inline-flex items-center gap-1.5 text-sm text-[#23483D] hover:underline font-medium"
                  >
                    <span>Explore the full context</span>
                    <span>→</span>
                  </button>
                ) : (
                  <div className="space-y-4 pt-2 animate-fade-in">
                    <div>
                      <h4 className="text-xs uppercase tracking-wider text-[#5C605A] font-medium mb-1">
                        The Setting in the Epic
                      </h4>
                      <p className="text-sm text-[#222421] leading-relaxed">
                        {result.verse.short_context}
                      </p>
                    </div>

                    <div>
                      <h4 className="text-xs uppercase tracking-wider text-[#5C605A] font-medium mb-1">
                        The Core Insight
                      </h4>
                      <p className="text-sm text-[#222421] leading-relaxed">
                        {result.verse.teaching_explanation}
                      </p>
                    </div>

                    <div>
                      <h4 className="text-xs uppercase tracking-wider text-[#5C605A] font-medium mb-1">
                        Timeless Application
                      </h4>
                      <p className="text-sm text-[#222421] leading-relaxed">
                        {result.verse.modern_reflection}
                      </p>
                    </div>

                    <button
                      type="button"
                      onClick={() => setShowFullContext(false)}
                      className="text-xs text-[#5C605A] hover:text-[#222421] underline pt-2 block"
                    >
                      Hide full context
                    </button>
                  </div>
                )}
              </div>

              {/* Reset action */}
              <div className="border-t border-[#222421]/10 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4">
                <button
                  type="button"
                  onClick={handleReset}
                  className="inline-flex items-center gap-2 text-sm text-[#5C605A] hover:text-[#222421] transition-colors"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  <span>Bring another situation</span>
                </button>

                <a
                  href="#explore"
                  className="text-xs text-[#23483D] hover:underline font-medium"
                >
                  Explore Mahābhārata ethical dilemmas →
                </a>
              </div>
            </article>
          </div>
        )}

        {/* Quiet Verse Archive Browser */}
        <div className="mt-20 border-t border-[#222421]/10 pt-10">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="font-serif text-xl text-[#222421]">
                Curated Verse Collection
              </h3>
              <p className="text-xs text-[#5C605A] mt-1">
                20 verified verses across classical themes of human action, mind, and equanimity.
              </p>
            </div>

            <button
              type="button"
              onClick={() => setShowArchive(!showArchive)}
              className="text-xs px-3.5 py-1.5 rounded-lg border border-[#222421]/15 text-[#222421] hover:bg-white transition-colors font-medium"
            >
              {showArchive ? 'Hide collection' : 'Browse verses'}
            </button>
          </div>

          {showArchive && (
            <div className="mt-6 space-y-4 animate-fade-in">
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                {allVerses.map((v) => (
                  <button
                    key={v.id}
                    type="button"
                    onClick={() => setSelectedArchiveVerse(v)}
                    className={`p-3.5 text-left rounded-xl border transition-all ${
                      selectedArchiveVerse?.id === v.id
                        ? 'border-[#23483D] bg-white ring-1 ring-[#23483D]'
                        : 'border-[#222421]/10 bg-white/60 hover:bg-white hover:border-[#222421]/20'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-serif font-medium text-xs text-[#222421]">
                        Gita {v.chapter}.{v.verse}
                      </span>
                      <span className="text-[10px] text-[#B49A62] font-semibold uppercase">
                        {v.themes[0]}
                      </span>
                    </div>
                    <p className="text-xs text-[#5C605A] line-clamp-2 italic">
                      "{v.translation}"
                    </p>
                  </button>
                ))}
              </div>

              {selectedArchiveVerse && (
                <div className="mt-6 bg-white rounded-2xl border border-[#222421]/10 p-6 md:p-8 space-y-6">
                  <div className="flex items-center justify-between border-b border-[#222421]/10 pb-4">
                    <div>
                      <span className="text-xs text-[#B49A62] font-semibold uppercase tracking-wider block">
                        Verified Passage
                      </span>
                      <h4 className="font-serif text-xl text-[#222421]">
                        Bhagavad Gita · Chapter {selectedArchiveVerse.chapter}, Verse {selectedArchiveVerse.verse}
                      </h4>
                    </div>
                    <button
                      type="button"
                      onClick={() => setSelectedArchiveVerse(null)}
                      className="text-xs text-[#5C605A] hover:text-[#222421]"
                    >
                      Close ✕
                    </button>
                  </div>

                  <div className="bg-[#F8F5ED]/60 rounded-xl p-4 text-center space-y-2">
                    <p className="font-serif text-base text-[#222421] whitespace-pre-line leading-relaxed">
                      {selectedArchiveVerse.sanskrit}
                    </p>
                    <p className="font-serif italic text-xs text-[#5C605A] whitespace-pre-line">
                      {selectedArchiveVerse.transliteration}
                    </p>
                  </div>

                  <div>
                    <p className="text-xs uppercase text-[#5C605A] font-medium mb-1">Translation</p>
                    <p className="font-serif italic text-base text-[#222421] leading-relaxed">
                      "{selectedArchiveVerse.translation}"
                    </p>
                  </div>

                  <div>
                    <p className="text-xs uppercase text-[#23483D] font-medium mb-1">The Teaching</p>
                    <p className="text-sm text-[#222421] leading-relaxed">
                      {selectedArchiveVerse.teaching_explanation}
                    </p>
                  </div>

                  <div className="p-4 rounded-xl bg-[#23483D]/5 border border-[#23483D]/10">
                    <p className="text-xs uppercase text-[#23483D] font-medium mb-1">Reflection Question</p>
                    <p className="font-serif italic text-sm text-[#222421]">
                      "{selectedArchiveVerse.reflection_question}"
                    </p>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
