import yaml

with open('Data-Files.yaml','r') as f:
    yamlData = yaml.safe_load(f)
    print(yamlData['marks'][0]['Science'][0]['number'])

