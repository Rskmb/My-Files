import numpy as np
def normal_dist(x,mean,sd): 
  prob_dist=(np.pi*sd)*np.exp(-0.5*((x-mean)/sd)**2)
  return prob_dist

mean=0
sd=1
x=1
result=normal_dist(mean,sd,x)
print(result)

 
 
