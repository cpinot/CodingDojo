#atributos de clases

class Stack:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def imprime_info(self):
        print(f"Curso: {self.nombre}, Calificacion: {self.calificacion}")

class Estudiante:
    def __init__(self, nombre, apellido, id, stack):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.stack = stack
    
    def imprime_info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido},ID: {self.id})") 
        self.stack.imprime_info()

alex_python= Stack("Python", 9.4)
martha_java=Stack("Java", 8.7)
Roger_fundamentos=Stack("Fundamentos de la Web", 10)

alex=Estudiante("Alex", "Miller", 12345, alex_python)
martha=Estudiante("Martha", "Gonzalez", 62634, martha_java)
roger=Estudiante("Roger", "Infante", 82828, Roger_fundamentos)

alex.imprime_info()
martha.imprime_info()
roger.imprime_info()
