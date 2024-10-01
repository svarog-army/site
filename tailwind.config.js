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
      screens: {
        desktop: '1440px',
      },
    },
  },
  plugins: [require('flowbite/plugin')],
};
