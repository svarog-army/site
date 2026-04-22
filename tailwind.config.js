export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      maxWidth: { container: '1440px' },
      screens: {
        desktop: '1440px',
        'mobile-range': { min: '320px', max: '1439px' },
      },
      fontFamily: {
        ethnocentric: ['Ethnocentric Regular', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
