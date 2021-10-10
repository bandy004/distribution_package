from distribution import Distribution


def test_mean():
    distribution = Distribution()
    distribution.data = [2, 4, 5, 6, 7, 8, 19, 20, 32, 2, 3, 7, 8]
    assert(distribution.mean == 0.0)


def test_stddev():
    distribution = Distribution()
    distribution.data = [2, 4, 5, 6, 7, 8, 19, 20, 32, 2, 3, 7, 8]
    assert(distribution.stddev == 0.0)
