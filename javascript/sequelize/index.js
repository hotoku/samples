var Sequelize = require("sequelize");
var sequelize = new Sequelize("sample", "", "", {dialect: "sqlite", storage: "db.sqlite"});






const User = sequelize.define('user', {
    text1: {
        type: Sequelize.STRING
    }
});


User.sync({force: true}).then(() => {
  return User.create({
      text1: "hoge"
  });
});
