import subprocess as sp
import json
import os
from typing import Any, Dict

from flask import Flask, request

app = Flask(__name__)


@app.route("/echo", methods=["POST"])
def search() -> bytes:
    data: Dict[str, Any] = request.get_json()  # type: ignore
    return json.dumps(data).encode("utf-8")


app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# curl -X POST  -H 'Content-Type: application/json'  -d '{"x": 1}' http://localhost:8080/echo
