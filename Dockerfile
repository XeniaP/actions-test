# Utiliza una imagen base de Nginx
FROM nginx:latest

# Etiqueta para indicar al creador de la imagen
LABEL maintainer="tumarulog@gmail.com"

# Copia archivos locales al sistema de archivos de la imagen
#COPY index.html /usr/share/nginx/html/
COPY index.html /home/ubuntu/actions-test

# Puerto en el que escuchará el servidor Nginx
EXPOSE 80

# Comando que se ejecutará cuando se inicie un contenedor basado en esta imagen
CMD ["nginx", "-g", "daemon off;"]
