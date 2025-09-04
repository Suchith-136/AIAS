import pytest
from task_2 import assign_grade

@pytest.mark.parametrize("score,expected", [
    (100, "A"),
    (90, "A"),
    (89, "B"),
    (80, "B"),
    (79, "C"),
    (70, "C"),
    (69, "D"),
    (60, "D"),
    (59, "F"),
    (0, "F"),
    (50, "F"),
])
def test_assign_grade_valid_scores(score, expected):
    assert assign_grade(score) == expected

@pytest.mark.parametrize("score", [-1, -5, 101, 105])
def test_assign_grade_invalid_numeric(score):
    with pytest.raises(ValueError):
        assign_grade(score)

@pytest.mark.parametrize("score", ["eighty", None, [], {}])
def test_assign_grade_invalid_type(score):
    with pytest.raises(TypeError):
        assign_grade(score)