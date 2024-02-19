var rango = 32; // valor inicial del rango ASCII
var limite = 127; // valor final del rango ASCII
var salida = ""; // variable que almacena la salida
while (rango <= limite) { // bucle que recorre el rango
  salida += String.fromCharCode(rango); // concatena el carácter correspondiente
  salida += " "; // añade un espacio
  rango++; // incrementa el valor del rango
}
console.log(salida); // imprime la salida