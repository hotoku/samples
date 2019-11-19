from jinja2 import Template
 
tpl_text = "{{ greeting }}! from {{ name }}"
template = Template(tpl_text)
 
data = dict(
    greeting="Hello World",
    name="hotoku"
)
disp_text = template.render(data)
print(disp_text)
