function agregarLike(elemento)  {
    var likes = parseInt(elemento.innerText);
    likes++;
    elemento.innerText = likes +" Likes";
    alert("Ninja was liked");
}
function agregarHtml(elemento) {
    let contenedor = document.querySelector('".flex-2');
}
function eliminar(elemento) {
    elemento.remove();
}
function login(elemento) {
    elemento.innerText = "Logout";
}