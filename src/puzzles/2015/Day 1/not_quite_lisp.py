from argparse import ArgumentParser
from os import path


class NotQuiteLisp:
    __instruction = {"(": 1, ")": -1}

    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "not_quite_lisp.py"
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
        input_lines = list()
        with open(self.__filepath, 'r') as inputfile:
            input_lines = inputfile.read().split('\n')
        
        results = list()
        for line in input_lines:
            floor = 0
            for character in line:
                floor += self.__instruction[character]
            results.append(floor)
        return results

    def solve_part2(self):
        input_lines = list()
        with open(self.__filepath, 'r') as inputfile:
            input_lines = inputfile.read().split('\n')
        
        results = list()
        for line in input_lines:
            floor = 0
            entered = False
            for i, character in enumerate(line, 1):
                floor += self.__instruction[character]
                if floor < 0:
                    results.append(i)
                    entered = True
                    break
            else:
                results.append(0)
        return results


if __name__ == "__main__":
    NotQuiteLisp().print_result()
