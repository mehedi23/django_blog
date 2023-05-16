
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