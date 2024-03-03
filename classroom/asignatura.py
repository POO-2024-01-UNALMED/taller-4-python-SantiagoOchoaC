class Asignatura:

    def __init__(self, nombre = None, salon = "remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self): # Utilizamos el metodo especial __str__ para modificar la salida al imprimir un objeto
        salida = self._nombre +" "+ self._salon # llamamos el atributo del objeto
        return salida 
