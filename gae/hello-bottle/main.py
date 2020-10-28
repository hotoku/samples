from bottle import Bottle
from datetime import datetime


app = Bottle()


@app.route('/')
def root():
    with open("times.txt") as f:
        lines = f.readlines()
    lines.append(datetime.now().strftime("%Y-%m-%d"))
    return f"{lines}"


if __name__ == '__main__':
    app.run(host='localhost', port=8080, reloader=True, debug=True)
