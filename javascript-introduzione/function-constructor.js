function Person(){
  this.firstname = "Pippo";
  this.lastname = "Pluto";
}

Person.prototype.sayHi = function(){
  return "Hi " + this.firstname;
};

var pippo = new Person();
console.log(typeof pippo);
console.log(pippo);
console.log(pippo.sayHi());

var pluto = new Person();


Array.prototype.getFirst = function(){
  return this[0];
};

var arr = [1,2,3];
var arr2 = ["pippo", 3, 4];
console.log(arr.getFirst());
console.log(arr2.getFirst());












