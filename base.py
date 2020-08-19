import reservadas

inputFile = open('./input.txt').read().split('\n')

for line in inputFile:
    results = reservadas.getLineValues(line)
    for result in results:
        for key in result:
     	    print(f'<{key},{result[key]}>')
