module.exports = {
  // mode: "production",
  mode: 'development',
  entry: './src/main.ts',
  module: {
    rules: [{
        test: /\.ts$/,
        use: 'ts-loader'
    }],
  },
  resolve: {
    extensions: [
      '.ts', '.js',
    ],
  },
};
