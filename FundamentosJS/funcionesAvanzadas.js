// Objetivo: Repasar las funciones avanzadas de JS
//funcion tipo flecha

const suma =(num1,num2) => num1 + num2;
const imprimiendoHola = nombre => console.log(`Hola ${nombre}`);

let resultado = suma(10,20);
console.log(resultado);
imprimiendoHola("Juan");


//forEach
const arreglo = ['Alex','Martha','Roger','Luis'];
for(let i=0;i<arreglo.length;i++){
    console.log(arreglo[i]);
}

arreglo.forEach(function(n)) ;
