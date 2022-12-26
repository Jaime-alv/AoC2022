import pathlib
import unittest
import string

example = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def divide(input_string: str) -> tuple[str, str]:
    half: int = int(len(input_string) / 2)
    result: tuple[str, str] = input_string[:half], input_string[half:]
    return result


def filter_string(tuple_in: tuple[str, str]) -> str:
    first: str = tuple_in[0]
    second: str = tuple_in[1]
    return list(filter(lambda x: x in second, first))[0]


def find_by_index(char: str) -> int:
    abc = string.ascii_letters
    return abc.index(char) + 1


def add_items(data: list[str]) -> int:
    result = 0
    for element in data:
        result += find_by_index(filter_string(divide(element)))
    return result


def split_in_groups(data: list[str]) -> list[tuple[str, str, str]]:
    result = []
    for index in range(0, len(data) - 1, 3):
        group: tuple[str, str,
                     str] = data[index], data[index + 1], data[index + 2]
        result.append(group)
    return result


def load_file(file: pathlib.Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


def element_in_all_rucksack(data: tuple[str, str, str]) -> str:
    first = data[0]
    second = data[1]
    third = data[2]
    return list(filter(lambda x: x in second and x in third, first))[0]


def part2(data: list[str]) -> int:
    result = 0
    formed_data: list[tuple[str, str, str]] = split_in_groups(data)
    for element in formed_data:
        char = element_in_all_rucksack(element)
        index = find_by_index(char)
        result += index
    return result


class TestDay3(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide('vJrwpWtwJgWrhcsFMMfFFhFp'),
                         ('vJrwpWtwJgWr', 'hcsFMMfFFhFp'))
        self.assertEqual(divide('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),
                         ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'))

    def test_filter_char(self):
        self.assertEqual(filter_string(('vJrwpWtwJgWr', 'hcsFMMfFFhFp')), "p")
        self.assertEqual(filter_string(
            divide("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")), "L")

    def test_find_index(self):
        self.assertEqual(find_by_index("p"), 16)
        self.assertEqual(find_by_index("L"), 38)
        self.assertEqual(find_by_index("v"), 22)
        self.assertEqual(find_by_index("r"), 18)
        self.assertEqual(find_by_index("Z"), 52)

    def test_example(self):
        self.assertEqual(add_items(example), 157)

    def test_split(self):
        self.assertEqual(split_in_groups(example), [("vJrwpWtwJgWrhcsFMMfFFhFp",
                                                     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                                                     "PmmdzqPrVvPwwTWBwg"),
                                                    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                                                     "ttgJtRGJQctTZtZT",
                                                     "CrZsJsPPZsGzwwsLwLmpwMDw")])

    def test_rucksacks(self):
        self.assertEqual(element_in_all_rucksack(("vJrwpWtwJgWrhcsFMMfFFhFp",
                                                  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                                                  "PmmdzqPrVvPwwTWBwg")), "r")
        self.assertEqual(element_in_all_rucksack(("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                                                  "ttgJtRGJQctTZtZT",
                                                  "CrZsJsPPZsGzwwsLwLmpwMDw")), "Z")


if __name__ == '__main__':
    input_data: pathlib.Path = pathlib.Path("./day3/input.txt")
    # print(add_items(load_file(input_data)))
    print(part2(load_file(input_data)))
    unittest.main(verbosity=2)
