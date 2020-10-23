# -*- coding: utf-8 -*-

class Cita:
    # Define una cita en base a la fecha, hora, pelado, tiempo empleado y precio

    def __init__(self,id,fecha,hora,pelado,tiempo,precio):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.pelado = pelado
        self.tiempo = tiempo
        self.precio = precio 
        
    #HU3: Saber los datos de una cita
    def resumenCita(self):
        """Imprime datos de la cita por pantalla."""
        print("######### DETALLES DE SU CITA ###############")
        print("ID: " + self.id)
        print("Fecha: " + self.fecha)
        print("Hora: " + self.hora)
        print("Tipo de pelado: " + self.pelado)
        print("Tiempo empleado: " + self.tiempo + " min")
        print("Precio: " + self.precio + " euros")        
        print("#############################################")

    #HU4: Como usuario quiero coger una cita
    def cogerCita(self,fecha,hora,pelado):
        self.fecha = fecha
        self.hora = hora 
        self.pelado = pelado 

        if (pelado == "corte hombre"):
            self.tiempo = "15"
            self.precio = "8"
        
        elif (pelado == "corte barba"):
            self.tiempo = "10"
            self.precio = "5"
        
        elif (pelado == "corte mujer"):
            self.tiempo = "30"
            self.precio = "12"

        else:
            self.tiempo = "15"
            self.precio = "10"

    
    #HU5: Como usuario quiero modificar la fecha y hora de la cita
    def modificarCita(self,fecha,hora):
        self.fecha = fecha
        self.hora = hora
        

    ###################################################################################

    def getID(self):
        return self.id

    ###################################################################################

    def getFecha(self):
        return self.fecha

    ###################################################################################
    #HU1 : Saber la hora de una cita
    def getHora(self):
        return self.hora  

    ###################################################################################

    def getPelado(self):
        return self.pelado

    ###################################################################################

    def getTiempo(self):
        return self.tiempo

    ###################################################################################
    #HU2 : Saber el precio de un pelado
    def getPrecio(self):
        return self.precio

    ###################################################################################
