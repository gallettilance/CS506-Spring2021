from collections import defaultdict
from math import inf
import random
import csv


def plot_data(samples, centroids, clusters=None):
    """
    Plot samples and color it according to cluster centroid.
    :param samples: samples that need to be plotted.
    :param centroids: cluster centroids.
    :param clusters: list of clusters corresponding to each sample.
    """

    colors = ['blue', 'green', 'gold']
    assert centroids is not None

    if clusters is not None:
        sub_samples = []
        for cluster_id in range(centroids[0].shape[0]):
            sub_samples.append(np.array([samples[i] for i in range(samples.shape[0]) if clusters[i] == cluster_id]))
    else:
        sub_samples = [samples]

    plt.figure(figsize=(7, 5))

    for clustered_samples in sub_samples:
        cluster_id = sub_samples.index(clustered_samples)
        plt.plot(clustered_samples[:, 0], clustered_samples[:, 1], 'o', color=colors[cluster_id], alpha=0.75,
                 label='Data Points: Cluster %d' % cluster_id)

    plt.xlabel('x1', fontsize=14)
    plt.ylabel('x2', fontsize=14)
    plt.title('Plot of X Points', fontsize=16)
    plt.grid(True)

    # Drawing a history of centroid movement
    tempx, tempy = [], []
    for mycentroid in centroids:
        tempx.append(mycentroid[:, 0])
        tempy.append(mycentroid[:, 1])

    for cluster_id in range(len(tempx[0])):
        plt.plot(tempx, tempy, 'rx--', markersize=8)

    plt.legend(loc=4, framealpha=0.5)
    plt.show(block=True)


def get_centroids(samples, clusters):
    """
    Find the centroid given the samples and their cluster.

    :param samples: samples.
    :param clusters: list of clusters corresponding to each sample.
    :return: an array of centroids.
    """
    unique_cluster = []
    centroid_list = []
    i = 0
    count = 0

    for h in clusters:
        if h not in unique_cluster:
            unique_cluster.append(h)

    while i < len(unique_cluster):
        num = []
        for j in range(len(clusters)):
            if clusters[j] == unique_cluster[i]:
                num.append(samples[j])
                count = count + 1
        centroid_list.append(avg(num))
        count = 0
        i = i + 1
    return np.array(centroid_list)

def avg(coordinate):
    n = len(coordinate)
    a = sum([p[0] for p in coordinate]) / n
    b = sum([p[1] for p in coordinate]) / n
    return [a, b]




def find_closest_centroids(samples, centroids):
    clusters = []
    for h in samples:
        min_dis = float('inf')
        index = 0
        for i in range(len(centroids.tolist())):
            num = calculation1(h, centroids[i])
            if num < min_dis:
                min_dis = num
                index = i
        clusters.append(index)
    return clusters

def calculation1(a, b):
    return sum([(a - b) ** 2 for a, b in zip(a, b)]) ** 0.5



def run_k_means(samples, initial_centroids, n_iter):
    """
    Run K-means algorithm. The number of clusters 'K' is defined by the size of initial_centroids
    :param samples: samples.
    :param initial_centroids: a list of initial centroids.
    :param n_iter: number of iterations.
    :return: a pair of cluster assignment and history of centroids.
    """

    centroid_history = []
    current_centroids = initial_centroids
    clusters = []
    for iteration in range(n_iter):
        centroid_history.append(current_centroids)
        print("Iteration %d, Finding centroids for all samples..." % iteration)
        clusters = find_closest_centroids(samples, current_centroids)
        print("Recompute centroids...")
        current_centroids = get_centroids(samples, clusters)
    # print(current_centroids)
    return clusters, centroid_history


def choose_random_centroids(samples, K):
    """
    Randomly choose K centroids from samples.
    :param samples: samples.
    :param K: K as in K-means. Number of clusters.
    :return: an array of centroids.
    """
    np.random.shuffle(samples)
    centroids = samples[:K,:]
    return centroids

def k_means(samples, choose_centroid):
    K = choose_centroid
    rc = random.choice(samples)
    centroids = [rc]
    while len(centroids) < K:
        probability = []
        for point in samples:
            probability.append((distance.euclidean(rc, point))**2)
        probability = [p/sum(probability) for p in probability]
        rc = random.choices(samples, probability)[0]
        centroids.append(rc)
    return centroids


def main():
    datafile = 'kmeans-data.mat'
    mat = scipy.io.loadmat(datafile)
    samples = mat['X']
    # print(samples)
    # samples contain 300 pts, each has two coordinates

    # Choose the initial centroids
    initial_centroids = np.array([[3, 3], [6, 2], [8, 5]])
    
    # Choose the random centroids
    initial_centroids = np.array(choose_random_centroids(samples,3))
   
    initial_centroids = np.array(k_means(samples,3))
     
    plot_data(samples, [initial_centroids])
    clusters = find_closest_centroids(samples, initial_centroids)

    # you should see the output [0, 2, 1] corresponding to the
    # centroid assignments for the first 3 examples.
    # print(np.array(clusters[:3]).flatten())
    plot_data(samples, [initial_centroids], clusters)
    clusters, centroid_history = run_k_means(samples, initial_centroids, n_iter=10)
    plot_data(samples, centroid_history, clusters)

    # Let's choose random initial centroids and see the resulting
    # centroid progression plot.. perhaps three times in a row
    for x in range(3):
        clusters, centroid_history = run_k_means(samples, choose_random_centroids(samples, K=3), n_iter=10)
        plot_data(samples, centroid_history, clusters)


if __name__ == '__main__':
    random.seed(7)
    main()
