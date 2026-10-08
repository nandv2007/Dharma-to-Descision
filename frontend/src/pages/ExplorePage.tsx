import React, { useState, useEffect } from 'react';
import { StorySummary } from '../types';
import { api } from '../services/api';

interface ExplorePageProps {
  onSelectStory: (storyId: string) => void;
}

export const ExplorePage: React.FC<ExplorePageProps> = ({ onSelectStory }) => {
  const [stories, setStories] = useState<StorySummary[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStories();
  }, []);

  const loadStories = async () => {
    try {
      setLoading(true);
      const data = await api.getStories();
      setStories(data);
    } catch (err) {
      console.error('Failed to load stories:', err);
    } finally {
      setLoading(false);
    }
  };

  // Human, one-sentence literary descriptions for each story
  const descriptions: Record<string, string> = {
    'arjuna-dilemma': 'Arjuna gazes across the lines at Kurukshetra, caught between his obligation as a warrior and the horror of slaying the mentors and kin who raised him.',
    'krishna-peace-mission': 'Krishna enters Hastinapura to offer five modest villages for peace, testing whether one should compromise to the brink of humiliation before turning to war.',
    'yudhishthira-yaksha': 'Standing beside four poisoned brothers at an enchanted pool, Yudhishthira is tested on restraint, truth, and whether justice extends equally beyond his own bloodline.',
    'vidura-counsel': 'In the dead of night, a troubled king summons Vidura for comforting reassurance, forcing the sage to choose between pleasant flattery and unvarnished truth.',
    'karna-loyalty': 'Offered the imperial crown and unity with his true brothers, Karna chooses whether gratitude to a flawed benefactor is higher than universal righteousness.',
    'abhimanyu-chakravyuha': 'A sixteen-year-old warrior enters an impenetrable battle formation with ingress knowledge but no exit strategy, relying on promises of backup that never arrive.',
  };

  return (
    <div className="max-w-4xl mx-auto px-6 py-16 space-y-12">
      {/* Header */}
      <header className="space-y-3 max-w-2xl">
        <h1 className="font-serif text-3xl sm:text-5xl text-[#222421] font-normal">
          The dilemmas
        </h1>
        <p className="text-base sm:text-lg text-[#5A5D56] font-sans leading-relaxed">
          Six moments from the Mahabharata where the choice is harder than it first appears.
        </p>
      </header>

      {/* Stories Archive List */}
      {loading ? (
        <div className="py-16 text-center text-sm text-[#5A5D56]">
          Loading the archive...
        </div>
      ) : (
        <div className="divide-y divide-[#E5E0D5] border-t border-[#E5E0D5]">
          {stories.map((story) => (
            <article
              key={story.id}
              className="py-10 first:pt-8 last:pb-8 space-y-3 group"
            >
              <div className="flex items-baseline justify-between gap-4">
                <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56]">
                  {story.parva}
                </span>
                <span className="text-xs font-serif italic text-[#7E8279]">
                  {story.characters.slice(0, 3).join(', ')}
                </span>
              </div>

              <h2 className="font-serif text-2xl sm:text-3xl text-[#222421] font-normal group-hover:text-[#23483D] transition-colors">
                <button
                  onClick={() => onSelectStory(story.id)}
                  className="text-left"
                >
                  {story.title}
                </button>
              </h2>

              <p className="text-[#5A5D56] text-sm leading-relaxed max-w-2xl font-sans">
                {descriptions[story.id] || story.subtitle}
              </p>

              <div className="pt-2">
                <button
                  onClick={() => onSelectStory(story.id)}
                  className="text-sm font-medium text-[#23483D] hover:text-[#1A362E] inline-flex items-center gap-1.5"
                >
                  <span>Explore this dilemma</span>
                  <span aria-hidden="true">→</span>
                </button>
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
};
