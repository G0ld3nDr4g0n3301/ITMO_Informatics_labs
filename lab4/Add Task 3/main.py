import test,y2p

yaml_data = ""
with open('schedule.yaml', 'r') as f:
	yaml_data = f.read()

test.test(yaml_data)