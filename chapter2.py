from flask import Flask
from flask import request
from flask import redirect

app=Flask(__name__) #Se crea un objeto Flask

@app.route('/') #Con este decorador se especifica la ruta
def index(): 
    "Función que regresa un string"
    return '<h1>Hola mundo!<h1/>' 
    
@app.route('/params/') # params es una ruta que puede recibibir parametros enla url
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>/') 
def params(name='default', num=0):
    return 'Los parametros son: {}, {}'.format(name, num)

@app.route('/redir') #Con este decorador se especifica la ruta
def redir(): 
    "función que redirige a google"
    return redirect('https://www.google.com.mx/?hl=es-419') 

if __name__ == '__main__':
    app.run(debug=True, port=8000) #Ejecuta el servidor por default en el servidor:5000
"La bandera debug se encarga de actualizar los cambios al servidor"
