import lab3

# First array is tests,and the second is answers, found manually
# the key is the complexity level
tests = {
	'1': [ [ (['КаРмА','КоРкА','КоРмА','КоРчмА'],['К','Р','А'],1)],[['КаРмА','КоРкА','КоРмА']]],
	'2': [[(['ОваАывУ','Оававыу','офыАфвУ','ОООАААУ'],['О','А','У'],2)],[['ОваАывУ','ОООАААУ']]],
	'3': [ [ (['МОД','ДОМ','ДрОМ'],['Д','О','М'],0)],[['ДОМ']]],
	'4': [ [ (['CnapT','CcAsT','ClasT'],['C','a','T'],1)],[['CnapT','ClasT']]],
	'5': [ [ (['Rs4юЯ','Ra4aЯ','rs5kЯ'],['R','4','Я'],1)],[['Rs4юЯ','Ra4aЯ']]]
}

test_complex = input('Enter a test complexity(1-5) or "a" for all tests: ')

if (len(test_complex) != 1) or (test_complex not in '12345a'):
	print('ENTER A NUMBER BETWEEN 1 AND 5 OR "a" SYMBOL')
	raise SystemExit

if test_complex == 'a':
	tests['a'] = [[i for i in tests['1'][0]],[i for i in tests['1'][1]] ]
	for i in '2345':
		for j in tests[i][0]:
			tests['a'][0].append(j)
		for j in tests[i][1]:
			tests['a'][1].append(j)

success_counter = 0
for test_num in range(len(tests[test_complex][0])):
	test_data = tests[test_complex][0][test_num]
	ans_list = [i for i in lab3.main(*test_data)]
	result = 'SOLVED'
	success_counter += 1
	for i in range(len(ans_list)):
		try:
			if ans_list[i] != tests[test_complex][1][test_num][i]:
				result = 'FAILED'
				success_counter -= 1
				break
		except:
			result = 'FAILED'
			success_counter -= 1
			break
	print('Test %s running...   %s' % (test_num+1, result))

if success_counter != len(tests[test_complex][0]):
	print('%s tests failed' % (len(tests[test_complex][0]) - success_counter))
else:
	print('ALL TESTS SOLVED')

