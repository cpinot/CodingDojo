var likesNumber =[9, 12, 9];
var boton = [
    document.querySelector("#btn-0"),
    document.querySelector("#btn-1"),
    document.querySelector("#btn-2")
];

function like(id) {
    console.log(id);
    likesNumber[id]++;
    boton[id].innerHTML = likesNumber[id] + " like(s)";
}