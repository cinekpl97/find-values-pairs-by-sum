import unittest
from algorithm import NumberAlgorithm
import pathlib as pl


class TestNumberAlgorithm(unittest.TestCase):
    '''
    Tests with array check contain statically assigned arrays (without file read) because its not necessary in those unittests
    File save is introduced in later tests
    '''

    def test_empty_input_result(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([])
        result = algorithm.find_pairs(12)
        self.assertEqual([], result)

    def test_single_element_less_than_sum_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([0])
        result = algorithm.find_pairs(12)
        self.assertEqual([], result)

    def test_single_element_equal_to_sum_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12])
        result = algorithm.find_pairs(12)
        self.assertEqual([], result)

    def test_double_element_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([0, 12])
        result = algorithm.find_pairs(12)
        self.assertEqual([(0, 12)], result)

    def test_triple_element_one_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([0, 12, 12])
        result = algorithm.find_pairs(12)
        self.assertEqual([(0, 12)], result)

    def test_triple_element_zero_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12, 12, 12])
        result = algorithm.find_pairs(12)
        self.assertEqual([], result)

    def test_long_element_zero_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12, 9, 1, 6, 4, 4, 4, 4, 12, 12])
        result = algorithm.find_pairs(12)
        self.assertEqual([], result)

    def test_long_element_one_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12, 9, 1, 6, 4, 4, 4, 4, 12, 0])
        result = algorithm.find_pairs(12)
        self.assertEqual([(0, 12)], result)

    def test_long_element_two_correct_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12, 9, 1, 6, 4, 4, 0, 12, 12, 0])
        result = algorithm.find_pairs(12)
        self.assertEqual([(0, 12), (0, 12)], result)

    def test_result_order_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([12, 0])
        result = algorithm.find_pairs(12)
        self.assertEqual([(0, 12)], result)

    def test_recrutation_example_input(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0])
        result = algorithm.find_pairs(12)
        self.assertEqual([(4, 8), (0, 12), (4, 8), (1, 11), (0, 12)], result)

    def test_check_output_exists(self):
        algorithm = NumberAlgorithm()
        algorithm.set_numbers_array([4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0])
        algorithm.save_data_to_file('algorithm\\output.txt')
        path = pl.Path("algorithm\\output.txt")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

    def test_check_input_read(self):
        algorithm = NumberAlgorithm()
        algorithm.get_data_from_file('algorithm\\input.txt')
        print(algorithm.numbers_array)
        self.assertNotEqual([], algorithm.numbers_array)


if __name__ == '__main__':
    unittest.main()
