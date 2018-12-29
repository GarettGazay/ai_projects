
#simple perceptron
def perceptron(input_vector,weights):
	output_layer=[]
	for (x,w) in zip(input_vector,weights):
		print('x:',x,'w:',w)
		mult = x*w
		output_layer.append(round(mult,2))
		print('multiplied_values:',(output_layer))
	result = sum(output_layer)
	print('final result:',round(result,2))
	return None
perceptron([.2,.6,.13],[.9,.042,.16])



