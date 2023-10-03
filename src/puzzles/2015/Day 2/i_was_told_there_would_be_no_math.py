from argparse import ArgumentParser
from os import path


class IWasToldThereWouldBeNoMath:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "i_was_told_there_would_be_no_math.py"
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

    @staticmethod
    def surface_area(width: int, length: int, height: int) -> int:
        return 2 * (width * length + length * height + height * width)

    def solve_part1(self) -> list[int]:
        input_lines: list[str] = list()
        with open(self.__filepath, "r") as inputfile:
            input_lines = inputfile.read().split("\n")

        results = list()
        for line in input_lines:
            width, length, height = [int(d) for d in line.split("x")]
            results.append(
                self.surface_area(width, length, height)
                + min(width * length, length * height, height * width)
            )
        return results

    def solve_part2(self):
        raise NotImplementedError


if __name__ == "__main__":
    IWasToldThereWouldBeNoMath().print_result()
