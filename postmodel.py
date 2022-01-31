import json
import sys, datetime

from jinja2 import Undefined

posts = [];

def CreatePost(data, status):
    print('creating a new post')
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    resp = json.loads(json_str)
    print('Creating a new post by:', resp['creator'])
    try:
            now = datetime.datetime.now()
            post = {};
            post = ({
            "postId": GenerateID(),
            "title" : resp['title'],
            "content" : resp['content'],
            "creator": resp['creator'],
            "created": now.strftime("%Y-%m-%d %H:%M:%S"),
            "comments": []
            })
            posts.append(post)
            status = 201
            print(post)
            return post, status
    except:
            status = 400
            return {'error': 'no content'}, status

def CreateComment(id, data, status): 
    convertedID = int(id)
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    resp = json.loads(json_str)
    print('Adding a new comment by:', resp['username'])
    found = False
    for i in posts:
        if (i['postId'] == convertedID):
            found = True

    if(found == True):
        if (id == Undefined):
            status = 400
            return {'error': 'post id is required'}, status
        else:
            try:
                now = datetime.datetime.now()
                comment = {};
                comment = ({
                "commentId": GenerateCommentID(convertedID),
                "content": resp['content'],
                "creator": resp['username'],
                "created": now.strftime("%Y-%m-%d %H:%M:%S")
                })
                for i in posts:
                    if (i['postId'] == convertedID):
                        i['comments'].append(comment)
                        status = 201
                        print(comment)
                        return comment, status

            except:
                status = 400
                return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def SelectPostByID(id, status):
    convertedID = int(id)
    found = False
    for i in posts:
        if (i['postId'] == convertedID):
            found = True
    if (found == True):
        if (id == Undefined):
            status = 400
            return {'error': 'post id is required'}, status
        try: 
            for i in posts:
                if (i['postId'] == convertedID):
                    print('Post found :', i['title'])
                    status = 200
                    return i, status
                if (i['postId'] != convertedID):
                    status = 404
                    return {'error': 'no content'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def SelectAllCommentsByPostID(id, status):
    convertedID = int(id)
    found = False
    for i in posts:
        if (i['postId'] == convertedID):
            found = True
    if (found == True):
        if (id == Undefined):
            status = 400
            return {'error': 'post id is required'}, status
        try: 
            for i in posts:
                if (i['postId'] == convertedID):
                    print('Post found :', i['title'])
                    status = 200
                    return i['comments'], status
                if (i['postId'] != convertedID):
                    status = 404
                    return {'error': 'no content'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def SelectPostsByTitle(title, status):
    print('Searching for posts by:', type(title))
    found = False
    for i in posts:
        if (i['title'] == title):
            found = True
    if (found == True):
        try: 
            for i in posts:
                if (i['title'] == title):
                    print('Post found :', i['title'])
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def SelectPostsByCreator(creator, status):
    print('Searching for posts by:', type(creator))
    found = False
    for i in posts:
        if (i['creator'] == creator):
            found = True
    if (found == True):
        try: 
            for i in posts:
                print(i['creator'])
                print(type(i['creator']))
                if (i['creator'] == creator):
                    print('Post found :', i['title'])
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def SelectAllPosts(status):
    try:
        print('All posts found')
        status = 200
        return posts, status
    except:
        status = 400
        return {'error': 'no content'}, status

def DeletePostByID(id,status):
    convertedID = int(id)
    count = 0
    found = False
    for i in posts:
        count = count + 1
        if (count > 0):
            if (i['postId'] == convertedID):
                found = True
    if (id == Undefined):
        status = 400
        return {'error': 'post id is required'}, status
    if (found == True):
        try:
            for i in posts:
                if (i['postId'] == convertedID):
                    posts.remove(i)
                    status = 200
                    print('Post deleted')
                    return {'message': 'Post deleted'}, status
                else:
                    status = 404
                    return {'error': 'no content'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status

def DeleteCommentByID(postID, id, status):
    convertedPostID = int(postID)
    convertedCommentID = int(id)
    count = 0
    inner = 0
    if (postID == Undefined):
        status = 400
        return {'error': 'post id is required'}, status
    if(id == Undefined):
        status = 400
        return {'error': 'comment id is required'}, status
    print(convertedCommentID)
    print(convertedPostID)
    found = False
    for i in posts:
        count = count + 1
        for j in i['comments']:
            inner = inner + 1
            if (inner > 0):
                if (j['commentId'] == convertedCommentID):
                    found = True
                    print('found')
                    break
    print(found)
    if (found == True):
        try:
            for i in posts:
                if (i['postId'] == convertedPostID):
                    print('Post found :', i['title'])
                    for j in i['comments']:
                        if (j['commentId'] == convertedCommentID):
                            i['comments'].remove(j)
                            status = 200
                            print('Comment deleted')
                            return {'message': 'Comment deleted'}, status
                        else:
                            status = 404
                            return {'message': 'Cannot delete a Comment'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'no content'}, status




def GenerateID():
    return len(posts) + 1

def GenerateCommentID(id):
    total = 0
    for i in posts:
        if (i['postId'] == id):
            total = len(i['comments']) + 1
    return total



