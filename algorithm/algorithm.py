class NumberAlgorithm:
    numbers_array: []
    result_array: []

    def __init__(self):
        self.numbers_array = []
        self.result_array = []

    def get_data_from_file(self, input_path: str):
        with open(f'{input_path}') as f:
            for line in f:
                file_data = line.strip().split(" ")
            self.numbers_array = list(map(int, file_data))

    def save_data_to_file(self, output_path: str):
        textfile = open(f'{output_path}', "w")
        for element in self.result_array:
            textfile.write(str(element) + ' ')
        textfile.close()

    def get_numbers_array(self):
        return self.numbers_array

    def get_result_array(self):
        return self.result_array

    def set_numbers_array(self, numbers: []):
        self.numbers_array = numbers

    def find_pairs(self, search_sum: int = 12):
        appearance_count = dict()
        result = []
        self.result_array = []
        for i in range(0, len(self.numbers_array)):
            counter_number = search_sum - self.numbers_array[i]
            if counter_number in appearance_count and appearance_count[counter_number] > 0:
                appearance_count[counter_number] -= 1
                appearance_count[self.numbers_array[i]] = appearance_count.get(self.numbers_array[i], 0) - 1
                if counter_number > self.numbers_array[i]:
                    result.append((self.numbers_array[i], counter_number))
                else:
                    result.append((counter_number, self.numbers_array[i]))

            appearance_count[self.numbers_array[i]] = appearance_count.get(self.numbers_array[i], 0) + 1

        self.result_array = result
        return result
