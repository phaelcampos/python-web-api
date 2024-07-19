import cgi
from database import conn

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))

def get_post_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")
    
    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")
        
    return[dict(zip(fields, post))for post in results]

def render_template(template_name, **context):
    template = env.get_template(template_name)
    return template.render(**context).encode("utf-8")


def add_new_post(posts):
    cursor = conn.cursor()
    cursor.execute(
        """\
            INSERT INTO post (title, content, author)
            VALUES (:title, :content, :author)
        """,
        posts
    )
    conn.commit()


def application(environ, start_response):
    body = b"Content not found"
    status = "404 Not Found"
    # processar o request 
    
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    
    if path == "/" and method == "GET":
        posts = get_post_from_database()
        body = render_template(
            "list.template.html",
            post_list=posts
        )
        status = "200 ok"
        
    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html",
            post=get_post_from_database(post_id=post_id)[0]
        )
        
        status = "200 OK"
    elif path == "/new" and method == "GET":
        body = render_template("form.template.html")
        status = "200 OK"
        
    elif path == "/new" and method == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"],
            environ=environ,
            keep_blank_values=1
        )
        post = {item.name:item.value for item in form.list}
        add_new_post(post)
        body = b"new post created with success!"
        status = "201 Created"
        
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [body]