import lab1

# First array is tests,and the second is answers, found manually
# the key is the complexity level
tests = {
	'1': [['jdln:-Odfs:-Osdf','asflkj:-Onasfnkn:-On,na:-O:-O'],[2,4]],
	'2': [['LAlkajsf:-Oj;jasfk:-Olajf:-O','slkjalkjk:-Oln,dsnf,:-Onmsd,mf:-O'],[3,3]],
	'3': [[';lkl;aaask;msa;lfm:-O:-O:-Omnas.f:-O:-:-:-O',';askfO-::-O:-:O-:O--O:'],[5,1]],
	'4': [['nfas,naslnf:-O;nlsnf:-Onj:-O:::--O:'],[3]],
	'5': [['sdfgdsfg:fd-sdfOsd:-Ogfasg:-Oadfs'],[2]],
	'a': [[''],[0]]
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

	if lab1.main(tests[test_complex][0][test_num]) == tests[test_complex][1][test_num]:
		result = 'SOLVED'
		success_counter += 1
	else:
		result = 'FAILED'
	print('Test %s running...   %s' % (test_num+1, result))

if success_counter != len(tests[test_complex][0]):
	print('%s tests failed' % (len(tests[test_complex][0]) - success_counter))
else:
	print('ALL TESTS SOLVED')

