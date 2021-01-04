import pytest

from cs506 import read

@pytest.mark.parametrize('dataset,expected', [
    (
        "tests/test_files/dataset_1.csv",
        [[138, 143], [93, 104], [61, 69], [179, 260], [48, 75], [37, 63], [29, 50], [23, 48], [30, 111], [2, 50], [38, 52], [46, 53], [71, 79], [25, 57], [298, 317], [74, 93], [50, 58], [76, 80], [381, 464], [387, 459], [78, 106], [60, 57], [507, 634], [50, 64], [77, 89], [64, 77], [40, 60], [136, 139], [243, 291], [256, 288], [94, 85], [36, 46], [45, 53], [67, 67], [120, 115], [172, 183], [66, 86], [46, 65], [121, 113], [44, 58], [64, 63], [56, 142], [40, 64], [116, 130], [87, 105], [43, 61], [43, 50], [161, 232], [36, 54]]
    ),
    (
        "tests/test_files/dataset_2.csv",
        [['JAN', 340, 360, 417], ['FEB', 318, 342, 391], ['MAR', 362, 406, 419], ['APR', 348, 396, 461], ['MAY', 363, 420, 472], ['JUN', 435, 472, 535], ['JUL', 491, 548, 622], ['AUG', 505, 559, 606], ['SEP', 404, 463, 508], ['OCT', 359, 407, 461], ['NOV', 310, 362, 390], ['DEC', 337, 405, 432]]
    ),
])
def test_read(dataset, expected):
    actual_data = read.read_csv(dataset)
    expected_data = expected

    assert len(actual_data) == len(expected_data)
    for i in range(len(actual_data)):
        assert actual_data[i] == expected_data[i]

