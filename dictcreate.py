index = [[['X',34],['Y',36],['Z',34]],[['X',35],['Y',37],['Z',38]]]

def createdict(index):
	result ={}
	finalresult = []
	for x in index:
		for i in x:
			if i[0] in result.keys():
				result[i[0]].append(i[1])
			else:
				result[i[0]] = [i[1]]
	for i in result.keys():
		temp = result[i]
		if (temp[-1] - temp[0]) == (len(temp)-1):
			finalresult.append(i)
 
	return finalresult

print createdict(index)
