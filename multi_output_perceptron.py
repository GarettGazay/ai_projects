import random
import time
iterations=0

def mop(x1,x2,x3,w1,w2):
	global iterations
	x=[x1,x2,x3]
	w=[w1,w2]

	x1_w1=x[0]*w[0]
	x1_w2=x[0]*w[1]

	x2_w1=x[1]*w[0]
	x2_w2=x[1]*w[1]

	x3_w1=x[2]*w[0]
	x3_w2=x[2]*w[1]

	output_1=[]
	output_2=[]

	output_1.extend((x1_w1, x2_w1, x3_w1))
	output_2.extend((x1_w2, x2_w2, x3_w2))

	sum_out1=sum(output_1)
	sum_out2=sum(output_2)

	print('Right Leg:',round(sum_out1,2))
	print('Left Leg:',round(sum_out2,2))
	print('')

	while iterations < 10:
		iterations+=1
		time.sleep(.5)
		mop(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))


mop(random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0))
print('Multi-Output Perceptron ;)')































# # 4 inputs
# input_vector =[.23,.15,.35,.66]
# matmul0,matmul1,matmul2,matmul3,matmul4 = ([] for i in range(5))
# # 4 inputs mapping to 5 outputs
# # 5 outputs, or possible actions to take
# w_matrix = np.array([
# 	[.11,.56,.45,.35,.56], #w1,n
# 	[.22,.89,.12,.68,.23], #w2,n
# 	[.33,.35,.56,.23,.15], #w3,n
# 	[.44,.78,.11,.44,.29], #w4,n
# 	])
# x = input_vector

		
# output_x0_wn=sum(matmul0)
# output_x1_wn=sum(matmul1)
# output_x2_wn=sum(matmul2)
# output_x3_wn=sum(matmul3)
# output_x4_wn=sum(matmul4)

# output_vector = []

# output_vector.append(round(output_x0_wn,2))
# output_vector.append(round(output_x1_wn,2))
# output_vector.append(round(output_x2_wn,2))
# output_vector.append(round(output_x3_wn,2))
# output_vector.append(round(output_x4_wn,2))
# print('')
# print('ouput_vector:',output_vector)










		



	

		





	


