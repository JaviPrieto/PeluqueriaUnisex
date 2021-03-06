FROM python:3

# Establecer directorio 
WORKDIR app/src/

# Copiar contenido
COPY . .

# Instalar requerimientos encesarios
RUN pip install --no-cache-dir -r requirements.txt

# Asignamos el puerto 80 al contenedor
EXPOSE 80

# Lanzamos la aplicación
CMD [ "python", "./app/src/main.py" ]
