import numpy as np
from collections import Counter

# 4 inputs
input_vector =[.23,.65,.85,.93]
matmul0,matmul1,matmul2,matmul3,matmul4 = ([] for i in range(5))
output_vals=[]
output_sum=[]
count=0
# 4 inputs mapping to 5 outputs
# 5 outputs, or possible actions to take
w_matrix = np.array([
	[.11,.56,.45,.35,.56], #w1,n
	[.22,.89,.12,.68,.23], #w2,n
	[.33,.35,.56,.23,.15], #w3,n
	[.44,.78,.11,.44,.29], #w4,n
	])
	
for (x,w) in zip(input_vector,w_matrix):
		mult = x*w[0]
		matmul0.append(round(mult,2))
		mult = x*w[1]
		matmul1.append(round(mult,2))
		mult = x*w[2]
		matmul2.append(round(mult,2))
		mult = x*w[3]
		matmul3.append(round(mult,2))
		mult = x*w[4]
		matmul4.append(round(mult,2))
		
output_x0_wn=sum(matmul0)
output_x1_wn=sum(matmul1)
output_x2_wn=sum(matmul2)
output_x3_wn=sum(matmul3)
output_x4_wn=sum(matmul4)

ouput_vector = []

ouput_vector.append(round(output_x0_wn,2))
ouput_vector.append(round(output_x1_wn,2))
ouput_vector.append(round(output_x2_wn,2))
ouput_vector.append(round(output_x3_wn,2))
ouput_vector.append(round(output_x4_wn,2))

print(ouput_vector)










		



	

		





	


