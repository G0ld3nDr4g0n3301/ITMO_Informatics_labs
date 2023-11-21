import y2p

def test(yaml_data):
	root_element = y2p.yaml_to_py(yaml_data)
	recursive_test(root_element)

def recursive_test(element):
	if isinstance(element.value, str):
		print(element.indent, element.parent.key, element.key, element.value)
	else:
		for i in element.value:
			if isinstance(i, y2p.linked_list):
				print(i.indent, i.parent.key, i.key)
				recursive_test(i)
			else:
				print(i)