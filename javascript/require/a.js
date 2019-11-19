var a = function(){
  return {
    a: 100,
    f: function(x){
      this.a = x;
    }
  };
};

module.exports = a;
