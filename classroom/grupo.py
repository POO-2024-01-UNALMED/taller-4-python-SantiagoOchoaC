from classroom.asignatura import Asignatura
class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None): #
        if (asignaturas == None): # Agregamos esto debido a que python solo crea una lista por función. 
            asignaturas = []
        if (estudiantes == None):
            estudiantes = []
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes # Atributos privados

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None): # Reemplazamos el Objeto Mutable vacio
        if (lista == None):
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self): # Utilizamos el método especial __str__ 
        salida = "Grupo de estudiantes:" +" "+ self._grupo 
        return salida

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod # Metodo innecesario
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre 