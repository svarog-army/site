//webpack.config.js
const path = require('path');
const {merge} = require('webpack-merge');

const defaultConfig = {
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
      },
    ],
  },
};

const baseConfig = {
  entry: {
    main: './src/base.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/base.js', // <--- Will be compiled to this single file
  },
};
const cookieConfig = {
  entry: {
    main: './src/cookies.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/cookies.js', // <--- Will be compiled to this single file
  },
};

const recruitConfig = {
  entry: {
    main: './src/recruit.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/recruit.js', // <--- Will be compiled to this single file
  },
};

const adminConfig = {
  entry: {
    main: './src/admin.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/admin.js', // <--- Will be compiled to this single file
  },
};

const statsConfig = {
  entry: {
    main: './src/stats.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/stats.js', // <--- Will be compiled to this single file
  },
};

const landingConfig = {
  entry: {
    main: './src/landing.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/landing.js', // <--- Will be compiled to this single file
  },
};

const phoneFormattingConfig = {
  entry: {
    main: './src/phone-formatting.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/phone-formatting.js',
  },
};

const redirectConfig = {
  entry: {
    main: './src/redirect.ts',
  },
  output: {
    path: path.resolve(__dirname, './svarog/static'),
    filename: 'js/redirect.js',
  },
};

const configs = [
  baseConfig,
  recruitConfig,
  adminConfig,
  cookieConfig,
  landingConfig,
  phoneFormattingConfig,
  statsConfig,
  redirectConfig,
].map(conf => merge(defaultConfig, conf));

module.exports = configs;
