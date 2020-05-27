var path = require('path');

module.exports = {
  entry: './src/b.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'sample.js',
    library: "sample",
    libraryTarget: 'var',
  },
  mode: 'production',
};


/*
  output: libraryの意味
  https://qiita.com/jkr_2255/items/283bc12dd07bc237179e
  - var（デフォルト）…output.libraryで指定した変数を宣言して、そこに代入する
  - this・window・global…それぞれ指定したオブジェクトの、output.library名のプロパティとして代入する
  - commonjs…exports[output.library]に代入する
  - commonjs2…module.exportsに代入する（output.libraryは影響しない）
  - amd…define()で登録する
  - umd…exports、module.exports、define()、thisのどれかを使う
*/
