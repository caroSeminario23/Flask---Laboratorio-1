# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask
from flask import redirect # Importación de la función redirect para redireccionar a otra URL

app = Flask(__name__) # Creación de la instancia de la aplicación

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/') # Decorador que indica la URL que se va a utilizar
def index(): # Función que se va a ejecutar (Función de vista)
    return redirect('http://www.example.com') # Redireccionamiento a la URL 'http://www.example.com'

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run(debug=True) # Inicialización de la aplicación