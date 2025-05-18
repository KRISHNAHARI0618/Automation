from jinja2 import Environment,FileSystemLoader # type: ignore
import yaml

with open('data.yaml','r') as f:
    data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')
output = template.render(data)
with open('output.yaml','w') as fileOut:
    fileOut.write(output)


environ = Environment(loader=FileSystemLoader('.'))
template2 = environ.get_template('template.j2')
output2 = template2.render(data)

with open('output2.yaml','w') as file:
    file.write(output2)

devEnvironment = Environment(loader=FileSystemLoader('.'))
template2 = devEnvironment.get_template('template.j2')
output3 = template2.render(data)

with open('Output3.yaml','w') as f:
    f.write(output3)
