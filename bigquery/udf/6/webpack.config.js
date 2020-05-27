var path = require('path');

module.exports = [
  {
    entry: './src/b.js',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'sample.js',
      library: "sample",
      libraryTarget: 'commonjs2',
    },
    mode: 'production',
  },
  {
    entry: './src/b.js',
    output: {
      path: path.resolve(__dirname, 'build'),
      filename: 'sample-var.js',
      library: "sample",
      libraryTarget: 'var',
    },
    mode: 'production',
  }
];
