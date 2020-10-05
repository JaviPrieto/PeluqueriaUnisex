class Cita:

    def __init__(self, fecha,hora,pelado,tiempo,precio):
        self.fecha = fecha
        self.hora = hora
        self.pelado = pelado
        self.tiempo = tiempo
        self.precio = precio

    def resumenCita(self):
        """Imprime datos de la cita por pantalla."""
        print("Fecha: " + self.fecha)
        print("Hora: " + self.hora)
        print("Tipo de pelado: " + self.pelado)
        print("Tiempo empleado: " + self.tiempo + "min")
        print("Precio: " + self.precio + "euros")

       


cita = Cita("16","12:00","corte pelo","15","10") 
cita.resumenCita()
