from bottle import route, run, template, static_file, request, HTTPResponse
import json


def return_json(ret):
    header = {
        "Content-Type": "application/json"
    }
    body = json.dumps(ret)
    return HTTPResponse(status=200, body=body, headers=header)


@route("/")
def home():
    return "this is home"


@route("/hello/<name>")
def hello(name):
    return template("<p>Hello <b>{{name}}</b></p>", name=name)


@route("/json")
def route_json():
    ret = dict(
        x=1,
        y="abc"
    )
    return return_json(ret)


run(host='localhost', port=8890, reloader=True)
