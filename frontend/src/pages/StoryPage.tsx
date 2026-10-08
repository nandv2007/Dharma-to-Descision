import React, { useState, useEffect } from 'react';
import { StoryDetail } from '../types';
import { api } from '../services/api';

interface StoryPageProps {
  storyId: string;
  onBack: () => void;
  onStartDecision: (storyId: string) => void;
}

export const StoryPage: React.FC<StoryPageProps> = ({ storyId, onBack, onStartDecision }) => {
  const [story, setStory] = useState<StoryDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStory();
  }, [storyId]);

  const loadStory = async () => {
    try {
      setLoading(true);
      const data = await api.getStoryDetail(storyId);
      setStory(data);
    } catch (err) {
      console.error('Failed to load story:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-3xl mx-auto px-6 py-24 text-center text-sm text-[#5A5D56]">
        Opening the text...
      </div>
    );
  }

  if (!story) {
    return (
      <div className="max-w-3xl mx-auto px-6 py-20 text-center space-y-4">
        <p className="text-sm text-[#5A5D56]">Story not found.</p>
        <button onClick={onBack} className="text-sm text-[#23483D] underline">
          Back to the dilemmas
        </button>
      </div>
    );
  }

  return (
    <article className="max-w-3xl mx-auto px-6 py-16 space-y-12">
      {/* Back button */}
      <div>
        <button
          onClick={onBack}
          className="text-xs text-[#5A5D56] hover:text-[#222421] transition-colors inline-flex items-center gap-1.5"
        >
          <span aria-hidden="true">←</span>
          <span>All dilemmas</span>
        </button>
      </div>

      {/* Header */}
      <header className="space-y-4 border-b border-[#E5E0D5] pb-10">
        <div className="flex items-baseline justify-between gap-4 text-xs font-sans uppercase tracking-[0.15em] text-[#5A5D56]">
          <span>{story.parva}</span>
          <span>{story.chapter_reference}</span>
        </div>

        <h1 className="font-serif text-3xl sm:text-5xl text-[#222421] font-normal leading-[1.2]">
          {story.title}
        </h1>

        <div className="text-xs font-serif italic text-[#7E8279] pt-1">
          Characters: {story.characters.join(', ')}
        </div>
      </header>

      {/* Narrative Context */}
      <section className="space-y-6 text-[#222421] text-base sm:text-lg leading-relaxed font-serif">
        <p className="first-letter:text-4xl first-letter:font-serif first-letter:font-normal first-letter:float-left first-letter:mr-2.5 first-letter:leading-none">
          {story.context}
        </p>
      </section>

      {/* The Dilemma */}
      <section className="border-l-2 border-[#23483D] pl-6 py-2 space-y-3 bg-[#F4EFE4]/60 p-6 rounded-r">
        <span className="text-xs font-sans uppercase tracking-[0.15em] text-[#23483D] font-medium block">
          The Dilemma
        </span>
        <p className="font-serif text-lg sm:text-xl text-[#222421] leading-relaxed italic">
          &ldquo;{story.dilemma}&rdquo;
        </p>
        <p className="text-sm text-[#5A5D56] font-sans leading-relaxed pt-1">
          {story.why_difficult}
        </p>
      </section>

      {/* Decision CTA */}
      <section className="pt-8 border-t border-[#E5E0D5] space-y-4 text-center sm:text-left">
        <h2 className="font-serif text-2xl text-[#222421] font-normal">
          What would you do?
        </h2>
        <p className="text-sm text-[#5A5D56] max-w-xl">
          Put yourself in this moment. There is no simple formula, and each possible choice carries genuine consequences.
        </p>
        <div className="pt-2">
          <button
            onClick={() => onStartDecision(story.id)}
            className="px-6 py-3.5 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
          >
            <span>Make your choice</span>
            <span aria-hidden="true">→</span>
          </button>
        </div>
      </section>
    </article>
  );
};
