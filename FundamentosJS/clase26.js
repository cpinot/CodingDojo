var addBtns = document.querySelectorAll(".add");
var removeBtns = document.querySelectorAll(".remove");
console.log(addBtns);

var amigos = document.querySelector("#amigos");
var solicitudes = document.querySelector("#solicitudes");

//Remover elementos en botones de +
for (index = 0; index < addBtns.length; index++) {
    console.log(addBtns[index]);
    let element = addBtns[index];
    element.addEventListener("click", () => {
        let elementoRemover = element.parentElement.parentElement;
        elementoRemover.remove();
        let numSolicitudes = parseInt(solicitudes.innerHTML);
        let numAmigos = parseInt(amigos.innerHTML);
        solicitudes.innerHTML = numSolicitudes - 1;
        amigos.innerHTML = numAmigos + 1;
    })
}

//Remover elementos en botones de -
for (index = 0; index < removeBtns.length; index++) {
    console.log(removeBtns[index]);
    let element = removeBtns[index];
    element.addEventListener("click", () => {
        let elementoRemover = element.parentElement.parentElement;
        elementoRemover.remove();
        let numSolicitudes = parseInt(solicitudes.innerHTML);
        solicitudes.innerHTML = numSolicitudes - 1;
    })
}


function cambiarNombre() {
    let elementoNombre = document.getElementById("nombre");
    console.log(elementoNombre.innerHTML);
    elementoNombre.innerHTML = "Ing. Nestor Ribero ";
}