/*
DATA TYPES:
undefined -> not defined yet
null -> nothing (not undefined)
boolean -> True of False
string -> it is a string :D
symbol -> immutable and unique
number -> is a number :D
objetct -> everything ?
*/


//HOW TO DECLARE A VARIABLE

//(1)
var nameOfVariable = "Bea"; //-> my var is a string
nameOfVariable = 8; //-> now it is a number
//-> var will be usable everywhere in the code

//(2)
let otherName = "salut";
//-> let will be usable in the scope where it was defined

//(3)
const pi = 3.14;
//-> constante qui change jamais

//DECLARING VS ASSIGNING

var a; //-> declaring a variable
console.log("a not assigned yet : ", a);
var b = 2; //-> declaring and assigning a variable + giving it a value -> "=" is the assigning parameter
a = 7; //-> now assigning the variable a tu value 7 - a was already declared
b = a; //-> we can also reasign a variable that was assigned before
console.log("a is now assigned : ", a);

//to declare without assgning = unitialized variables

//operations are normal (+,-,*,/,%)
//incrementing: myVar = myVar +1; || myVar++; || myVar += 1; -> this is true for every operation (not %)
//my decimal is with a dote
var myDecimal = 3.1;

// \ -> escape symbol for quotes -> \' - \" - \\ - \n - \r - \b - \f
var myStr = "I am string \" still a string\" with quotes inside";

// taille d un string
var myStr = "salut";
var tailleMyStr = myStr.length; //taille du string, sans paranthèses
var firstLetter = myStr[0]; // premiere lettre de mySrs
// var lastLettre = myStr[-1] -> DOESNT WORK

//arrays
var array = [1,2]; // [] like python, elements can be different data types
var nesteArray = [[1,2],[3,4]];
//index like python
array.push(3); // adds 3 to the end of the array
array.unshift(3); // adds 3 to the begining of the array
a = array.pop(); // a is the last value of the array, and array loses last value
b = array.shift(); // same as pop, but first value

//functions
function thisIsFunction(a, b){//arguments
    console.log(a-b);
}
thisIsFunction(10, 5); // appel