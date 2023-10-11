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

    def is_nice1(self, text: str) -> bool:
        return (
            self.has_3_vowels(text)
            and self.has_repeat(text)
            and not self.has_forbidden_pairs(text)
        )

    def has_3_vowels(self, text: str) -> bool:
        return self.has_vowels(text, 3)

    def has_vowels(self, text: str, num_vowels: int = 1) -> bool:
        vowel_count = 0
        for ch in text.lower():
            if ch in "aeiou":
                vowel_count += 1
            if vowel_count >= num_vowels:
                return True
        return False

    def has_repeat(self, text: str) -> bool:
        for ch1, ch2 in zip(text[:-1], text[1:]):
            if ch1 == ch2:
                return True
        return False

    def has_forbidden_pairs(self, text: str) -> bool:
        forbidden_pairs = ["ab", "cd", "pq", "xy"]
        for pair in forbidden_pairs:
            if pair in text:
                return True
        return False

    def solve_part1(self) -> int:
        inputdata: list[str] = list()
        with open(self.__filepath, "r") as inputfile:
            inputdata = inputfile.read().split("\n")

        num_isnice = 0
        for string in inputdata:
            if self.is_nice1(string):
                num_isnice += 1
        return num_isnice

    def is_nice2(self, text: str) -> bool:
        return self.has_repeating_pairs(text) and self.has_bisected_pair(text)
    
    def has_repeating_pairs(self, text: str) -> bool:
        return False

    def has_bisected_pair(self, text: str) -> bool:
        return False

    def solve_part2(self) -> int:
        inputdata: list[str] = list()
        with open(self.__filepath, 'r') as inputfile:
            inputdata = inputfile.read().split('\n')

        num_nice_strings = 0
        for string in inputdata:
            if self.is_nice2(string):
                num_nice_strings += 1

        return num_nice_strings


if __name__ == "__main__":
    DoesntHeHaveInternelvesForThis().print_result()
