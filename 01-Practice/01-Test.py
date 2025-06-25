from jinja2 import Environment, FileSystemLoader
import yaml

# Load YAML data
with open('data.yaml') as f:
    data = yaml.safe_load(f)

# Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')

# Render
output = template.render(data)

# Save to .tf file
with open('generated.tf', 'w') as f:
    f.write(output)
