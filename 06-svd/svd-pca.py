import numpy as np
import matplotlib.pyplot as plt

n_samples = 500
C = np.array([[0.1, 0.6], [2., .6]])
X = np.random.randn(n_samples, 2) @ C + np.array([-6, 3])
plt.axis('equal')
plt.scatter(X[:, 0], X[:, 1], s=10, alpha=0.8)
plt.title("Raw Data")
plt.show()

Xc = X - np.mean(X,axis=0)
plt.axis('equal')
plt.scatter(Xc[:, 0], Xc[:, 1], s=10, alpha=0.8, color='r')
plt.title("Mean Centered Data")
plt.show()

u, s, vt = np.linalg.svd(Xc,full_matrices=False)
plt.plot(range(1,len(s)+1),s)
plt.title("Singular Values")
plt.show()

scopy = s.copy()
scopy[1] = 0.
reducedX = u @ np.diag(scopy) @ vt
plt.axis('equal')
plt.scatter(Xc[:,0],Xc[:,1], color='r')
plt.scatter(reducedX[:,0], reducedX[:,1])
endpoints = np.array([[-10],[10]]) @ vt[[0],:]
_ = plt.plot(endpoints[:,0], endpoints[:,1], 'g-')
plt.show()

