var addBtns = document.querySelectorAll(".add");
var removeBtns = document.querySelectorAll(".remove");
console.log(addBtns);

var amigos = document.querySelector("#amigos");
var solicitudes = document.querySelector("#solicitudes");

//Remover elementos en botones de +
function aceptarSolicitud(element){
    let elementoRemover = element.parentElement.parentElement;
    elementoRemover.remove();
    let numSolicitudes = parseInt(solicitudes.innerHTML);
    let numAmigos = parseInt(amigos.innerHTML);
    solicitudes.innerHTML = numSolicitudes - 1;
    amigos.innerHTML = numAmigos + 1;
    
}
function removeElement(element){
    let elementoRemover = element.parentElement.parentElement;
    elementoRemover.remove();
    let numSolicitudes = parseInt(solicitudes.innerHTML);
    let numAmigos = parseInt(amigos.innerHTML);
    solicitudes.innerHTML = numSolicitudes - 1;
    }


function editProfile(){
    let cardName=document.querySelector(".cardName");
    console.log(cardName);
    cardName.innerText="Cynthia Pino";
}