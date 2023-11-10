Agenda de contactos

- Permite crer un usuario de la agenda y crear contactos relacionados a ese usuario
- Un usuario solo va a poder tener acceso (crear, modificar, ver y eliminar) a sus propios contactos
- Datos del contacto: primer_nombre, segundo_nombre, email, telefono_casa, movil

endpoints:
    POST /api/users/ -> crear un nuevo usuario
    POST /api/token/ -> crea los tokens de acceso y de actualizacion
    POST /api/token/refresh/ -> actualiza un token

    GET       /api/contacts/ -> consultar todos los contactos DEL USUARIO
    POST      /api/contacts/ -> crea un nuevo contacto
    GET       /api/contacts/:pk -> muestra los detalles de un contacto
    PATCH/PUT /api/contacts/:pk -> modifica un contacto
    DELETE    /api/contacts/:pk -> elimina un contacto

# Instructions

1. Install django and django rest_framework
2. Install getenv
3. Install postgres and run postgresql. Also create your database
4. On settings.py change the DATABASE and the authentication methods, also delete the templates
5. Change the directory name for the main project files to `config`
6. Change all the references to the old directory name
7. Create a new app. A good name can be service, api, or app
8. Add a models file to the new app and include the new entities of the project
9. Create the serializers for each model you want to expose on your endpoints. Including the creation of users so you app can be accessible
10. Create the viewsets for your serializers so you can use them on your urls
11. Create your urls in the urls.py file and include your new routes
12. On here you'll also need to include the JWT package views
13. Include these views on your main urls file
14. If you forgot to change your settings to include the new jwt authentication methods as the default authentication method, you should do it now
15. Make and run migrations
16. Test in postman
16.1 Tweak if neccessary
17. Create the api so you can "auto create the migrations"
