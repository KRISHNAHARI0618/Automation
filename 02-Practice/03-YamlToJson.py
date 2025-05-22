import yaml
import json


with open('config.yaml','r') as file:
    yaml_load = yaml.safe_load(file)
    
with open('Output.json', 'w') as file:
    json.dump(yaml_load,file,indent=2)
    # file.write(jsondata)

# print(jsondata)


## When we are taking anyting from the file is called Loading 
## When we are making output to file is called Dumping

"""
| Format | Read from | Function    | Write to | Function |
| ------ | --------- | ----------- | -------- | -------- |
| YAML   | File      | `safe_load` | File     | `dump`   |
| JSON   | File      | `load`      | File     | `dump`   |
| JSON   | String    | `loads`     | String   | `dumps`  |

"""