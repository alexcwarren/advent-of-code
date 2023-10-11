from argparse import ArgumentParser
from os import path


class DoesntHeHaveInternelvesForThis:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "doesnt_he_have_internelves_for_this.py"
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

    def solve_part1(self):
        inputdata: list[str] = list()
        with open(self.__filepath, 'r') as inputfile:
            inputdata = inputfile.read().split('\n')
        print(inputdata)

        isnice_results = [False, False, False, False, False]
        return isnice_results

    def solve_part2(self):
        raise NotImplementedError


if __name__ == "__main__":
    DoesntHeHaveInternelvesForThis().print_result()
