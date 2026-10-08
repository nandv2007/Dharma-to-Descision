import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { HomePage } from './pages/HomePage';
import { ExplorePage } from './pages/ExplorePage';
import { StoryPage } from './pages/StoryPage';
import { DecisionFlow } from './pages/DecisionFlow';
import { AboutPage } from './pages/AboutPage';
import { GitaQuestionPage } from './pages/GitaQuestionPage';

export function App() {
  const [currentTab, setCurrentTab] = useState<string>('home');
  const [activeStoryId, setActiveStoryId] = useState<string>('arjuna-dilemma');

  // Sync hash routing so refresh and links work seamlessly
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash.replace('#', '');
      if (hash.startsWith('story/')) {
        const id = hash.replace('story/', '');
        setActiveStoryId(id);
        setCurrentTab('story');
      } else if (hash.startsWith('decide/')) {
        const id = hash.replace('decide/', '');
        setActiveStoryId(id);
        setCurrentTab('decide');
      } else if (['home', 'explore', 'about', 'gita', 'question'].includes(hash)) {
        setCurrentTab(hash === 'question' ? 'gita' : hash);
      } else if (!hash) {
        setCurrentTab('home');
      }
    };

    handleHashChange();
    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  const handleNavigate = (tab: string, storyId?: string) => {
    if (storyId) {
      setActiveStoryId(storyId);
      if (tab === 'story') {
        window.location.hash = `story/${storyId}`;
      } else if (tab === 'decide') {
        window.location.hash = `decide/${storyId}`;
      }
    } else {
      window.location.hash = tab === 'home' ? '' : tab;
    }
    setCurrentTab(tab);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#F8F5ED] text-[#222421]">
      {/* Editorial Navigation */}
      <Navbar currentTab={currentTab} onNavigate={handleNavigate} />

      {/* Main Reading / Decision Experience */}
      <main className="flex-1">
        {currentTab === 'home' && (
          <HomePage onNavigate={handleNavigate} />
        )}

        {currentTab === 'explore' && (
          <ExplorePage
            onSelectStory={(id) => handleNavigate('story', id)}
          />
        )}

        {currentTab === 'story' && (
          <StoryPage
            storyId={activeStoryId}
            onBack={() => handleNavigate('explore')}
            onStartDecision={(id) => handleNavigate('decide', id)}
          />
        )}

        {currentTab === 'decide' && (
          <DecisionFlow
            storyId={activeStoryId}
            onExit={() => handleNavigate('story', activeStoryId)}
            onExploreOther={() => handleNavigate('explore')}
          />
        )}

        {currentTab === 'about' && (
          <AboutPage onNavigate={handleNavigate} />
        )}

        {currentTab === 'gita' && (
          <GitaQuestionPage />
        )}
      </main>

      {/* Clean Footer */}
      <Footer onNavigate={handleNavigate} />
    </div>
  );
}

export default App;
