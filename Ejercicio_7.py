# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask
from flask import abort # Importación de la función abort para abortar la solicitud

app = Flask(__name__) # Creación de la instancia de la aplicación

# CLASE DE USUARIO
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# FUNCIÓN PARA CARGAR UN USUARIO
def load_user(id):
    # Diccionario de usuario
    users = {
        "1": User("1", "Carolina"),
        "2": User("2", "Isabel"),
        "3": User("3", "Venom")
    }
    # Revisar si el usuario se encuentra en el diccionario
    if id in users:
        return users[id]
    else:
        return None

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/user/<id>') # Decorador que indica la URL que se va a utilizar

def get_user(id): # Función que se va a ejecutar (Función de vista)
    user = load_user(id) # Carga del usuario con el ID proporcionado
    if not user: # Verificación de que el usuario no existe
        abort(404) # Aborto de la solicitud con un código 404 (Not Found)
    return '<h1>Hello, %s</h1>' % user.name # Retorno del saludo al usuario

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run(debug=True) # Inicialización de la aplicación