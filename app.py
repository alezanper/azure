# from flask import Flask
# from flask_restful import Resource, Api
# 
# app = Flask(__name__)
# api = Api(app)
# 
# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
# 
# api.add_resource(Student, '/student/<string:name>')
# 
# app.run()

import os
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>My Demo</h1>" + "<p>A Simple Application for testing purposes.</p>" + "<h3>Hello from: " + socket.gethostname() + "</h3>" + "<button>Button</button>"

@app.route('/<name>')
def greeting(name):
    return "<h3>Hello, " + name + "</h3>"

if __name__ == "__main__":
    app.run()