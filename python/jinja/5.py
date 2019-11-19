from jinja2 import Template, Environment, FileSystemLoader

def myfilter(x):
    return f"this is filtered: original value = '{x}'"

env = Environment(loader=FileSystemLoader("."))
env.filters["myfilter"] = myfilter

template = env.get_template("5.jinja.txt")
     
data = dict(
    val = "val"
)
disp_text = template.render(data)
print(disp_text)
