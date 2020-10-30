[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Peluqueria Unisex
Proyecto para la asignatura de Infraestructura Virtual de 4º curso de Ingeniería Informática

## Descripción de funcionalidad

El microservicio solventará las citas de una peluquería unisex, asignando horas y fechas, tipos de pelado, tiempo empleado para cada uno y el precio.
Podrás pedir una cita online, viendo entre los días y las horas disponibles, indicando siempre en tu cita el pelado que te quieres hacer, el sistema calculará el tiempo a emplear para cada pelado y conforme calcula el tiempo se van cerrando horas del día asignado, dejando las horas libres disponibles para próximos clientes.

Datos empleados:
Fecha, Hora, Tipo de pelado, Tiempo empleado, Precio.

## Interés de la aplicación

He decidido hacer el proyecto sobre una peluquería porque mi prima tiene una, y hace tiempo me dijo que si yo le podía hacer un software para ella guardar ahí todo lo relacionado con los clientes y las citas, el caso es que no lo estoy haciendo por ella pero sí por saber si soy capaz de desarrollar algo por el estilo.

Los pasos a seguir para desplegar la aplicación son:

- [Pasos a seguir](./docs/pasos.md)

## Herramientas utilizadas

- Lenguaje : [Python](https://www.python.org)
- Base de datos : [MySQL-phpMyAdmin](https://www.phpmyadmin.net/)
- Servicio de logs : [LogRocket](https://logrocket.com/)

## Herramientas de construcción utilizadas

Justificación del uso de las herramientas de construcción:

**make** es una utilidad disponible en Linux que agiliza la tarea de compilar código desde la terminal. Nos evita tener que escribir los comandos de compilación a mano, que suelen ser muy largos, y en cambio nos permite escribir algo mucho más corto que al final hace lo mismo. Además, make puede hacer muchas otras cosas que harán que preparar las prácticas para enviarlas sea coser y cantar. 

He utilizado un archivo makefile que ejecuta las funciones **main.py** y **test.py** dependiendo como llames a make, make nos ayuda a compilar nuestros programas. Presenta muchas ventajas para programas grandes, en los que hay muchos ficheros repartidos por varios directorios. Principalmente aporta dos ventajas: 

- *Es capaz de saber qué cosas hay que recompilar*. Si cuando estamos depurando nuestro programa tocamos un fichero fuente, al compilar con make sólo se recompilaran aquellos ficheros que dependan del que hemos tocado. Si compilamos a mano con el compilador que sea, o tenemos en la cabeza esas dependencias para compilar sólo lo que hace falta, o lo compilamos todo. Si el proyecto es grande, se nos olvidará alguna dependencia o nos pasaremos horas compilando.

- *Nos guarda los comandos de compilación con todos sus parámetros para encontrar librerías, etc*. No tendremos que escribir largas líneas de compilación con montones de opciones que debemos saber de memoria o, al menos, sólo tendremos que hacerlo una vez

## Documentación adicional 

- [¿Por qué he usado estas herramientas?](./docs/herramientas.md)
- [¿Cómo he configurado git?](./docs/configuracion.md)

## Historias de usuario

Estas son las historias de usuario abiertas hasta el momento:

- [ ] [HU1: Saber la hora de una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/2)
- [ ] [HU2: Saber el precio de un pelado](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/3)
- [ ] [HU3: Saber los datos de una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/6)
- [ ] [HU4: Como usuario quiero coger una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/14)
- [ ] [HU5: Como usuario quiero modificar una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/15)


Explicación de las historias de usuario y milestones 

- [HU y milestones](./docs/hu-milestones.md)

## Comandos

### Ejecución de la función main

Esto ejecuta el archivo main.py que contiene la función main de la app en la que se muestran los datos de una cita de un cliente.

```bash
make main
```

### Ejecución de los tests

El proyecto utiliza para la ejecución de los tests [pytest](https://docs.pytest.org/en/stable/).

```bash
make test
```

## Autor

[Javier Prieto](https://github.com/JaviPrieto) 
