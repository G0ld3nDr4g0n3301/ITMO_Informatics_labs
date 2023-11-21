class linked_list():

	def __init__(self, indent, parent, key=None, value=None):
		self.indent = indent
		self.parent = parent
		self.key = key
		if value:
			self.value = value
		else:
			self.value = []

	def get(self):
		return self

def yaml_to_py(yaml_data):
	lines = yaml_data.strip().split('\n')
	root_element = linked_list(None, None, "root")
	current_parent = root_element
	#print(root_element)
	#print(current_parent)
	for line in lines:
		if line == '': continue
		indent = 0
		while line[indent] == ' ':
			indent += 1
		indent = int(indent/2)
		element = linked_list(indent, current_parent.get())

		if indent == 0:
			element.parent = root_element
		else:
			while indent <= current_parent.indent:
				current_parent = current_parent.parent
				element.parent = current_parent
		
		#if current_parent.key == "root":
		#	print(element.value[0].key)
		#	print(element.key)
		#	print(current_parent.value[0].key + 'LOL')
		#	print('-----------------------------')

		parts = line.strip().split(':', 1)
		if len(parts) == 1:
			#if element.key == "friday":
				#print(current_parent.value[0].key)
			if parts[0][0] == '-':
				element.parent.value.append(parts[0].replace('- ',''))
			else:
				print('FATAL ERROR IN LIST RECOGNITION')
		else:
			if parts[1] == '':
				element.key = parts[0]
				current_parent.value.append(element)
				# if current_parent.key == "root":
				# 	print(current_parent.key)
				# 	print('FOX')
				# 	print(element.key)
				# 	print(element.value[0].key, 'LOL')
				# 	print("ACHATHA2")
				current_parent = element
				#print(current_parent.value)

			else:
				element = linked_list(indent, current_parent, parts[0], parts[1])
				current_parent.value.append(element)
				#print(current_parent.key)
				current_parent = element
				#print(current_parent.key)
	return root_element

