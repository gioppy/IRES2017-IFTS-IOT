var resistanceValue = 480;
var resistanceColors = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white'
];

//Converto il numero in stringa
var resistanceValueString = resistanceValue.toString();

//Mi salvo i valori dei primi due numeri come indice dell'array
var firstRing = resistanceValueString[0];
var secondRing = resistanceValueString[1];

//Calcolo il moltiplicatore, contando le cifre dopo i primi due valori
var multiplierArray = resistanceValueString.slice(2);
var multiplier = multiplierArray.length;

console.log(resistanceColors[firstRing]);
console.log(resistanceColors[secondRing]);
console.log(resistanceColors[multiplier]);
















