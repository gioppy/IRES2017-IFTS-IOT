var person = {
  firstname: 'Default name',
  sayHi: function() {
    return "Hi " + this.firstname;
  },
  sayHello: function(){
    return "Hello " + this.firstname + ' ' + this.lastname;
  }
};

var pippo = {
  firstname: 'Pippo',
  lastname: 'Pluto'
};

pippo.__proto__ = person;
console.log(pippo.sayHi());
console.log(pippo.sayHello());

var paperino = {
  firstname: "Paperino"
};

paperino.__proto__ = person;
console.log(paperino.sayHi());