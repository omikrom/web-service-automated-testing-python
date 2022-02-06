import json
import sys, datetime


posts = [];

async def CreatePost(data, status):
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    req = json.loads(json_str)
    print('Creating a new post by:', req['creator'])
    try:
            iD = GenerateID();
            date = datetime.datetime.now();
            post = {};
            post = ({
            "postId": iD,
            "title" : req['title'],
            "content" : req['content'],
            "created": date.strftime("%Y-%m-%d %H:%M:%S"),
            "creator": req['creator'],
            "comments": []
            })
            posts.append(post)
            status = 201
            return post, status
    except:
            status = 400
            return {'error': 'no content'}, status

async def CreateComment(id, data, status): 
    ## dump string to json
    json_str = json.dumps(data.json)
    ## load json to python object
    req = json.loads(json_str)
    print('Adding a new comment by:', req['creator'])
    found = False
    for i in posts:
        if (i['postId'] == id):
            found = True
            break
    if(found == True):
            try:
                now = datetime.datetime.now()
                comment = {};
                comment = ({
                "commentId": GenerateCommentID(id),
                "content": req['content'],
                "creator": req['creator'],
                "created": now.strftime("%Y-%m-%d %H:%M:%S")
                })
                for i in posts:
                    if (i['postId'] == id):
                        i['comments'].append(comment)
                        status = 201
                        return comment, status

            except:
                status = 400
                return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status

async def SelectPostByID(id, status):
    print('Reading post details for ID:', id);
    found = False
    for i in posts:
        if (i['postId'] == id):
            found = True
            break
    if (found == True):
        try: 
            for i in posts:
                if (i['postId'] == id):
                    print('Post found :', i['title'])
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status



async def SelectAllCommentsByPostID(id, status):
    print('Reading all comments for post ID:', id);
    found = False
    for i in posts:
        if (i['postId'] == id):
            found = True
            break
    if (found == True):
        try: 
            for i in posts:
                if (i['postId'] == id):
                    print('Post found :', i['title'])
                    status = 200
                    return i['comments'], status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status

async def SelectPostsByTitle(title, status):
    print('Searching for posts by:', title)
    found = False
    for i in posts:
        if (i['title'] == title):
            found = True
            break
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
        return {'error': 'Post not found'}, status



async def SelectPostsByCreator(creator, status):
    print('Searching for posts by:', creator)
    found = False
    for i in posts:
        if (i['creator'] == creator):
            found = True
            break
    if (found == True):
        try: 
            for i in posts:
                if (i['creator'] == creator):
                    print('Post found :', i['title'])
                    status = 200
                    return i, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status

async def SelectAllPosts(status):
    print('Reading all posts')
    try:
        status = 200
        return posts, status
    except:
        status = 400
        return {'error': 'no content'}, status

async def DeletePostByID(id,status):
    print('Deleting post for post ID:', id)
    found = False
    for i in posts:
        if (i['postId'] == id):
                found = True
                break
    if (found == True):
        try:
            for i in posts:
                if (i['postId'] == id):
                    posts.remove(i)
                    status = 200
                    print('Post deleted')
                    return {'message': 'Post deleted', 'post' : i}, status
                else:
                    status = 404
                    return {'error': 'no content'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status

async def DeleteCommentByID(postID, id, status):
    print('Deleting comment of post ID:', postID)
    print('Deleting comment by ID:', id)
    found = False
    for i in posts:
        if (i['postId'] == postID):
            found = True
            break
    if (found == True):
        try:
            for i in posts:
                if (i['postId'] == postID):
                    print('Post found :', i['title'])
                    for j in i['comments']:
                        print('Comment found :', j['commentId'])
                        if (j['commentId'] == id):
                            i['comments'].remove(j)
                            status = 200
                            print('Comment deleted')
                            return {'message': 'Comment deleted'}, status
        except:
            status = 400
            return {'error': 'no content'}, status
    else:
        status = 404
        return {'error': 'Post not found'}, status




def GenerateID():
    return len(posts) + 1

def GenerateCommentID(id):
    total = 0
    for i in posts:
        if (i['postId'] == id):
            total = len(i['comments']) + 1
    return total



