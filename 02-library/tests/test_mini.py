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
    ("/Users/jenajordahl/workspaces/CS-506-Homeworks/CS506-Spring2021/02-library/tests/test_files/dataset_3.csv")])
def test_dist(datasetPath):
    dataset = read.read_csv("/Users/jenajordahl/workspaces/CS-506-Homeworks/CS506-Spring2021/02-library/tests/test_files/dataset_3.csv")
    example = kmeans.distance(dataset[0],dataset[1])
    example_2 = kmeans.distance_squared(dataset[0],dataset[1])
    assert float("%.4f" % (example)) == 1.4142
    assert float("%.4f" % (example_2)) == 2.0

@pytest.mark.parametrize('datasetPath,expected1,expected2', [
    ("tests/test_files/dataset_1.csv",
     "tests/test_files/dataset_1_k_is_2_0.csv",
     "tests/test_files/dataset_1_k_is_2_1.csv"),
])


def test_kmeans_when_k_cost(datasetPath, expected1, expected2):
    random.seed(1)
    dataset = read.read_csv(datasetPath)
    expected_clustering1 = read.read_csv(expected1)
    expected_clustering2 = read.read_csv(expected2)
    clustering = kmeans.k_means(dataset=dataset, k=2)
    cost = kmeans.cost_function(clustering)
    assert float("%.4f" % (cost)) == 6328.3683



