function name(name){
  return function(lastName){
    console.log(name + ' ' + lastName);
  };
}

name("Pippo")("Pluto");

/*var person = name("Pippo");
person("Pluto");*/