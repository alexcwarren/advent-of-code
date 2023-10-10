from argparse import ArgumentParser
from os import path
from hashlib import md5
from sys import maxsize


class TheIdealStockingStuffer:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "the_ideal_stocking_stuffer.py"
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

    def solve_part1(self, prefix: str = '0' * 5) -> list[int]:
        inputdata = list()
        with open(self.__filepath, 'r') as inputfile:
            inputdata = inputfile.read().split('\n')

        results = list()
        for secret_key in inputdata:
            for num in range(0, maxsize):
                hash = md5(f'{secret_key}{num}'.encode())
                hexdigest = hash.hexdigest()
                if hexdigest.startswith(prefix):
                    results.append(num)
                    break

        return results

    def solve_part2(self):
        return self.solve_part1('0' * 6)


if __name__ == "__main__":
    TheIdealStockingStuffer().print_result()
