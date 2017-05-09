function concatenate(name, ...strings){
  console.log(name + ' ' + strings.join('-'));
}

concatenate("Pippo", 1,2,3);
concatenate("Pluto", "Lorem", "Ipsum",1,2,3,4);