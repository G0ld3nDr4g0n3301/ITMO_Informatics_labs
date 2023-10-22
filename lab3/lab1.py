import re

def main(string):
	expr = re.compile(":-O")
	count = expr.findall(string)
	return len(count)

if __name__ == '__main__':
	string = input('')
	print(main(string))
