from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."), trim_blocks=False)
template = env.get_template("4.jinja.html")
     
data = {"items": ["a", "b", "c</li><li>d"]}
disp_text = template.render(data)
print(disp_text)
