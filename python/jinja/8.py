from jinja2 import Template
 
tpl_text = """
{% set i = 0 %}
{% while i < 10 %}
{{i}}
{% i += 1 %}
{% endwhile %}
"""
template = Template(tpl_text)
 
data = dict(
)
disp_text = template.render(data)
print(disp_text)
