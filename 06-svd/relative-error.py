import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('data/AbileneFlows/odnames','r') as f:
    odnames = [line.strip() for line in f]
dates = pd.date_range('9/1/2003',freq='10min',periods=1008)
Atraf = pd.read_table('data/AbileneFlows/X',sep='  ',header=None,names=odnames,engine='python')
Atraf.index = dates
print(Atraf.shape)

print("rank of our matrix is ", np.linalg.matrix_rank(Atraf))

u,s,vt = np.linalg.svd(Atraf)

fig = plt.figure(figsize=(6,4))
plt.plot(range(1,1+len(s)),s)
plt.xlabel(r'$k$',size=20)
plt.ylabel(r'$\sigma_k$',size=20)
_ = plt.title(r'Singular Values of $A$',size=20)
plt.show()

fig = plt.figure(figsize=(6,4))
Anorm = np.linalg.norm(Atraf)
plt.plot(range(1,21),s[0:20]/Anorm)
plt.xlim([0,20])
plt.xlabel(r'$k$',size=20)
_ = plt.ylabel(r'$\sigma_k$',size=20)
plt.show()

fig = plt.figure(figsize=(6,4))
Anorm = np.linalg.norm(Atraf)
err = np.cumsum(s[::-1]**2)
err = np.sqrt(err[::-1])
plt.plot(range(1,21),err[:20]/Anorm)
plt.xlim([0,20])
plt.xlabel(r'$k$',size=16)
plt.ylabel(r'relative F-norm error',size=16)
_ = plt.title(r'Relative Error of rank-$k$ approximation to $A$',size=16)
plt.show()


