function a(){
  console.log("This is from a");
}

//Le funzioni sono oggetti!
a.name = "Pippo";

a();

var b = function(){
  console.log("This is from b");
};

b();

function printTextFromFunction(textFunction){
  textFunction();
}

printTextFromFunction(
  function(){
    console.log("This is from c");
  }
);

(function(text){
  console.log("This is from " + text);
})("IIFE");


var simpleNumber = 2;
console.log(typeof simpleNumber);

//MAI UTILIZZARE QUESTO!
var objectNumber = new Number(2);
console.log(typeof objectNumber);
console.log(objectNumber + 1);