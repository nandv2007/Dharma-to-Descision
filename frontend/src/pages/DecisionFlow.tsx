import React, { useState, useEffect } from 'react';
import { StoryDetail, DecisionOption, ModernOption } from '../types';
import { api, getSessionId } from '../services/api';

interface DecisionFlowProps {
  storyId: string;
  onExit: () => void;
  onExploreOther: () => void;
}

type Screen =
  | 'situation'
  | 'choice'
  | 'reason'
  | 'consequences'
  | 'mahabharata'
  | 'modern'
  | 'reflection';

export const DecisionFlow: React.FC<DecisionFlowProps> = ({
  storyId,
  onExit,
  onExploreOther,
}) => {
  const [story, setStory] = useState<StoryDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [screen, setScreen] = useState<Screen>('situation');

  // Choices
  const [selectedOptionId, setSelectedOptionId] = useState<string>('C');
  const [userReasoning, setUserReasoning] = useState<string>('');
  const [decisionId, setDecisionId] = useState<string>('');
  const [submittingEpic, setSubmittingEpic] = useState(false);

  // Modern scenario choice
  const [selectedModernOptionId, setSelectedModernOptionId] = useState<string>('C');
  const [modernRevealed, setModernRevealed] = useState(false);

  // Final reflection
  const [finalReflection, setFinalReflection] = useState<string>('');
  const [savingReflection, setSavingReflection] = useState(false);

  useEffect(() => {
    loadStory();
  }, [storyId]);

  const loadStory = async () => {
    try {
      setLoading(true);
      const data = await api.getStoryDetail(storyId);
      setStory(data);
      if (data.options.length > 0) {
        setSelectedOptionId(data.options[0].id);
      }
      if (data.modern_scenario?.options?.length > 0) {
        setSelectedModernOptionId(data.modern_scenario.options[0].id);
      }
    } catch (err) {
      console.error('Failed to load story for decision:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCommitChoice = async () => {
    if (!story) return;
    try {
      setSubmittingEpic(true);
      const res = await api.submitDecision({
        session_id: getSessionId(),
        case_id: story.id,
        chosen_option_id: selectedOptionId,
        reasoning_text: userReasoning,
      });
      setDecisionId(res.decision_id);
      setScreen('consequences');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
      console.error('Failed to submit choice:', err);
      // Still proceed gracefully
      setScreen('consequences');
    } finally {
      setSubmittingEpic(false);
    }
  };

  const handleModernChoiceSelect = (optId: string) => {
    setSelectedModernOptionId(optId);
    setModernRevealed(true);
  };

  const handleFinishReflection = async () => {
    if (decisionId && story) {
      try {
        setSavingReflection(true);
        await api.saveReflection({
          session_id: getSessionId(),
          case_id: story.id,
          decision_id: decisionId,
          answers: { reflection: finalReflection },
          personal_commitment: finalReflection,
        });
      } catch (err) {
        console.error('Failed to save reflection:', err);
      } finally {
        setSavingReflection(false);
      }
    }
    onExploreOther();
  };

  if (loading) {
    return (
      <div className="max-w-2xl mx-auto px-6 py-24 text-center text-sm text-[#5A5D56]">
        Loading the dilemma...
      </div>
    );
  }

  if (!story) {
    return (
      <div className="max-w-2xl mx-auto px-6 py-20 text-center space-y-4">
        <p className="text-sm text-[#5A5D56]">Unable to load dilemma.</p>
        <button onClick={onExit} className="text-sm text-[#23483D] underline">
          Return to dilemmas
        </button>
      </div>
    );
  }

  const chosenOption = story.options.find((o) => o.id === selectedOptionId) || story.options[0];
  const chosenModernOption = story.modern_scenario?.options?.find(
    (m) => m.id === selectedModernOptionId
  );

  const screenSteps: { key: Screen; stepNum: number; label: string }[] = [
    { key: 'situation', stepNum: 1, label: 'The Situation' },
    { key: 'choice', stepNum: 2, label: 'The Choice' },
    { key: 'reason', stepNum: 3, label: 'Your Reason' },
    { key: 'consequences', stepNum: 4, label: 'What Might Follow' },
    { key: 'mahabharata', stepNum: 5, label: 'The Mahabharata' },
    { key: 'modern', stepNum: 6, label: 'A Modern Echo' },
    { key: 'reflection', stepNum: 7, label: 'Reflection' },
  ];

  const currentStepInfo = screenSteps.find((s) => s.key === screen);

  return (
    <div className="max-w-2xl mx-auto px-6 py-12 sm:py-16 space-y-10">
      {/* Top Bar with Step & Exit */}
      <div className="flex items-baseline justify-between border-b border-[#E5E0D5] pb-4 text-xs">
        <span className="font-sans text-[#5A5D56]">
          {currentStepInfo?.stepNum} of 7 · {currentStepInfo?.label}
        </span>
        <button
          onClick={onExit}
          className="text-[#5A5D56] hover:text-[#222421] transition-colors"
        >
          Exit
        </button>
      </div>

      {/* =========================================================
          SCREEN 1: THE SITUATION
          ========================================================= */}
      {screen === 'situation' && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              {story.parva}
            </span>
            <h1 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              {story.title}
            </h1>
          </header>

          <div className="space-y-5 text-[#222421] text-base leading-relaxed font-serif">
            <p>{story.context}</p>
          </div>

          <div className="border-l-2 border-[#23483D] pl-5 py-2 my-6 bg-[#F4EFE4]/60 p-5 rounded-r">
            <span className="text-xs font-sans uppercase tracking-wider text-[#23483D] font-medium block mb-1">
              The conflict
            </span>
            <p className="font-serif text-base sm:text-lg text-[#222421] italic leading-relaxed">
              &ldquo;{story.dilemma}&rdquo;
            </p>
          </div>

          <div className="pt-4">
            <button
              onClick={() => {
                setScreen('choice');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>Consider the choices</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 2: THE CHOICE
          ========================================================= */}
      {screen === 'choice' && (
        <div className="space-y-8">
          <header className="space-y-2">
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              What would you do?
            </h2>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              Read each course of action. There are no labels indicating which is right.
            </p>
          </header>

          <div className="space-y-4">
            {story.options.map((option: DecisionOption) => {
              const isSelected = selectedOptionId === option.id;
              return (
                <div
                  key={option.id}
                  onClick={() => setSelectedOptionId(option.id)}
                  className={`p-5 rounded border cursor-pointer transition-colors ${
                    isSelected
                      ? 'border-[#23483D] bg-white ring-1 ring-[#23483D]'
                      : 'border-[#E5E0D5] bg-[#FAF7F0] hover:border-[#B49A62]'
                  }`}
                >
                  <div className="flex items-start gap-3.5">
                    <div className="pt-0.5">
                      <div
                        className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                          isSelected
                            ? 'border-[#23483D] bg-[#23483D]'
                            : 'border-[#7E8279] bg-transparent'
                        }`}
                      >
                        {isSelected && (
                          <div className="w-1.5 h-1.5 rounded-full bg-white" />
                        )}
                      </div>
                    </div>
                    <div className="space-y-1.5">
                      <h3 className="font-serif text-base text-[#222421] font-medium leading-snug">
                        {option.title}
                      </h3>
                      <p className="text-sm text-[#5A5D56] leading-relaxed">
                        {option.description}
                      </p>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="pt-4 flex items-center justify-between">
            <button
              onClick={() => {
                setScreen('situation');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="text-xs text-[#5A5D56] hover:text-[#222421]"
            >
              ← Back to situation
            </button>
            <button
              onClick={() => {
                setScreen('reason');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>Continue</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 3: YOUR CHOICE & REASON
          ========================================================= */}
      {screen === 'reason' && chosenOption && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              Your Decision
            </span>
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              You chose:
            </h2>
          </header>

          <div className="border-l-2 border-[#23483D] pl-5 py-2 space-y-2 bg-[#F4EFE4]/60 p-5 rounded-r">
            <h3 className="font-serif text-lg text-[#222421] font-medium">
              {chosenOption.title}
            </h3>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              {chosenOption.description}
            </p>
          </div>

          <div className="space-y-2 pt-2">
            <label className="text-sm font-serif text-[#222421] block">
              Why would you choose this?{' '}
              <span className="text-xs text-[#5A5D56] font-sans font-normal">
                (Optional)
              </span>
            </label>
            <textarea
              rows={4}
              value={userReasoning}
              onChange={(e) => setUserReasoning(e.target.value)}
              placeholder="What weighed most heavily in your mind?"
              className="w-full bg-white border border-[#E5E0D5] rounded p-3.5 text-sm text-[#222421] placeholder:text-[#A6ABA0] focus:border-[#23483D] focus:outline-none transition-colors"
            />
          </div>

          <div className="pt-4 flex items-center justify-between">
            <button
              onClick={() => {
                setScreen('choice');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="text-xs text-[#5A5D56] hover:text-[#222421]"
            >
              ← Change choice
            </button>
            <button
              onClick={handleCommitChoice}
              disabled={submittingEpic}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2 disabled:opacity-50"
            >
              <span>{submittingEpic ? 'Recording...' : 'See what might follow'}</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 4: WHAT MIGHT FOLLOW
          ========================================================= */}
      {screen === 'consequences' && chosenOption && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              Consequences
            </span>
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              What might follow
            </h2>
            <p className="text-sm text-[#5A5D56]">
              Every path in the epic alters the future. Here are the likely ripples of that choice.
            </p>
          </header>

          <div className="space-y-6 text-sm text-[#222421] leading-relaxed">
            {/* Immediate effect */}
            <div className="space-y-1 border-b border-[#E5E0D5] pb-5">
              <span className="text-xs font-sans uppercase tracking-wider text-[#5A5D56] block font-medium">
                The immediate effect
              </span>
              <p className="font-serif text-base text-[#222421]">
                {chosenOption.consequence.immediate_effect}
              </p>
            </div>

            {/* Potential benefit & risk */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 border-b border-[#E5E0D5] pb-5">
              <div className="space-y-1">
                <span className="text-xs font-sans uppercase tracking-wider text-[#23483D] block font-medium">
                  Potential benefit
                </span>
                <p className="text-[#5A5D56]">
                  {chosenOption.advantages?.join(' ') || chosenOption.consequence.strategic_impact}
                </p>
              </div>

              <div className="space-y-1">
                <span className="text-xs font-sans uppercase tracking-wider text-[#7E8279] block font-medium">
                  Potential risk
                </span>
                <p className="text-[#5A5D56]">
                  {chosenOption.risks?.join(' ') || chosenOption.consequence.long_term_risk}
                </p>
              </div>
            </div>

            {/* Who is affected */}
            <div className="space-y-2 border-b border-[#E5E0D5] pb-5">
              <span className="text-xs font-sans uppercase tracking-wider text-[#5A5D56] block font-medium">
                Who may be affected
              </span>
              <p className="text-[#5A5D56]">
                {chosenOption.consequence.secondary_consequence}
              </p>
            </div>

            {/* Unintended consequence */}
            <div className="space-y-1 pt-1">
              <span className="text-xs font-sans uppercase tracking-wider text-[#7E8279] block font-medium">
                Possible unintended consequence
              </span>
              <p className="text-[#5A5D56] italic font-serif">
                {chosenOption.consequence.unintended_consequence}
              </p>
            </div>
          </div>

          <div className="pt-6 border-t border-[#E5E0D5]">
            <button
              onClick={() => {
                setScreen('mahabharata');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>What happened in the Mahabharata</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 5: THE MAHABHARATA
          ========================================================= */}
      {screen === 'mahabharata' && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              The Original Text
            </span>
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              What happened in the epic
            </h2>
          </header>

          <div className="space-y-6 text-[#222421] text-base leading-relaxed font-serif">
            <p>
              {story.principles?.[0]?.episode_connection || story.context}
            </p>

            <div className="border-l-2 border-[#B49A62] pl-5 py-2 my-6 bg-[#F4EFE4]/60 p-5 rounded-r space-y-2 font-sans text-sm">
              <div className="flex items-baseline justify-between">
                <span className="font-serif text-base text-[#222421] font-medium">
                  {story.principles?.[0]?.name}
                </span>
                <span className="text-xs font-serif italic text-[#7E8279]">
                  {story.principles?.[0]?.sanskrit_term}
                </span>
              </div>
              <p className="text-[#5A5D56] leading-relaxed">
                {story.principles?.[0]?.definition}
              </p>
            </div>
          </div>

          <div className="text-xs text-[#5A5D56] border-t border-[#E5E0D5] pt-4">
            Source: {story.sources?.[0]?.text} ({story.sources?.[0]?.chapter_section})
          </div>

          <div className="pt-4">
            <button
              onClick={() => {
                setScreen('modern');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>Consider a modern echo</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 6: A MODERN ECHO
          ========================================================= */}
      {screen === 'modern' && story.modern_scenario && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              A Modern Echo
            </span>
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              {story.modern_scenario.title}
            </h2>
            <p className="text-sm text-[#5A5D56] font-sans">
              The same underlying dilemma in everyday life.
            </p>
          </header>

          <div className="p-5 rounded bg-[#FAF7F0] border border-[#E5E0D5] text-sm text-[#222421] leading-relaxed space-y-3 font-sans">
            <p>{story.modern_scenario.context}</p>
            <p className="italic font-serif text-[#222421] pt-1">
              &ldquo;{story.modern_scenario.dilemma}&rdquo;
            </p>
          </div>

          <div className="space-y-4">
            <span className="text-xs uppercase tracking-wider text-[#5A5D56] font-medium block">
              What would you do today?
            </span>
            {story.modern_scenario.options.map((mOpt: ModernOption) => {
              const isSelected = selectedModernOptionId === mOpt.id;
              return (
                <div
                  key={mOpt.id}
                  onClick={() => handleModernChoiceSelect(mOpt.id)}
                  className={`p-4 rounded border cursor-pointer transition-colors ${
                    isSelected
                      ? 'border-[#23483D] bg-white ring-1 ring-[#23483D]'
                      : 'border-[#E5E0D5] bg-[#FAF7F0] hover:border-[#B49A62]'
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <div className="pt-0.5">
                      <div
                        className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                          isSelected
                            ? 'border-[#23483D] bg-[#23483D]'
                            : 'border-[#7E8279] bg-transparent'
                        }`}
                      >
                        {isSelected && (
                          <div className="w-1.5 h-1.5 rounded-full bg-white" />
                        )}
                      </div>
                    </div>
                    <div className="space-y-1">
                      <h3 className="font-serif text-sm text-[#222421] font-medium">
                        {mOpt.title}
                      </h3>
                      <p className="text-xs text-[#5A5D56] leading-relaxed">
                        {mOpt.description}
                      </p>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Reveal trade-off quietly */}
          {modernRevealed && chosenModernOption && (
            <div className="border-l-2 border-[#23483D] pl-4 py-2 text-xs space-y-1 bg-[#F4EFE4]/60 p-4 rounded-r">
              <span className="font-medium text-[#23483D] block uppercase tracking-wider">
                The trade-off
              </span>
              <p className="text-[#222421] leading-relaxed">
                {chosenModernOption.primary_tradeoff}
              </p>
            </div>
          )}

          <div className="pt-4 flex justify-end">
            <button
              onClick={() => {
                setScreen('reflection');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>One last question</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}

      {/* =========================================================
          SCREEN 7: ONE LAST QUESTION
          ========================================================= */}
      {screen === 'reflection' && (
        <div className="space-y-8">
          <header className="space-y-2">
            <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56] block">
              Closing Reflection
            </span>
            <h2 className="font-serif text-3xl sm:text-4xl text-[#222421] font-normal">
              Would you make the same choice again?
            </h2>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              Having seen the possible fallout and the parallel in your own world, how does the decision look in hindsight?
            </p>
          </header>

          <div className="space-y-2">
            <label className="text-sm font-serif text-[#222421] block">
              Optional reflection
            </label>
            <textarea
              rows={4}
              value={finalReflection}
              onChange={(e) => setFinalReflection(e.target.value)}
              placeholder="What surprised you about the trade-offs involved?"
              className="w-full bg-white border border-[#E5E0D5] rounded p-3.5 text-sm text-[#222421] placeholder:text-[#A6ABA0] focus:border-[#23483D] focus:outline-none transition-colors"
            />
          </div>

          <div className="pt-6 border-t border-[#E5E0D5] flex items-center justify-between">
            <button
              onClick={handleFinishReflection}
              disabled={savingReflection}
              className="px-6 py-3.5 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
            >
              <span>{savingReflection ? 'Saving...' : 'Explore another dilemma'}</span>
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
