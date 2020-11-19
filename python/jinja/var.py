from jinja2 import Template

tpl = """
{% set x = 1%}
{{ x + 1 }}
"""

print(Template(tpl).render({}))
