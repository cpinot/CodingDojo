function imprimirImpares() {
    console.log("Impares entre 0 y 20");
    for (let i = 0; i < 20; i++) {
        if (i % 2 !== 0) {
            console.log(i);
        }
    }
}
function disminuirMultiplosDe3() {
    console.log("Multiplos de 3 entre 100 y 0");
    for (let i = 100; i > 0; i--) {
        if (i % 3 === 0) {
            console.log(i);
        }
    }
}
function imprimeLaSecuencia() {
    console.log("Imprimir la Secuencia");
    var secuencia=1.5;
    var rest=4;
    while(true) {
        console.log(rest);
        rest-=secuencia;
        if(rest<=-4) {
            break;
        }
    }
}
function Sigma() {
    console.log("Sigma de 1 a 100");
    let sum = 0;
    for (let i = 0; i <=100; i++) {
        sum += i;
    }
    console.log(sum);
}
function factorial() {
    console.log("Factorial de 1 a 12");
    let product = 1;
    for (let i = 1; i <= 12; i++) {
        product *= i;
    }
    console.log(product);
}

imprimirImpares();
disminuirMultiplosDe3();
imprimeLaSecuencia();
Sigma();
factorial();
