from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="Templates")

@app.route('/user/<name>') 
def user(name='Laura'): 
    age = 16
    my_list = [1, 2, 3, 4]
    return render_template('user.html', var_name=name, var_age=age, var_list=my_list)

if __name__ == '__main__':
    app.run(debug=True, port=8000)    