import urllib
import re

def extractNo(str):
	regex = ur"and the next nothing is (\d+)"
	matches = re.search(regex, str)
	if matches:
		return matches.groups()[0]

	return "";

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
new_no = '12345'
i = 0
while i<500:
	data = urllib.urlopen(url+new_no)
	text = data.read()
	if (text == 'Yes. Divide by two and keep going.'):
		new_no = str(int(new_no) / 2)
	else:
		new_no = extractNo(text)

	if new_no == '':
		break
	print(i, new_no, text)
	i += 1