function example(elemento) {
    console.log("elemento clickeado", elemento);
}
function turnOff(element) {
    element.innerText = "Off";
}
function hide(element) {
    element.remove();
    console.log("elemento eliminado", element);
}
