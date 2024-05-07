import json

with open('status.json') as f:
    status = json.load(f)

print(status)
print(type(status))

status['height'] = 165.5

with open('status.json', 'w') as f:
    json.dump(status, f)

print(status)
