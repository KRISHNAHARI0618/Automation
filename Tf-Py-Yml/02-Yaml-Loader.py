from platform import python_branch
import yaml


data = yaml.safe_load("""
name : Krishna
skills: 
  - Python
  - DevOps
  - Yaml
""")

print(data['name'])

print(data['skills'][1])

for i in range(len(data['skills'])):
    print(data['skills'][i])

yaml_str = yaml.dump(data,default_flow_style=False,indent=4)
print(yaml_str)


data1 = yaml.safe_load_all("""
--- 
name: Krishna
age: 24
skills:
  - Python
  - DevOps
  - Kubernetes

---
name: Hari
age: 25
skills:
  - Ansible
  - Docker
  - Terraform

""")

# yamlstr = yaml.dump_all(data1)
# print(yamlstr)

for i in data1:
    print(i)

