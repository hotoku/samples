from jinja2 import Template, Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("2.jinja.txt")
 
data = dict(
    greeting="Hello World",
    name="hotoku"
)
disp_text = template.render(data)
print(disp_text)
