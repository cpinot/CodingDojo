var displayDiv = document.querySelector("#display");
displayDiv.innerText = 0;
function press(valor) {
    if (displayDiv.innerText == "0") {
        displayDiv.innerText = valor;
    } else {
        displayDiv.innerText += valor;
    }
}
function clr() {
    displayDiv.innerText = 0;
}
function setOP(op) {
    displayDiv.innerText += op;
}
function calculate() {

    var operacion = displayDiv.innerText;
    console.log(operacion);
    operacion = eval(operacion);
    console.log(operacion);
    displayDiv.innerText = operacion;
}
