function b(){
  console.log(num);
}

function a(){
  var num = 2;
  b();
}

var num = 1;
a();