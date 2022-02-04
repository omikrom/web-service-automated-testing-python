import json
import sys, datetime

userdata = [];

async def CreateUser(data, status):
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    req = json.loads(json_str)
    print('Adding a new user :', req['username'])
    try:
        now = datetime.datetime.now()
        userInput = {};
        userInput = ({
        "id": GenerateID(),
        "username": req['username'],
        "password": req['password'],
        "name": req['name'],
        "email": req['email'],
        "created": now.strftime("%Y-%m-%d %H:%M:%S")
        })
        userdata.append(userInput)
        status = 201
        return userInput, status
    except:
        status = 400
        return {'error': 'no content'}, status

async def SelectUserByID(id, status):
    print('Reading user details by id: ', id)
    found = False
    for i in userdata:
        if (i['id'] == id):
            found = True
            break
    if(found == True):
        try: 
            for i in userdata:
                if (i['id'] == id):
                    print('User found :', i['username'])
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'user id not found'}, status


async def SelectUserByUsername(username, status):
    print('Reading user details by name: ', username)
    found = False
    for i in userdata:
        if (i['username'] == username):
            found = True
            break
    if(found == True):
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
    else:
        status = 404
        return {'error': 'user name not found'}, status


async def SelectAllUsers(status):
    print('Reading all users')
    try:
        status = 200
        return userdata, status
    except:
        status = 400
        return {'error': 'no content'}, status


async def UpdateUserByID(id, data, status):
    print('update user by id: ', id)
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    req = json.loads(json_str)
    found = False
    for i in userdata:
        if(i['id'] == id):
            found = True
            break
    if(found == True):
        try:
            for i in userdata:
                if (i['id'] == id):
                    i['username'] = req['username']
                    i['password'] = req['password']
                    i['name'] = req['name']
                    i['email'] = req['email']
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'user id not found'}, status


async def DeleteUserByID(id, status):
    print('Deleting user by id: ', id)
    found = False
    for i in userdata:
        if(i['id'] == id):
            found = True
            break
    if(found == True):
        try:
            for i in userdata:
                if (i['id'] == id):
                    print('Deleting user :', i['username'])
                    i.remove(i)
                    status = 200
                    return {'message': 'deleted'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'user id not found'}, status


def GenerateID():
    return len(userdata) + 1