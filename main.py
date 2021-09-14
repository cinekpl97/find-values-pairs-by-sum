from algorithm.algorithm import NumberAlgorithm


def main():
    algorithm = NumberAlgorithm()
    algorithm.get_data_from_file('algorithm/input.txt')
    algorithm.find_pairs(12)
    print(algorithm.result_array)
    algorithm.save_data_to_file('algorithm/output.txt')


if __name__ == "__main__":
    main()
