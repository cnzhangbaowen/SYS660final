import pandas as pd
import numpy as np

df = pd.read_csv('try.csv',index_col=0,header=None)

arrangement = []

for row in df.iterrows():
    row = list(row)
    row[1] = row[1].as_matrix().reshape(6,5)
    arrangement.append(row)

q1 = int(input('Do you prefer popular game or minority game:'))
q2 = int(input('How much time do you want to spend on a game:'))
q3 = int(input('How much you\'d like to spend on video game:'))
q4 = int(input('What difficulty would you like to choose:'))
q5 = int(input('What system requirement would you like to choose:'))
q6 = int(input('What rating would you like to choose:'))

for i in range(len(arrangement)):
	print((arrangement[i])[0])
	print('合 = ',(((arrangement[i])[1])[0][q1-1])+(((arrangement[i])[1])[1][q2-1])+(((arrangement[i])[1])[2][q3-1])+(((arrangement[i])[1])[3][q4-1])+(((arrangement[i])[1])[4][q5-1])+(((arrangement[i])[1])[5][q6-1]))
	# print(row[0])
    (arrangement[i])[0][len((arrangement[i])[0]):len((arrangement[i])[0])] = ((arrangement[i])[1])[0][q1-1])+(((arrangement[i])[1])[1][q2-1])+(((arrangement[i])[1])[2][q3-1])+(((arrangement[i])[1])[3][q4-1])+(((arrangement[i])[1])[4][q5-1])+(((arrangement[i])[1])[5][q6-1])
	# print(row[0])


