/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        paper: {
          DEFAULT: '#F8F5ED',
          warm: '#F4EFE4',
          card: '#FFFFFF',
          border: '#E5E0D5',
          line: '#DCD6C7',
        },
        ink: {
          DEFAULT: '#222421',
          light: '#5A5D56',
          muted: '#7E8279',
          faint: '#A6ABA0',
        },
        forest: {
          DEFAULT: '#23483D',
          dark: '#1A362E',
          light: '#2E5D4F',
          wash: 'rgba(35, 72, 61, 0.08)',
        },
        gold: {
          DEFAULT: '#B49A62',
          subtle: '#D8C69F',
        }
      },
      fontFamily: {
        serif: ['Newsreader', 'Georgia', 'Cambria', 'serif'],
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
