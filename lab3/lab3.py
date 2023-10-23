import re

def main(strings,letters,space):
	reg = '[%s].{%s}[%s].{%s}[%s]' % (letters[0],space,letters[1],space,letters[2])
	expr = re.compile(reg)
	for string in strings:
		sub = expr.search(string)
		if sub == None:
			continue
		if string == sub.group(0):
			yield sub.group(0)
		else:
			continue

if __name__ == '__main__':
	letters = [i for i in input('enter 3 letters: ')]
	if len(letters) != 3: 
		print('3 letters')
		raise SystemExit
	try:
		space = int(input('enter the length of spaces between letters: '))
		word_num = int(input('Enter the number of words: '))
	except:
		print('Enter a NUMBERS')
		raise SystemExit
	string = []
	for i in range(word_num):
		string.append(input(''))
	for i in main(string,letters,space):
		print(i)