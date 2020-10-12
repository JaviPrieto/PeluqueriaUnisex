# -*- coding: utf-8 -*-

class Cita:
    # Define una cita en base a la fecha, hora, pelado, tiempo empleado y precio

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

    ###################################################################################

    def getFecha(self):
        return self.fecha

    ###################################################################################

    def getHora(self):
        return self.hora

    ###################################################################################

    def getPelado(self):
        return self.pelado

    ###################################################################################

    def getTiempo(self):
        return self.tiempo

    ###################################################################################

    def getPrecio(self):
        return self.precio

    ###################################################################################
