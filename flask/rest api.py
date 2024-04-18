
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)


class Hello(Resource):

	
	def get(self):

		return jsonify({'message': 'hello world'})

	
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):

	def get(self, num):

		return jsonify({'square': num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# driver function
if __name__ == '__main__':

	app.run(debug = True)
