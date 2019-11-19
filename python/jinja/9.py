from jinja2 import Template
 
tpl_text = """
{{ hoge }}
{#
  in comment
  {{ hoge }}
#}
out of comment
"""
template = Template(tpl_text)
 
data = dict(
    hoge="hoge"
)
disp_text = template.render(data)
print(disp_text)
