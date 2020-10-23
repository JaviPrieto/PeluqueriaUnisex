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

Los pasos a seguir para desplegar una aplicación de este tipo es:

- Crear las clases pertinentes, Cita.py, main.py, Hora.py
- Ver la relación que tienen unas clases con las otras.
- Escribir los métodos que normalmente utilizaremos para coger citas, modificar o eliminar.
- Automatizar todo el proceso, porque al cabo de un tiempo será todo igual.

## Herramientas utilizadas

- Lenguaje : [Python](https://www.python.org)
- Base de datos : [MySQL-phpMyAdmin](https://www.phpmyadmin.net/)
- Servicio de logs : [LogRocket](https://logrocket.com/)

## Documentación adicional 

- [¿Por qué he usado estas herramientas?](./docs/herramientas.md)
- [¿Cómo he configurado git?](./docs/configuracion.md)

## Historias de usuario

Estas son las historias de usuario abiertas hasta el momento:

- [ ] [HU1: Saber la hora de una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/2)
- [ ] [HU2: Saber el precio de un pelado](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/3)
- [ ] [HU3: Saber los datos de una cita](https://github.com/JaviPrieto/PeluqueriaUnisex/issues/6)

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
