from flask import Flask
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)

class exponent(Resource):
    def get(self, num1, num2):
        result = math.pow(num1,num2)
        return {'result': result}

api.add_resource(exponent, '/<float:num1>/<float:num2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
