from argparse import ArgumentParser
from os import path


class Trebuchet:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "trebuchet!.py"
        self.is_part1: bool = is_part1

        # Look for command-line args if no filepath provided
        if filepath is None:
            parser = ArgumentParser(
                prog=prog_name,
                usage=f"python {prog_name} -f <filepath> -p <partnumber>",
            )
            parser.add_argument("-f", "--filepath")
            parser.add_argument("-p", "--partnumber", choices=["1", "2"], default="1")
            args = parser.parse_args()
            filepath = args.filepath
            self.is_part1 = args.partnumber == "1"

        if filepath is None:
            print("ERROR: filepath not provided.")
            exit()
        elif not path.isfile(filepath):
            print('ERROR: "{filepath}" does not exist.')
            exit()
        else:
            self.__filepath: str = filepath

    def print_result(self):
        if self.is_part1:
            print(f"{self.solve_part1()}")
        else:
            print(f"{self.solve_part2()}")

    def solve_part1(self) -> int:
        lines: list[str]
        with open(self.__filepath) as inputfile:
            lines = inputfile.read().split()

        total_sum_first_last: int = 0
        for line in lines:
            from re import findall
            digits = findall(r'\d', line)
            sum_first_last = int(digits[0] + digits[-1])
            total_sum_first_last += sum_first_last

        return total_sum_first_last

    def solve_part2(self) -> int:
        lines: list[str] = []
        with open(self.__filepath) as inputfile:
            lines = inputfile.read().lower().split()

        numbers: dict[str,int] = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

        from re import findall
        total_sum_first_last: int = 0
        for line in lines:
            print(line)
            digits = findall(r'\d', line)
            print(digits)
            print()

        return total_sum_first_last


if __name__ == "__main__":
    Trebuchet().print_result()
