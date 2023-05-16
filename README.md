Python 3.10.6 <br>
pip install -r requirements.txt <br>
python manage.py makemigration <br>
python manage.py migrate <br>
python manage.py runserver <br>

<br>
<br>
<br>
<br>
<br>

<pre>
register <b>post</b> :
    url : "/api/user/register/",
    body :
        "email": "string",
        "username": "string",
        "password": "string",
        "password2" : "string"
</pre>

<pre>
register <b>post</b> :
    url : "/api/user/login/",
    body :
        "email": "string",
        "password": "string"
</pre>

<pre>
all blog <b>get</b> :
    url : "/api/user/blogs/",

specific blog <b>get</b> :
    url : "/api/user/blogs/<b>"blog_id"</b>",
</pre>

<pre>
user blog <b>get</b> :
    url : "/api/user/blogs/",
</pre>

<pre>
blog <b>post</b> :
    url : "/api/user/blogs/",
    header : {
        "Authorization" : "Bearer <b>token</b>"
    }
    body :
        "tittle": "string",
        "description": "string",
        "category": [array],
        "banner_image": {
            "image_name" : "string.file_extention",
            "image_url" : "string <b>base64</b>"
        }
</pre>

<pre>
blog <b>patch</b> :
    url : "/api/user/blogs/",
    header : {
        "Authorization" : "Bearer <b>token</b>"
    }
    params : {
        blog_no : <b> blog_id </b>
    }
    body :
        "tittle": "string",
        "description": "string",
        "category": [array],
        "banner_image": {
            "image_name" : "string.file_extention",
            "image_url" : "string <b>base64</b>"
        }
</pre>

<pre>
blog <b>delete</b> :
    url : "/api/user/blogs/",
    header : {
        "Authorization" : "Bearer <b>token</b>"
    }
    params : {
        blog_no : <b> blog_id </b>
    }
</pre>

<pre>
like / undo like blog <b>post</b> :
    url : "/api/reactions/likes/<b>"blog_id"</b>",
    header : {
        "Authorization" : "Bearer <b>token</b>"
    }
</pre>