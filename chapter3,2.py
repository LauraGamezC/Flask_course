from flask import Flask, render_template
from ensurepip import bootstrap
from flask_bootstrap import Bootstrap
from flask import render_template

app=Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/') #Con este decorador se especifica la ruta
def b_function():
  return render_template('user_temp.html', name='Laura')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500   