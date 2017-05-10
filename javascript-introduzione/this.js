function a(){
  console.log(this);
}

var b = function(){
  console.log(this);
};

var c = {
  name: "Pippo",
  sayHi: function(){
    //THIS con variabile di ponte
    var self = this;
    var setName = function(name){
      self.name = name;
      console.log(this);
    };

    //THIS con bind()
    /*var setName = function(name){
      this.name = name;
      console.log(this);
    }.bind(this);*/

    //THIS con Fat Arrow Function - solo ES6
    //var setName = (name) => this.name = name;

    setTimeout(function(){
      this.name = "Paperino";
    }.bind(this), 1500);

    /*setTimeout(() => {
      this.name = "Paperino";
    }, 1500);*/

    setName("Pluto");

    console.log(this);
  }
};

a();
b();
c.sayHi();