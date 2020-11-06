## Docker :whale2:

### Justificacion del contenedor base
Como utilizo [Python]((https://www.python.org/)) en mi proyecto, he consultado las imágenes oficiales de Python en [DockerHub](https://hub.docker.com/_/python), tenemos cuatro opciones a la hora de elegir una imagen oficial de Python:

**python:<version>** : Esta es la imagen de facto. Si no está seguro de cuáles son sus necesidades, probablemente desee utilizar este. Está diseñado para usarse tanto como un contenedor desechable (monte su código fuente e inicie el contenedor para iniciar su aplicación), así como la base para construir otras imágenes.

Algunas de estas etiquetas pueden tener nombres como buster o stretch en ellas. Estos son los nombres de código de la suite para las versiones de Debian e indican en qué versión se basa la imagen. Si su imagen necesita instalar paquetes adicionales más allá de lo que viene con la imagen, es probable que desee especificar uno de estos explícitamente para minimizar las roturas cuando haya nuevas versiones de Debian.

Esta etiqueta se basa en buildpack-deps. buildpack-deps está diseñado para el usuario medio de Docker que tiene muchas imágenes en su sistema. Por diseño, tiene una gran cantidad de paquetes Debian extremadamente comunes. Esto reduce la cantidad de paquetes que las imágenes que se derivan de él necesitan instalar, reduciendo así el tamaño total de todas las imágenes en su sistema.

**python:<version>-slim**: Esta imagen no contiene los paquetes comunes contenidos en la etiqueta predeterminada y solo contiene los paquetes mínimos necesarios para ejecutar Python. A menos que esté trabajando en un entorno donde solo se implementará la imagen de Python y tiene limitaciones de espacio, le recomendamos que utilice la imagen predeterminada de este repositorio.

**python:<version>-alpine** : Esta imagen está basada en el popular proyecto Alpine Linux, disponible en la imagen oficial de Alpine. Alpine Linux es mucho más pequeño que la mayoría de las imágenes base de distribución (~ 5 MB) y, por lo tanto, genera imágenes mucho más delgadas en general.

Esta variante es muy recomendable cuando se desea que el tamaño final de la imagen sea lo más pequeño posible. La principal advertencia a tener en cuenta es que utiliza musl libc en lugar de glibc y amigos, por lo que cierto software puede tener problemas dependiendo de la profundidad de sus requisitos de libc. Sin embargo, la mayoría del software no tiene problemas con esto, por lo que esta variante suele ser una opción muy segura. Consulte este hilo de comentarios de Hacker News para obtener más información sobre los problemas que podrían surgir y algunas comparaciones a favor y en contra del uso de imágenes basadas en Alpine.

Para minimizar el tamaño de la imagen, es poco común que se incluyan herramientas adicionales relacionadas (como git o bash) en las imágenes basadas en Alpine. Usando esta imagen como base, agregue las cosas que necesita en su propio Dockerfile (vea la descripción de la imagen de alpine para ver ejemplos de cómo instalar paquetes si no está familiarizado).

**python:<version>-windowsservercore** : Esta imagen se basa en Windows Server Core (microsoft / windowsservercore). Como tal, solo funciona en lugares donde esa imagen lo hace, como Windows 10 Professional / Enterprise (Anniversary Edition) o Windows Server 2016.

## Pruebas

| Imagen Usada | Tiempo de Usuario | Tiempo del Sistema | Porcentaje de CPU | Tamaño |
| -- | -- | -- | -- | -- |
| python| 0.3s | 0.02s | 1% | 1.169GB |
| python-alpine| 0.3s | 0.03s | 1% | 341.7MB |
| python-slim| 0.3s | 0.03s | 1% | 407.2MB |

Atendiendo a los datos extraídos de las distintas ejecuciones, y las buenas prácticas anteriormente mencionadas, la imagen base que usaremos será python-alpine, aparte de por tener el menor tamaño, porque la diferencia de tiempo con python tampoco es grande.



