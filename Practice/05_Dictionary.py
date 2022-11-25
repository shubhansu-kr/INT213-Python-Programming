di = {}

di = {
    "id": 21, 
    "str": 'shubh'
}

# key value pair. 
print(di["id"], di["str"])

print(di.keys(), di.values())

print(di.items())

# check keys. 
if 'ky' in di:
    print(di['ky'])

# key must be present otherwise error
di.pop('id')
print(di)

di['id'] = 21

for i in di:
    print(i)
    # prints the keys only

for i in range(10, 0, -1): 
    print(i)

