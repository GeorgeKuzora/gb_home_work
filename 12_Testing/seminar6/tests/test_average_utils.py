from unittest.mock import patch

from pytest import raises

from src.average_utils import AverageUtils as au


class TestUnitFindAverage:
    def test_find_average(self):
        assert au.find_average([1, 2, 3]) == 2
        assert au.find_average([5]) == 5

    def test_find_average_empty_list(self):
        assert au.find_average([]) == 0

    def test_find_average_raises_on_not_list(self):
        with raises(TypeError):
            au.find_average("not list")

    def test_find_average_raises_on_not_numbers(self):
        with raises(TypeError):
            au.find_average(["a", "b"])


class TestUnitCompareAverage:

    def test_compare_average_equals(self, capsys):
        with patch.object(
            au, "find_average", side_effect=[2, 2]
        ) as mock_find_average:
            expected_output = "Средние значения равны"
            au.compare_average([1, 2, 3], [2, 2])
            captured = capsys.readouterr()
            assert captured.out.strip() == expected_output
            mock_find_average.assert_called_with([2, 2])

    def test_compare_average_greater(self, capsys):
        with patch.object(
            au, "find_average", side_effect=[2, 1.5]
        ) as mock_find_average:
            expected_output = "Первый список имеет большее среднее значение"
            au.compare_average([1, 2, 3], [2, 1])
            captured = capsys.readouterr()
            assert captured.out.strip() == expected_output
            mock_find_average.assert_called_with([2, 1])

    def test_compare_average_less(self, capsys):
        with patch.object(
            au, "find_average", side_effect=[2, 3.5]
        ) as mock_find_average:
            expected_output = "Второй список имеет большее среднее значение"
            au.compare_average([1, 2, 3], [2, 5])
            captured = capsys.readouterr()
            assert captured.out.strip() == expected_output
            mock_find_average.assert_called_with([2, 5])


class TestIntegration:
    def test_compare_average_equals(self, capsys):
        expected_output = "Средние значения равны"
        au.compare_average([1, 2, 3], [2, 2])
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    def test_compare_average_greater(self, capsys):
        expected_output = "Первый список имеет большее среднее значение"
        au.compare_average([1, 2, 3], [2, 1])
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    def test_compare_average_less(self, capsys):
        expected_output = "Второй список имеет большее среднее значение"
        au.compare_average([2, 1], [1, 2, 3])
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

    def test_compare_average_raises_on_not_list(self):
        with raises(TypeError):
            au.compare_average("not list", [1, 2, 3])

    def test_compare_average_raises_on_not_numbers(self):
        with raises(TypeError):
            au.compare_average(["a", "b"], [1, 2, 3])
