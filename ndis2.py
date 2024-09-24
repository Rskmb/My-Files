import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
Mean=100;
sd=4
size=100000
values=np.random.normal(Mean,sd,size)
mp.hist(values,100)
mp.axvline(values.mean(),color='k',linestyle='dashed',linewidth=2)
mp.show()
