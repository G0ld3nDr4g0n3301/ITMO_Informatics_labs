import re

def main(string):
	string = string.split(' / ')
	if len(string) != 3:
		return 'Не хайку.Должно быть 3 строки.'
	expr = re.compile("[уеоэаыяиюёЁУЕЫАОЭЮИЯ]")
	count1 = len(expr.findall(string[0]))
	count2 = len(expr.findall(string[1]))
	count3 = len(expr.findall(string[2]))
	if (count1 != 5) or (count2 != 7) or (count3 != 5):
		return 'Не хайку.'
	return 'Хайку!'

if __name__ == '__main__':
	string = input('')
	print(main(string))
