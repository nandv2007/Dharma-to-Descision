import React from 'react';

interface FooterProps {
  onNavigate: (tab: string) => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigate }) => {
  return (
    <footer className="border-t border-[#E5E0D5] bg-[#F8F5ED] py-12 mt-auto">
      <div className="max-w-5xl mx-auto px-6 flex flex-col sm:flex-row items-baseline justify-between gap-6">
        <div>
          <span className="font-serif text-lg font-medium text-[#222421] block">
            Dharma to Decisions
          </span>
          <span className="text-xs text-[#5A5D56] font-serif italic mt-0.5 block">
            Ancient dilemmas. Modern choices.
          </span>
        </div>

        <nav className="flex items-center gap-6 text-xs text-[#5A5D56]">
          <button
            onClick={() => onNavigate('explore')}
            className="hover:text-[#222421] transition-colors"
          >
            Explore
          </button>
          <button
            onClick={() => onNavigate('gita')}
            className="hover:text-[#222421] transition-colors"
          >
            A Question for the Gita
          </button>
          <button
            onClick={() => onNavigate('about')}
            className="hover:text-[#222421] transition-colors"
          >
            About
          </button>
        </nav>
      </div>
    </footer>
  );
};
