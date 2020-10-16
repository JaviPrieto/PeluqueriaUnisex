# Peluqueria Unisex
Proyecto para la asignatura de Infraestructura Virtual de 4º curso de Ingeniería Informática

## Descripción de funcionalidad

El microservicio solventará las citas de una peluquería unisex, asignando horas y fechas, tipos de pelado, tiempo empleado para cada uno y el precio.
Podrás pedir una cita online, viendo entre los días y las horas disponibles, indicando siempre en tu cita el pelado que te quieres hacer, el sistema calculará el tiempo a emplear para cada pelado y conforme calcula el tiempo se van cerrando horas del día asignado, dejando las horas libres disponibles para próximos clientes.

Datos empleados:
Fecha, Hora, Tipo de pelado, Tiempo empleado, Precio.

## Herramientas utilizadas

- Lenguaje : [Python](https://www.python.org)
- Base de datos : [MySQL-phpMyAdmin](https://www.phpmyadmin.net/)
- Servicio de logs : [LogRocket](https://logrocket.com/)

## Documentación adicional 

- [¿Por qué he usado estas herramientas?](./docs/herramientas.md)
- [¿Cómo he configurado git?](./docs/configuracion.md)

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
