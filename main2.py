# c = "4"
# print(int(c))
# d = '{"f": [1,2, 3], "as": 1}'


# nya = [1, 2, 3]
# ftsrgbhzd_edrtsfg = sum([i ** 2 for i in nya]) ** 0.5


aerg = {
    "organic": [
        {
            "respiration": 3,
            "growth": 9,
            "metabolism": 4,
            "synthesis": 7
        },
        {
            "cleavage": 11,
            "digestion": 5,
            "division": 8,
            "response to stimuli": 1
        }
    ],
    "inorganic": [
        {
            "assimilation": 12,
            "dissimilation": 6
        }
    ]
}

server, host, type_dict, digits, mult = "127.0.0.1", "5000", "organic", 1, 2
lines = ""
for dictionary in aerg[type_dict]:
    nechet_val = []
    nechet_key = []

    mult_val = []
    mult_key = []

    multttttt = 1

    for key, value in dictionary.items():
        if value % 2 != 0 and len(str(value)) == digits:
            nechet_val.append(value)
            nechet_key.append(key)
        if value % mult == 0 and len(str(value)) == digits:
            mult_val.append(value)
            mult_key.append(key)
        multttttt *= value
    line = f"{nechet_key[nechet_val.index(max(nechet_val))]};{max(nechet_val)};{mult_key[mult_val.index(min(mult_val))]};{min(mult_val)};{abs(multttttt)%(mult+1)}"

    lines += line + "\n"
print(lines)

with open("derfgtedrag.csv", mode="w") as file:
    for line in lines.split("\n"):
        file.writelines(line)