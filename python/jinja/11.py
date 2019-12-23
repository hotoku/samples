from jinja2 import Template


print(Template("{{hoge.fuga}}").render(dict(
    hoge=dict(
        fuga="a"
    )
)))
