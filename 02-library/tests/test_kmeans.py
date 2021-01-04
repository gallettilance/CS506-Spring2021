import pytest
import random

from cs506 import kmeans,read


def clustered_all_points(clustering, dataset):
    points = []
    for assignment in clustering:
        points += clustering[assignment]
    for point in points:
        if point not in dataset:
            return False
    return True


@pytest.mark.parametrize('datasetPath', [
    ("tests/test_files/dataset_1.csv"),
])
def test_kmeans_when_k_is_1(datasetPath):
    random.seed(1)
    dataset = read.read_csv(datasetPath)
    expected_clustering = dataset
    clustering = kmeans.k_means(dataset=dataset, k=1)

    assert len(clustering.keys()) == 1
    assert clustered_all_points(clustering, dataset) is True

    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering]


@pytest.mark.parametrize('datasetPath,expected1,expected2', [
    ("tests/test_files/dataset_1.csv",
     "tests/test_files/dataset_1_k_is_2_0.csv",
     "tests/test_files/dataset_1_k_is_2_1.csv"),
])
def test_kmeans_when_k_is_2(datasetPath, expected1, expected2):
    random.seed(1)
    dataset = read.read_csv(datasetPath)
    expected_clustering1 = read.read_csv(expected1)
    expected_clustering2 = read.read_csv(expected2)
    clustering = kmeans.k_means(dataset=dataset, k=2)
    cost = kmeans.cost_function(clustering)

    for _ in range(10):
        new_clustering = kmeans.k_means(dataset=dataset, k=2)
        new_cost = kmeans.cost_function(clustering)
        if new_cost < cost:
            clustering = new_clustering
            cost = new_cost


    assert len(clustering.keys()) == 2
    assert clustered_all_points(clustering, dataset) is True
    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering1, expected_clustering2]


@pytest.mark.parametrize('datasetPath,expected1,expected2,expected3', [
    ("tests/test_files/dataset_1.csv",
     "tests/test_files/dataset_1_k_is_3_0.csv",
     "tests/test_files/dataset_1_k_is_3_1.csv",
     "tests/test_files/dataset_1_k_is_3_2.csv"),
])
def test_kmeans_when_k_is_3(datasetPath, expected1, expected2, expected3):
    random.seed(1)
    dataset = read.read_csv(datasetPath)
    expected_clustering1 = read.read_csv(expected1)
    expected_clustering2 = read.read_csv(expected2)
    expected_clustering3 = read.read_csv(expected3)
    clustering = kmeans.k_means(dataset=dataset, k=3)
    cost = kmeans.cost_function(clustering)

    for _ in range(10):
        new_clustering = kmeans.k_means(dataset=dataset, k=3)
        new_cost = kmeans.cost_function(clustering)
        if new_cost < cost:
            clustering = new_clustering
            cost = new_cost

    assert len(clustering.keys()) == 3
    assert clustered_all_points(clustering, dataset) is True
    
    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering1, expected_clustering2, expected_clustering3]
