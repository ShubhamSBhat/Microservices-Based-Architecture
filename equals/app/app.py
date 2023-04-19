from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class equals(Resource):
    def get(self, num1, num2):
        if num1==num2:
            result = True
        else:
            result = False
        return {'result': result}

api.add_resource(equals, '/<float:num1>/<float:num2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050 , host = '0.0.0.0')
