import math

#softmax test

def softmax(*input_vector):
	ea_vector=[]
	for a in input_vector:
		ea = (math.e ** a) 
		ea_vector.append(ea)
		vector_sum = sum(ea_vector)
	for k in ea_vector:
		result = k / vector_sum
		print('P:',round(result,2))
	print('input_vector:',input_vector)
	return 'Softmax results'


print(softmax(1,.2,3,4))


