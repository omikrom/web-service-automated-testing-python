
#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import asyncio
import os

## testing
import usermodel
import postmodel
##usermodel.CreateUser()


##json serialize
#from flask import jsonify

##request data
##from flask import request

service = Flask(__name__)

CORS(service)
cors = CORS(service, resources={r"/api/*": {
    "origins": "*",
    "methods": "GET, POST, PUT, DELETE, OPTIONS",
    "allowedHeaders":  "Authorization, Origin, Content-Type, Accept, X-Requested-With",
    "maxAge": 1728000
    }})

@service.route('/', methods=['GET'])
def welcome():
	return "Welcome!"


    ## USER ROUTES ##

@service.route('/createuser', methods=['POST'])
async def createuser():
    status = 0
    res = usermodel.CreateUser(request, status)
    return jsonify(res[0]), res[1]

@service.route('/users', methods=['GET'])
async def getusers():
    status = 0
    res = usermodel.SelectAllUsers(status)
    print(res[0])
    print(res[1])
    return jsonify(res[0]), res[1]


@service.route('/user/<id>', methods=['GET'])
async def getuser(id):
    status = 0
    res = usermodel.SelectUserByID(id, status)
    print(res)
    print(res[1])
    return jsonify(res[0]), res[1]

@service.route('/user', methods=['GET'])
async def getuserbyname():
    status = 0
    name = request.args.get('username')
    res = usermodel.SelectUserByUsername(name, status)
    print(res)
    print(res[1])
    return jsonify(res[0]), res[1]

@service.route('/user/<id>', methods=['PATCH'])
async def updateuser(id):
    print('test')
    status = 0
    res = usermodel.UpdateUserByID(id, request, status)
    print(res[1])
    return jsonify(res[0]), res[1]

@service.route('/user/<id>', methods=['DELETE'])
async def deleteuser(id):
    status = 0
    res = usermodel.DeleteUserByID(id, status)
    print(res[1])
    return jsonify(res[0]), res[1]



    ## POST ROUTES ##


@service.route('/createpost', methods=['POST'])
async def createpost():
    status = 0
    res = postmodel.CreatePost(request, status)
    return jsonify(res[0]), res[1]


@service.route('/post/<id>/comment', methods=['POST'])
async def createcomment(id):
    status = 0
    res = postmodel.CreateComment(id, request, status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>', methods=['GET'])
async def getpost(id):
    status = 0
    res = postmodel.SelectPostByID(id, status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>/comments', methods=['GET'])
async def getcomments(id):
    status = 0
    res = postmodel.SelectAllCommentsByPostID(id, status)
    return jsonify(res[0]), res[1]

@service.route('/posts', methods=['GET'])
async def getpostsbytitle():
    status = 0
    title = request.args.get('title')
    print(title)
    res = postmodel.SelectPostsByTitle(title, status)
    return jsonify(res[0]), res[1]

@service.route('/posts/user', methods=['GET'])
async def getpostsbycreator():
    status = 0
    user = request.args.get('creator')
    print(user)
    res = postmodel.SelectPostsByCreator(user, status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>/comment/<postId>', methods=['DELETE'])
async def deletecomment(postId, id):
    status = 0
    res = postmodel.DeleteCommentByID(postId, id, status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>', methods=['DELETE'])
async def deletepost(id):
    status = 0
    res = postmodel.DeletePostByID(id, status)
    return jsonify(res[0]), res[1]


if __name__ == '__main__':
    service.run(host='0.0.0.0', port=int(os.getenv('PORT')))
asyncio.run()

