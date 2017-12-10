
def generate_recursive(g, n):
		
	if (n <= 0):
		return g

	else:
		k = len(g)
		newArr = []

		for i in range(k-1, -1, -1):
			newArr.append('0'+g[i])

		for i in range(k-1, -1, -1):
			newArr.append('1'+g[i])


	return generate_recursive(newArr, n-1)

def generateCodes(n):
	x = generate_recursive(['0','1'], n-1)
	return x

def start():
	n = int(raw_input())
	g = generateCodes(n)
	k = 1
	for i in range(len(g)-1, -1, -1):
		if (k > n):
			break

		print g[i]
		k +=1	


start()

