from jinja2 import FileSystemLoader,Environment

data = {
    "name" : "Peddireddy",
    "Year" : 2025,
    "Course" : "DevOps Learning",
    "RoleName" : "DevOps Admin",
    "aws_instance_type" : "t2.micro",
    "ami_id" : "ami01234"
}

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('main.tf.j2')

output = template.render(data)

print(output)

with open('output.tf','w') as f:
    f.write(output)
