import React from 'react';

interface AboutPageProps {
  onNavigate: (tab: string, storyId?: string) => void;
}

export const AboutPage: React.FC<AboutPageProps> = ({ onNavigate }) => {
  return (
    <article className="max-w-2xl mx-auto px-6 py-16 space-y-12">
      <header className="space-y-4">
        <h1 className="font-serif text-3xl sm:text-5xl text-[#222421] font-normal leading-[1.2]">
          About Dharma to Decisions
        </h1>
      </header>

      <section className="space-y-6 text-[#222421] text-base leading-relaxed font-serif">
        <p>
          Dharma to Decisions is an interactive exploration of difficult choices found in the Mahabharata.
        </p>
        <p>
          Rather than telling visitors what they should believe, the experience asks a simpler question:
        </p>
        <blockquote className="border-l-2 border-[#23483D] pl-5 py-1 text-xl italic text-[#23483D]">
          What would you do?
        </blockquote>
        <p>
          Visitors can explore the original situations, make their own choices, consider the consequences, and reflect on how similar questions appear in everyday life.
        </p>
      </section>

      {/* Sources & Scholarship Section */}
      <section className="border-t border-[#E5E0D5] pt-10 space-y-4 font-sans text-sm text-[#5A5D56]">
        <h2 className="font-serif text-xl text-[#222421] font-normal">
          Sources & Reference Text
        </h2>
        <p className="leading-relaxed">
          The episodes presented here are grounded in classical Sanskrit textual scholarship, primarily referencing:
        </p>
        <ul className="list-disc list-inside space-y-2 text-xs leading-relaxed text-[#222421] pt-1">
          <li>
            <strong>Bhandarkar Oriental Research Institute (BORI)</strong> — Critical Edition of the Mahābhārata (Pune, 1919–1966).
          </li>
          <li>
            <strong>J.A.B. van Buitenen</strong> — <em>The Mahābhārata</em>, Books 1–5 (University of Chicago Press).
          </li>
          <li>
            <strong>Kisari Mohan Ganguli</strong> — <em>The Mahabharata of Krishna-Dwaipayana Vyasa</em> (1883–1896).
          </li>
          <li>
            <strong>IIT Kanpur Gita Supersite</strong> — Comprehensive textual and commentary archive for the Bhagavad Gītā.
          </li>
          <li>
            <strong>Bibek Debroy</strong> — <em>The Mahabharata</em>, unabridged English translation (Penguin India).
          </li>
        </ul>
        <p className="text-xs text-[#7E8279] pt-2">
          Historical narrative events are preserved faithfully from these editions. The contemporary scenarios are original hypotheticals created solely to explore analogous ethical tensions in modern life.
        </p>
      </section>

      {/* Closing Link */}
      <section className="border-t border-[#E5E0D5] pt-8">
        <button
          onClick={() => onNavigate('explore')}
          className="text-sm font-medium text-[#23483D] hover:underline inline-flex items-center gap-1.5"
        >
          <span>Explore the stories</span>
          <span aria-hidden="true">→</span>
        </button>
      </section>
    </article>
  );
};
