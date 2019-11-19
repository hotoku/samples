from jinja2 import Template
 
tpl_text = """\
{% for i in range(3) -%}
  {{ i }}
{%- endfor %}
===
{% for i in range(3) -%}
  {{ i }}
{% endfor %}
===
{%- for i in range(3) -%}
  {{ i }}
{% endfor %}
===
{% for i in range(3) -%}
  {{ i }}
{% endfor %}
===
{% for i in range(3) -%}
  {{ i }}
{% endfor %}fuga
"""
template = Template(tpl_text)
 
data = dict(
    hoge="hoge"
)
disp_text = template.render(data)
print(disp_text)
