import json
import sys, datetime

userdata = [];

async def CreateUser(data, status):
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    resp = json.loads(json_str)
    print('Adding a new user :', resp['username'])
    if (resp['username'] == ''):
        status = 400
        return {'error': 'no content'}, status
        ## convert data to json
    else:
        try:
            now = datetime.datetime.now()
            userInput = {};
            userInput = ({
            "id": GenerateID(),
            "username": resp['username'],
            "password": resp['password'],
            "name": resp['name'],
            "email": resp['email'],
            "created": now.strftime("%Y-%m-%d %H:%M:%S")
            })
            userdata.append(userInput)
            status = 201
            print(userInput)
            return userInput, status
        except:
            status = 400
            return {'error': 'no content'}, status

async def SelectUserByID(id, status):
    convertedID = int(id)
    try: 
        for i in userdata:
            if (i['id'] == convertedID):
                print('User found :', i['username'])
                status = 200
                return i, status
            if (i['id'] != id):
                status = 404
                return {'error': 'no content'}, status
    except:
        status = 400
        return {'error': 'no content'}, status


async def SelectUserByUsername(username, status):
    try: 
        for i in userdata:
            print(i['username'])
            print(username)
            if (i['name'] == username):
                print('User found :', i['name'])
                status = 200
                return i, status
    except:
        status = 400
        return {'error': 'no content'}, status


async def SelectAllUsers(status):
    try:
        print('Getting all users')
        status = 200
        return userdata, status
    except:
        status = 400
        return {'error': 'no content'}, status


async def UpdateUserByID(id, data, status):
    print('update user by id')
    ## dump string to json
    convertedID = int(id)
    json_str = json.dumps(data.json)
    ## load json to python object
    resp = json.loads(json_str)
    print('Updating user :', resp['username'])
    if (resp['username'] == ''):
        print('no content')
        status = 400
        return {'error': 'no content'}, status
        ## convert data to json
    else:
        try:
            for i in userdata:
                if (i['id'] == convertedID):
                    i['username'] = resp['username']
                    i['password'] = resp['password']
                    i['name'] = resp['name']
                    i['email'] = resp['email']
                    print(userdata)
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status


async def DeleteUserByID(id, status):
    convertedID = int(id)
    try:
        for i in userdata:
            if (i['id'] == convertedID):
                print('Deleting user :', i['username'])
                userdata.remove(i)
                status = 200
                return {'message': 'deleted'}, status
    except:
        status = 400
        return {'error': 'no content'}, status


def GenerateID():
    return len(userdata) + 1