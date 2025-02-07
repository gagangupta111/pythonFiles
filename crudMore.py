from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        un = json_data['username']
        pw = json_data['password']
        #args = parser.parse_args()
        #un = str(args['username'])
        #pw = str(args['password'])
        return jsonify(u=un, p=pw)

api.add_resource(HelloWorld, '/testing')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)
