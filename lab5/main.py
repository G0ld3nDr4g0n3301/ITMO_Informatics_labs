import seaborn
import matplotlib.pyplot as plot
import csv
import pandas


def convert(argument):
	return int(argument[:argument.find('.')])

with open('data.csv', 'r' , encoding='utf-8') as raw_data:
	columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE']
	date = ['11.09.2018','11.10.2018','13.11.2018','11.12.2018']
	csv_data = csv.reader(raw_data, delimiter=',')
	matrix = [[],[],[],[]]
	for row in csv_data:
		if row == []:
			break
		if row[0] == date[0]:
			matrix[0].append([convert(row[1]), convert(row[2]), convert(row[3]), convert(row[4])])
		if row[0] == date[1]:
			matrix[1].append([convert(row[1]), convert(row[2]), convert(row[3]), convert(row[4])])
		if row[0] == date[2]:
			matrix[2].append([convert(row[1]), convert(row[2]), convert(row[3]), convert(row[4])])
		if row[0] == date[3]:
			matrix[3].append([convert(row[1]), convert(row[2]), convert(row[3]), convert(row[4])])
	plot.figure(figsize=(16, 8))
	for i in range(4):
		frame = pandas.DataFrame(matrix[i], columns=columns)
		plot.subplot(2, 2, i + 1)
		seaborn.boxplot(data=frame,palette='husl')
		plot.title(date[i])
		plot.legend(columns,loc='upper right')
	plot.subplots_adjust(wspace=0.4, hspace=0.4)
	plot.show()

	# I'm so sleepy... I hardly can keep my eyes open.I haven't slept for 2 days.
