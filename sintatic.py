import json
inputFile = json.loads(open('./saida4.json').read())

for line in inputFile:
    words = []
    for word in line['lineValues']:
        words.append(word['value'])
    print(' '.join(words))