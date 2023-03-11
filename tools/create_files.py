import json
import yaml

with open('totallabels.json', 'w') as f:
    json.dump({}, f)

with open('totallabels.yaml', 'w') as f:
    yaml.dump({}, f)