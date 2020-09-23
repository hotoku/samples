from jinja2 import Template

tpl_text = """
{%- for n in range(10) -%}
{{- n }}
{% endfor -%}
"""
template = Template(tpl_text)

disp_text = template.render({})
print(disp_text)
