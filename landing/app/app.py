from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os
import json

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    
    response = requests.get('http://add-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']
    

def minus(n1, n2):
    response = requests.get('http://minus-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']

def multiply(n1, n2):
    response = requests.get('http://multiply-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']

def divide(n1, n2):
    response = requests.get('http://divide-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']

def equals(n1, n2):
    response = requests.get('http://equals-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']

def exponent(n1, n2):
    response = requests.get('http://exponent-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']

def modulus(n1, n2):
    response = requests.get('http://modulus-service:5050/'+n1+'/'+n2)
    
    result = json.loads(response.content.decode('utf-8'))
    return result['result']



@app.route('/', methods=['POST', 'GET'])
def index():
    req1 = request.form.get("first")
    req2 = request.form.get("second")
    number_1, number_2 = None, None
    try:
        number_1 = float(req1)
        number_2 = float(req2)
    except Exception:
        print('cant convert', req1, req2, 'to float')
        number_1 = req1
        number_2 = req2
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = add(str(number_1), str(number_2))
    elif operation == 'minus':
        result =  minus(str(number_1), str(number_2))
    elif operation == 'multiply':
        result = multiply(str(number_1), str(number_2))
    elif operation == 'divide':
        if number_2==0:
            result = "Can't divide by 0"
        else: 
            result = divide(str(number_1), str(number_2))
    elif operation == 'equals':
        result = equals(str(number_1), str(number_2))
    elif operation == 'exponent':
        result = exponent(str(number_1), str(number_2))
    elif operation == 'modulus':
        result = modulus(str(number_1), str(number_2))
    else:
        result = 'Wrong'

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )