function pizzaOven(tipoCorteza, tipoSalsa, quesos, salsas) {
    var pizza = {};
    pizza.tipoCorteza = tipoCorteza;
    pizza.tipoSalsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.salsas = salsas;
    return pizza;
}


var pizza1 = pizzaOven("Estilo Chicago", "Tradicional", ["mozzarela"],["peperoni", "salchicha"]);
console.log(pizza1);
var pizza2 = pizzaOven("lanzada a mano" , "marinara" , ["mozzarella", "feta"],["champiñones", "aceitunas", "cebollas"]);
console.log(pizza2);
var pizza3 = pizzaOven("Estilo Argentino", "Tradicional", ["mozzarela","cheddar"],["oregano", "pimenton", "cebolla caramelizada", "albahaca"]);
console.log(pizza3);
var pizza4 = pizzaOven("Pan Delgado", "Blanca", ["mozzarela", "ricotta"],["choclo","cebolla", "pimiento", "espinaca"]);
console.log(pizza4);
