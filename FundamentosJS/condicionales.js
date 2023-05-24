let pais="USA";
let edad=21;

if(pais==="USA"){
    if(edad>=21){
        console.log("Ya eres mayor de edad en "+ pais);
    }
    else{
        let num=21-edad;
        console.log("Te faltan "+num+" años para ser mayor de edad en "+ pais);
    }
}
else{
    if(edad>=18){
        console.log("Ya eres mayor de edad en "+ pais);
    }
    else{
        num=18-edad;
        console.log("Te faltan "+num+" años para ser mayor de edad en "+ pais);
    }
}