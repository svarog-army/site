/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './svarog/templates/**/*.html',
    './src/js/**/*.js',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      maxWidth: {
        container: '1440px',
      },
      screens: {
        desktop: '1440px',
        'mobile-range': { min: '320px', max: '1439px' },
      },
    },
  },
  plugins: [require('flowbite/plugin'), require('tailwindcss-intersect')],
};
