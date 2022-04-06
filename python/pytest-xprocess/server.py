import click
from aiohttp import web
import sys
from datetime import datetime

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@click.command()
def main():
    with open(f"/tmp/hoge-{datetime.now().strftime('%s')}", "w") as fp:
        fp.write("hoge")
    print("server start", file=sys.stderr)
    sys.stderr.flush()
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


main()
