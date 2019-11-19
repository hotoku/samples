from bottle import route, run, template, static_file, request, view



@route("/")
def home():
    return "this is home"
        


@route("/hello/<name>")
def hello(name):
    return template("<p>Hello <b>{{name}}</b></p>", name=name)



@route("/hello2/<name>")
@view("hello2.
def hello2(name):
    return 

run(host='localhost', port=8890, reloader=True)
