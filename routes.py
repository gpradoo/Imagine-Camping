from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/eventos')
def servicos():
   return render_template('eventos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/estrutura')
def clientes():
    return render_template('estrutura.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')                
app.run(host = '0.0.0.0', port=5000, debug=True )
