import lab2

# First array is tests,and the second is answers, found manually
# the key is the complexity level
tests = {
	'1': [['jdln:-Odfs:-Osdf','sddafsd sdfa / sdf asdfasdf / sadfasfdasfd'],['Не хайку.Должно быть 3 строки.','Не хайку.']],
	'2': [['Привет воин / Куда направляешься ты? / Конечно на информатику!'],['Не хайку.']],
	'3': [['Когда же закончится это? / Или уже отчислят меня? / Не хочу отчисления!','К горе уехал / Упал быстро с горы я! / Очень Мудрый я.','Привет'],['Не хайку.','Хайку!','Не хайку.Должно быть 3 строки.']],
	'4': [['', 'я / я / я','Смотреть больно на / ОПД не сделанное мной / Сдам ли лабу я?'],['Не хайку.Должно быть 3 строки.','Не хайку.','Хайку!']],
	'5': [['\n','\t / \n / \r', 'Сложные тесты / написал я для проги / не сработали.'],['Не хайку.Должно быть 3 строки.','Не хайку.','Хайку!',]],
	'a': [[''],['Не хайку.Должно быть 3 строки.']]
}

test_complex = input('Enter a test complexity(1-5) or "a" for all tests: ')

if (len(test_complex) != 1) or (test_complex not in '12345a'):
	print('ENTER A NUMBER BETWEEN 1 AND 5 OR "a" SYMBOL')
	raise SystemExit

if test_complex == 'a':
	for i in '12345':
		for j in tests[i][0]:
			tests['a'][0].append(j)
		for j in tests[i][1]:
			tests['a'][1].append(j)

success_counter = 0
for test_num in range(len(tests[test_complex][0])):

	if lab2.main(tests[test_complex][0][test_num]) == tests[test_complex][1][test_num]:
		result = 'SOLVED'
		success_counter += 1
	else:
		result = 'FAILED'
	print('Test %s running...   %s' % (test_num+1, result))

if success_counter != len(tests[test_complex][0]):
	print('%s tests failed' % (len(tests[test_complex][0]) - success_counter))
else:
	print('ALL TESTS SOLVED')

