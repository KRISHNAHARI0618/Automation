from jinja2 import Environment,FileSystemLoader
import yaml


with open('values.yaml','r') as f:
    values = yaml.safe_load(f)

env = Environment(loader = FileSystemLoader('.'))

template  = env.get_template('main.tf.j2')

output = template.render(values)

with open('main.tf','w') as file:
    file.write(output)