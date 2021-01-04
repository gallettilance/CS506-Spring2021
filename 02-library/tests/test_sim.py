import pytest
import random

from cs506 import sim


def _generate_rand_point(dimension):
    return [random.randrange(1, 1000, 1) for i in range(dimension)]


def test_euclidean():
    # sanity checks
    try:
        sim.euclidean_dist([], [])
    except ValueError as e:
        assert str(e) == "lengths must not be zero"
    try:
        sim.euclidean_dist([0], [0,0])
    except ValueError as e:
        assert str(e) == "lengths must be equal"
    
    assert sim.euclidean_dist([0,0], [1,0]) == 1
    assert sim.euclidean_dist([0,0,0], [1,0,0]) == 1
    assert sim.euclidean_dist([0,0,0], [0,0,0]) == 0
    assert sim.euclidean_dist([0,0,0], [1,0,0]) == sim.euclidean_dist([1,0,0], [0,0,0])
    dimension = random.randint(1, 100)
    x = _generate_rand_point(dimension)
    # distance from a pt to itself is 0
    assert sim.euclidean_dist(x, x) == 0
    # distance is always positive
    y = _generate_rand_point(dimension)
    assert sim.euclidean_dist(x, y) >= 0
    # distance is symmetric
    assert sim.euclidean_dist(x, y) == sim.euclidean_dist(y, x)
    # triangle inequality
    z = _generate_rand_point(dimension)
    assert sim.euclidean_dist(x, y) <= sim.euclidean_dist(x, z) + sim.euclidean_dist(z, y)


def test_manhattan():
    # sanity checks
    try:
        sim.manhattan_dist([], [])
    except ValueError as e:
        assert str(e) == "lengths must not be zero"
    try:
        sim.manhattan_dist([0], [0,0])
    except ValueError as e:
        assert str(e) == "lengths must be equal"
    
    assert sim.manhattan_dist([0,0], [1,1]) == 2
    assert sim.manhattan_dist([0,0,0], [1,1,1]) == 3
    dimension = random.randint(1, 100)
    x = _generate_rand_point(dimension)
    # distance from a pt to itself is 0
    assert sim.manhattan_dist(x, x) == 0
    # distance is always positive
    y = _generate_rand_point(dimension)
    assert sim.manhattan_dist(x, y) >= 0
    # distance is symmetric
    assert sim.manhattan_dist(x, y) == sim.manhattan_dist(y, x)
    # triangle inequality
    z = _generate_rand_point(dimension)
    assert sim.manhattan_dist(x, y) <= sim.manhattan_dist(x, z) + sim.manhattan_dist(z, y)


def test_cosine():
    try:
        sim.cosine_sim([], [])
    except ValueError as e:
        assert str(e) == "lengths must not be zero"
    try:
        sim.cosine_sim([0], [0,0])
    except ValueError as e:
        assert str(e) == "lengths must be equal"
    
    assert sim.cosine_sim([1,0], [1,0]) == 1
    assert sim.cosine_sim([0,1,0], [1,0,0]) == 0


def test_jaccard():
    # sanity checks
    try:
        sim.jaccard_dist([], [])
    except ValueError as e:
        assert str(e) == "lengths must not be zero"
    
    assert sim.jaccard_dist([0,0], [1,0]) == .5
    assert sim.jaccard_dist([0,0,0], [1,1,1]) == 1
    dimension = random.randint(1, 100)
    x = _generate_rand_point(dimension)
    # distance from a pt to itself is 0
    assert sim.jaccard_dist(x, x) == 0
    # distance is always positive
    y = _generate_rand_point(dimension)
    assert sim.jaccard_dist(x, y) >= 0
    # distance is symmetric
    assert sim.jaccard_dist(x, y) == sim.jaccard_dist(y, x)
    # triangle inequality
    z = _generate_rand_point(dimension)
    assert sim.jaccard_dist(x, y) <= sim.jaccard_dist(x, z) + sim.jaccard_dist(z, y)

