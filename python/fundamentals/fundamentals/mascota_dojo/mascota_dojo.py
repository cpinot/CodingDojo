from mascota import Mascota, Perro, Gato
from ninja import Ninja


ninja1= Ninja("Javier", "Soriano", Perro("Croquetas","Perro","Salchicha"),"Helado", "Croquetas")
ninja1.alimentar().caminar().bañar()

mascota1 = Mascota("Kiara","Perro","Huesitos")
mascota1.comer().dormir().jugar().ruido()

ninja2= Ninja("Rosa", "Perez", Gato("Charly","Gato","Jurel"),"Helado", "racion de comida")
ninja2.alimentar().caminar().bañar()