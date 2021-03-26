import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import sklearn.datasets as datasets
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures

# LINE
def generate_line_data():
    centers = [[0, 0]]
    t, _ = datasets.make_blobs(n_samples=750, centers=centers, cluster_std=1, random_state=0)
    # create some space between the classes
    X = np.array(list(filter(lambda x : x[0] - x[1] < -.5 or x[0] - x[1] > .5, t)))
    Y = np.array([1 if x[0] - x[1] >= 0 else 0 for x in X])
    return X, Y

# AND
def generate_and_data():
    X = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]])
    Y = np.array([x[0] and x[1] for x in X])
    return X, Y

# OR
def generate_or_data():
    X = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]])
    Y = np.array([x[0] or x[1] for x in X])
    return X, Y

# XOR
def generate_xor_data():
    X = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]])
    Y = np.array([x[0]^x[1] for x in X])
    return X, Y

X, Y = generate_line_data()

cs = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
cs = np.hstack([cs] * 20)

plt.scatter(X[:,0],X[:,1],color=cs[Y].tolist(), s=50, alpha=0.8)
plt.show()

# for xor to be fit
# poly = PolynomialFeatures(interaction_only=True)
# lr = LogisticRegression(penalty='none', verbose=2, solver='sag')
# model = make_pipeline(poly, lr).fit(X, Y)

model = LogisticRegression(penalty='none', verbose=2, solver='sag').fit(X, Y)

# create a mesh to plot in
h = .02  # step size in the mesh
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
meshData = np.c_[xx.ravel(), yy.ravel()]

fig, ax = plt.subplots()
A = model.predict_proba(meshData)[:, 1].reshape(xx.shape)
Z = model.predict(meshData).reshape(xx.shape)
ax.contourf(xx, yy, A, cmap="RdBu", vmin=0, vmax=1)
ax.axis('off')

# Plot also the training points
T = model.predict(X)
T = T.reshape(X[:,0].shape)
ax.scatter(X[:, 0], X[:, 1], color=cs[Y].tolist(), s=50, alpha=0.9)
plt.show()
