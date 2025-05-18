import os
import yaml

# data = [
#     {"name" : "alice" ,"role": "DevOps Engineer" ,"marks": "100"},
#     {"name" : "Bob" ,"role": "Development Engineer" ,"marks": "1000"},
#     {"name" : "Corbole" ,"role": "Ops Engineer" ,"marks": "200"},
# ]

data = {
    "student" : {
        "name" : "Peddireddy",
        "Role" : "DevOps Engineer",
        "Skills" : ["Terraform","Python","Kubernetes"],
        "marks" :
        {
            "Terraform" : 87,
            "Kubernetes" : 94,
            "Python" : 83
        }

    }
}

with open("Development.yaml" , 'w') as file:
    yaml.dump(data,file,default_flow_style=False,indent=4)