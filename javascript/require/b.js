var b = function(){
  console.log("b!");
  return {
    cnt: 0,
    hello: function(){
      console.log("hello");
      this.cnt += 1;
    }
  };
};

module.exports = new b();
