import requests
import json

# with open('serv.json') as cat_file:
#     data = json.load(cat_file)
# response = requests.get(f"http://{data['server']}/{data['port']}")
# print(json.loads(response.content))

kitty = {
    "calculated orbit": [
        [
            8.6,
            5.2,
            6.3
        ],
        [
            0.8,
            0.9,
            0.6
        ]
    ],
    "observations": [
        [
            6.5,
            1.3,
            9.5
        ],
        [
            0.9,
            0.7,
            0.8
        ]
    ]
}
nya = kitty["observations"][0]
ftsrgbhzd_edrtsfg = sum([i ** 2 for i in nya]) ** 0.5
nya1 = kitty["observations"][1]
ftsrgbhzd_edrtsfg1 = sum([i ** 2 for i in nya1]) ** 0.5
nya2 = kitty["calculated orbit"][0]
ftsrgbhzd_edrtsfg2 = sum([i ** 2 for i in nya2]) ** 0.5
nya3 = kitty["calculated orbit"][1]
ftsrgbhzd_edrtsfg3 = sum([i ** 2 for i in nya3]) ** 0.5

print(round(abs(ftsrgbhzd_edrtsfg - ftsrgbhzd_edrtsfg2), 2), round(abs(ftsrgbhzd_edrtsfg1 - ftsrgbhzd_edrtsfg3), 2))