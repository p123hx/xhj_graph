#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import numpy as np
# data=np.load('idx_a.npy')
# print(len(data))
# # data_y=np.load('idx_q.npy')
# # # print('结果',data_y)
# # tran_data=np.load('idx2w.pkl')
# # # print(tran_data)
# # tran_next=np.load('w2idx.pkl')
# # print(tran_next)
#
# # test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
# # a=np.argmax(test, 0)
# # print(a)


import numpy as np
import matplotlib.pyplot as plt
data=open('loss6','r')
loss=[]

for i in data:
    aa=i.split(' ')
    if len(aa) < 6:
        continue
    bb=aa[-1].strip('\n')
    loss.append(float(bb))
loss_t=loss[len(loss)-100:len(loss)]
avrg = sum(loss_t)/100
list_g=[]
for i in range(10):
    list_batch = loss_t[10*i:10*(i+1)]
    list_g.append(sum(list_batch)/10)

plt.figure(figsize=(12,6))

x=np.arange(1,11,1)

y=list_g

plt.plot(x,y,label='leaning rate',color='red',linewidth=1.0,linestyle='--') #前后添加"$"符号 表示数学公式

plt.legend(loc='best')
y=[avrg]*10
plt.plot(x,y,label='Average',color='blue',linewidth=1.0,linestyle='-')
print(avrg)
plt.show()

    

    





