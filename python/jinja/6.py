from jinja2 import Template, Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('6-1.jinja.txt')
     
data = dict(
    val="hoge"
)
disp_text = template.render(data)
print(disp_text)
