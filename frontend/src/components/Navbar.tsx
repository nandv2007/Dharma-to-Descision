import React, { useState } from 'react';
import { Menu, X } from 'lucide-react';

interface NavbarProps {
  currentTab: string;
  onNavigate: (tab: string, storyId?: string) => void;
}

export const Navbar: React.FC<NavbarProps> = ({ currentTab, onNavigate }) => {
  const [menuOpen, setMenuOpen] = useState(false);

  const handleLink = (tab: string, storyId?: string) => {
    onNavigate(tab, storyId);
    setMenuOpen(false);
  };

  return (
    <header className="border-b border-[#E5E0D5] bg-[#F8F5ED]/95 sticky top-0 z-40 backdrop-blur-sm">
      <div className="max-w-5xl mx-auto px-6 h-16 sm:h-20 flex items-center justify-between">
        {/* Brand / Logo */}
        <button
          onClick={() => handleLink('home')}
          className="text-left group flex items-baseline gap-2.5"
        >
          <span className="font-serif text-xl sm:text-2xl font-semibold tracking-tight text-[#222421] group-hover:text-[#23483D] transition-colors">
            Dharma to Decisions
          </span>
        </button>

        {/* Desktop Navigation */}
        <nav className="hidden sm:flex items-center gap-8 text-sm">
          <button
            onClick={() => handleLink('explore')}
            className={`transition-colors ${
              currentTab === 'explore'
                ? 'text-[#23483D] font-medium'
                : 'text-[#5A5D56] hover:text-[#222421]'
            }`}
          >
            Explore
          </button>
          <button
            onClick={() => handleLink('gita')}
            className={`transition-colors ${
              currentTab === 'gita'
                ? 'text-[#23483D] font-medium'
                : 'text-[#5A5D56] hover:text-[#222421]'
            }`}
          >
            A Question for the Gita
          </button>
          <button
            onClick={() => handleLink('about')}
            className={`transition-colors ${
              currentTab === 'about'
                ? 'text-[#23483D] font-medium'
                : 'text-[#5A5D56] hover:text-[#222421]'
            }`}
          >
            About
          </button>
          <button
            onClick={() => handleLink('explore')}
            className="px-4 py-2 text-xs font-medium uppercase tracking-wider text-white bg-[#23483D] hover:bg-[#1A362E] rounded transition-colors"
          >
            Explore the dilemmas
          </button>
        </nav>

        {/* Mobile Menu Button */}
        <div className="sm:hidden flex items-center">
          <button
            onClick={() => setMenuOpen(!menuOpen)}
            className="p-2 text-[#222421] hover:text-[#23483D]"
            aria-label="Toggle menu"
          >
            {menuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {menuOpen && (
        <div className="sm:hidden border-b border-[#E5E0D5] bg-[#F8F5ED] px-6 py-4 space-y-3 text-sm">
          <button
            onClick={() => handleLink('explore')}
            className="block w-full text-left py-2 text-[#222421]"
          >
            Explore the dilemmas
          </button>
          <button
            onClick={() => handleLink('gita')}
            className="block w-full text-left py-2 text-[#23483D] font-medium"
          >
            A Question for the Gita
          </button>
          <button
            onClick={() => handleLink('about')}
            className="block w-full text-left py-2 text-[#5A5D56]"
          >
            About
          </button>
        </div>
      )}
    </header>
  );
};
