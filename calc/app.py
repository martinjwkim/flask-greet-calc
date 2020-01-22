from flask import Flask, request
import operations
app = Flask(__name__)

@app.route('/math/<operation>')
def math(operation):
    a = float(request.args["a"])
    b = float(request.args["b"])
    operations_dict={
        'add':operations.add(a,b),
        'sub':operations.sub(a,b),
        'mult':operations.mult(a,b),
        'div':operations.div(a,b)
        }
    return str(operations_dict[operation])

@app.route('/add')
def add():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.add(a,b))

@app.route('/sub')
def sub():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.sub(a,b))

@app.route('/mult')
def mult():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.mult(a,b))

@app.route('/div')
def div():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.div(a,b))

