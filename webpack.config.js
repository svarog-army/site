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

const configs = [baseConfig, recruitConfig, adminConfig, cookieConfig].map(conf =>
  merge(defaultConfig, conf),
);

module.exports = configs;
