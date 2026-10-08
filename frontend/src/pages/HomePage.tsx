import React from 'react';

interface HomePageProps {
  onNavigate: (tab: string, storyId?: string) => void;
}

export const HomePage: React.FC<HomePageProps> = ({ onNavigate }) => {
  const featured = [
    {
      id: 'arjuna-dilemma',
      character: 'ARJUNA',
      title: 'Duty and personal attachment',
      summary: 'Facing teachers, kin, and elders across the battleline, trapped between social obligation and familial affection.',
    },
    {
      id: 'vidura-counsel',
      character: 'VIDURA',
      title: 'The cost of speaking difficult truths',
      summary: 'Summoned by an anxious king who demands comfort, choosing whether to speak the unpalatable truth that could save the realm.',
    },
    {
      id: 'yudhishthira-yaksha',
      character: 'YUDHISHTHIRA',
      title: 'Restraint, fairness, and compassion',
      summary: 'Given the chance to revive only one fallen brother, choosing whether to favor his own kin or maintain equal justice across family lines.',
    },
  ];

  return (
    <div className="max-w-4xl mx-auto px-6 py-16 sm:py-24 space-y-24">
      {/* Hero Section */}
      <section className="space-y-6 pt-4">
        <span className="text-[11px] font-sans uppercase tracking-[0.2em] text-[#5A5D56] font-medium block">
          Ancient Dilemmas
        </span>
        <h1 className="font-serif text-4xl sm:text-6xl text-[#222421] font-normal leading-[1.15] max-w-2xl">
          What would you do?
        </h1>
        <p className="text-base sm:text-lg text-[#5A5D56] leading-relaxed max-w-xl font-sans">
          The Mahabharata is filled with difficult choices—between duty and affection, loyalty and justice, truth and consequence.
          <br className="hidden sm:inline" /> Explore those choices for yourself.
        </p>
        <div className="pt-2">
          <button
            onClick={() => onNavigate('explore')}
            className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors inline-flex items-center gap-2"
          >
            <span>Explore the dilemmas</span>
            <span aria-hidden="true">→</span>
          </button>
        </div>
      </section>

      {/* Editorial Introduction */}
      <section className="border-t border-[#E5E0D5] pt-16 space-y-4 max-w-2xl">
        <h2 className="font-serif text-2xl sm:text-3xl text-[#222421] font-normal">
          Some choices have no easy answer.
        </h2>
        <p className="text-[#5A5D56] text-base leading-relaxed">
          In the Mahabharata, people rarely face a simple division between good and evil. Instead, they are caught between competing responsibilities—to their families, their mentors, their vows, and the wider world.
        </p>
      </section>

      {/* Featured Stories */}
      <section className="border-t border-[#E5E0D5] pt-16 space-y-8">
        <div className="flex items-baseline justify-between">
          <span className="text-xs uppercase tracking-[0.15em] text-[#5A5D56] font-medium">
            Selected Moments
          </span>
          <button
            onClick={() => onNavigate('explore')}
            className="text-xs text-[#23483D] hover:underline font-medium"
          >
            View all six stories →
          </button>
        </div>

        <div className="divide-y divide-[#E5E0D5]">
          {featured.map((item) => (
            <div
              key={item.id}
              className="py-8 first:pt-0 last:pb-0 flex flex-col sm:flex-row sm:items-baseline justify-between gap-4 group"
            >
              <div className="max-w-xl space-y-2">
                <span className="text-xs font-sans uppercase tracking-wider text-[#5A5D56]">
                  {item.character}
                </span>
                <h3 className="font-serif text-xl sm:text-2xl text-[#222421] font-normal group-hover:text-[#23483D] transition-colors">
                  {item.title}
                </h3>
                <p className="text-sm text-[#5A5D56] leading-relaxed">
                  {item.summary}
                </p>
              </div>
              <button
                onClick={() => onNavigate('story', item.id)}
                className="text-sm font-medium text-[#23483D] hover:text-[#1A362E] whitespace-nowrap self-start sm:self-auto pt-2 sm:pt-0"
              >
                Read the story →
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* Have a question of your own? */}
      <section className="border-t border-[#E5E0D5] pt-14 pb-2">
        <div className="bg-white/60 border border-[#E5E0D5] rounded-2xl p-8 sm:p-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div className="max-w-xl space-y-2">
            <span className="text-xs uppercase tracking-wider text-[#B49A62] font-semibold block">
              Personal Reflection
            </span>
            <h2 className="font-serif text-2xl sm:text-3xl text-[#222421] font-normal">
              Have a question of your own?
            </h2>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              Not every dilemma comes from an ancient story. Bring something you&apos;re facing today and explore a perspective from the Bhagavad Gita.
            </p>
          </div>
          <button
            onClick={() => onNavigate('gita')}
            className="px-5 py-2.5 text-xs font-medium uppercase tracking-wider text-[#23483D] border border-[#23483D]/30 hover:bg-[#23483D] hover:text-white rounded-lg transition-colors whitespace-nowrap self-start sm:self-auto"
          >
            A Question for the Gita →
          </button>
        </div>
      </section>

      {/* How it works */}
      <section className="border-t border-[#E5E0D5] pt-16 space-y-8">
        <span className="text-xs uppercase tracking-[0.15em] text-[#5A5D56] font-medium block">
          How It Works
        </span>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-8">
          <div className="space-y-2">
            <span className="font-serif text-lg text-[#23483D] block font-medium">
              01 Read
            </span>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              Understand the situation and why the choice is difficult.
            </p>
          </div>
          <div className="space-y-2">
            <span className="font-serif text-lg text-[#23483D] block font-medium">
              02 Choose
            </span>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              Make the decision you would make, with no labels telling you what is right.
            </p>
          </div>
          <div className="space-y-2">
            <span className="font-serif text-lg text-[#23483D] block font-medium">
              03 Reflect
            </span>
            <p className="text-sm text-[#5A5D56] leading-relaxed">
              See the consequences, learn what happened in the epic, and consider a modern echo.
            </p>
          </div>
        </div>
      </section>

      {/* Closing CTA */}
      <section className="border-t border-[#E5E0D5] pt-16 text-center space-y-4">
        <h2 className="font-serif text-2xl sm:text-3xl text-[#222421] font-normal">
          Begin with a dilemma.
        </h2>
        <p className="text-sm text-[#5A5D56] max-w-md mx-auto">
          Start with Arjuna on the battlefield of Kurukshetra, or choose any of the six stories in the archive.
        </p>
        <div className="pt-2">
          <button
            onClick={() => onNavigate('story', 'arjuna-dilemma')}
            className="px-6 py-3 text-sm font-medium text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors"
          >
            Begin with Arjuna&apos;s choice →
          </button>
        </div>
      </section>
    </div>
  );
};
