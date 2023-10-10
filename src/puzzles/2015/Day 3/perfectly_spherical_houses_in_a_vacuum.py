from argparse import ArgumentParser
from os import path


class PerfectlySphericalHousesInAVacuum:
    movements = {
        '^': (0, 1),
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, -1)
    }

    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "perfectly_spherical_houses_in_a_vacuum.py"
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

    def solve_part1(self) -> list[int]:
        directions = list()
        with open(self.__filepath, 'r') as inputfile:
            directions_data = inputfile.read().split('\n')

        totals_visited = list()
        for directions in directions_data:
            visited_coordinates = set()
            pos = (0, 0)
            visited_coordinates.add(pos)
            for direction in directions:
                movement = self.movements[direction]
                x_pos = pos[0] + movement[0]
                y_pos = pos[1] + movement[1]
                pos = (x_pos, y_pos)
                visited_coordinates.add(pos)
            totals_visited.append(len(visited_coordinates))

        return totals_visited

    def solve_part2(self):
        raise NotImplementedError


if __name__ == "__main__":
    PerfectlySphericalHousesInAVacuum().print_result()
