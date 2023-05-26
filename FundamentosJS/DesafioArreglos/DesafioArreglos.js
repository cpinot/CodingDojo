function siempreHambriento(arr) {
    var siHayComida=false;
    var cont=0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]=="comida"){
            siHayComida=true;
            cont+=1;
        }
        else{
            siHayComida=false;
            
        }
    }
    if(siHayComida){
        for(var i=0;i<cont;i++){
        console.log("delicioso");
        }
    }
    else{
        console.log("Tengo hambre");
    }
}

function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i=0;i<arr.length;i++){
        if(arr[i]>cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

function betterThanAverage(arr) {
    var sum = 0;
    var promedio=0;
    // calcula el promedio
        for(var i=0;i<arr.length;i++){
            sum+=arr[i];
        }
        promedio=sum/arr.length;
    var count = 0

    // cuenta cuántas variables son mayores que el promedio
        for(var i=0;i<arr.length;i++){
            if(arr[i]>promedio){
                count+=1;
            }
        }
    return count;
}
function reverse(arr) {
    var temp=0;
    for(var i=0;i<arr.length/2;i++){
        temp=arr[i];
        arr[i]=arr[arr.length-1-i];
        arr[arr.length-1-i]=temp;
    }
    return arr;
}

function fibonacciArray(n) {
    // [0, 1] son los valores inciales del arreglos para calcular el resto
    var fibArr = [0, 1];
    while(fibArr.length < n) {
        var anterior = fibArr[fibArr.length - 1];
        var anterior2 = fibArr[fibArr.length - 2];
        fibArr.push(anterior + anterior2);
    }
    return fibArr;
}



console.log("--------------------------------------------------");
console.log(" valores de funcion siempreHambriento");
siempreHambriento([3.14, "comida", "pastel", true, "comida"]);
// esto debería mostrar "delicioso, "delicioso"
siempreHambriento([4, 1, 5, 7, 2]);
// esto debería mostrar "Tengo hambre"

console.log("--------------------------------------------------");  
console.log(" valores de funcion highPass");
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // esperamos de vuelta [6, 8, 10, 9]

console.log("--------------------------------------------------");
console.log(" valores de funcion betterThanAverage");
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result +" Valores son mayores que el promedio"); // esperamos 4 de vuelta

console.log("--------------------------------------------------");
console.log(" valores de funcion reverse");
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // esperamos de vuelta ["e", "d", "c", "b", "a"]

console.log("--------------------------------------------------");
console.log(" valores de funcion fibonacciArray");
var result = fibonacciArray(10);
console.log(result); // esperamos de vuelta[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]