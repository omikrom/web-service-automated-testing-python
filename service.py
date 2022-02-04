
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
    res = await usermodel.CreateUser(request, status)
    return jsonify(res[0]), res[1]

@service.route('/users', methods=['GET'])
async def getusers():
    status = 0
    res = await usermodel.SelectAllUsers(status)
    return jsonify(res[0]), res[1]


@service.route('/user/<id>', methods=['GET'])
async def getuser(id):
    status = 0
    res = await usermodel.SelectUserByID(int(id), status)
    return jsonify(res[0]), res[1]

@service.route('/user', methods=['GET'])
async def getuserbyname():
    status = 0
    name = request.args.get('username')
    if (type(name) == str):
        res = await usermodel.SelectUserByUsername(name, status)
        return jsonify(res[0]), res[1]

@service.route('/user/<id>', methods=['PATCH'])
async def updateuser(id):
    status = 0
    res = await usermodel.UpdateUserByID(int(id), request, status)
    return jsonify(res[0]), res[1]

@service.route('/user/<id>', methods=['DELETE'])
async def deleteuser(id):
    status = 0
    res = await usermodel.DeleteUserByID(int(id), status)
    return jsonify(res[0]), res[1]


    ## POST ROUTES ##


@service.route('/createpost', methods=['POST'])
async def createpost():
    status = 0
    res = await postmodel.CreatePost(request, status)
    return jsonify(res[0]), res[1]


@service.route('/post/<id>/comment', methods=['POST'])
async def createcomment(id):
    status = 0
    res = await postmodel.CreateComment(int(id), request, status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>', methods=['GET'])
async def getpost(id):
    status = 0
    res = await postmodel.SelectPostByID(int(id), status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>/comments', methods=['GET'])
async def getcomments(id):
    status = 0
    res = await postmodel.SelectAllCommentsByPostID(int(id), status)
    return jsonify(res[0]), res[1]

@service.route('/posts', methods=['GET'])
async def getpostsbytitle():
    status = 0
    title = request.args.get('title')
    if (type(title) == str):
        res = await postmodel.SelectPostsByTitle(title, status)
        return jsonify(res[0]), res[1]
    else:
        return jsonify([]), 400

@service.route('/posts/user', methods=['GET'])
async def getpostsbycreator():
    status = 0
    creator = request.args.get('creator')
    if (type(creator) == str):
        res = await postmodel.SelectPostsByCreator(creator, status)
        return jsonify(res[0]), res[1]
    else:
        return jsonify([]), 400


@service.route('/post/<id>', methods=['DELETE'])
async def deletepost(id):
    status = 0
    res = await postmodel.DeletePostByID(int(id), status)
    return jsonify(res[0]), res[1]

@service.route('/post/<id>/comment/<postId>', methods=['DELETE'])
async def deletecomment(postId, id):
    status = 0
    res = await postmodel.DeleteCommentByID(int(postId), int(id), status)
    return jsonify(res[0]), res[1]



osenv = os.getenv('PORT')

if __name__ == '__main__':
    service.run(host='0.0.0.0', port=osenv)

##asyncio.run()


