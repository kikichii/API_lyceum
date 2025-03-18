import sys
import json

meow = {
    "same": {

    },
    "different": {

    }
}
for i in sys.stdin:
    key, value = i.rstrip('\n').split(' ** ')
    if int(value) > 0 and int(value) % 2 == 0 and len(value) == 2:
        meow['same'][key] = value
    else:
        meow['different'][key] = value

with open('ocean.json', 'w') as cat:
    json.dump(meow, cat)