"""OT EngSoc | IEC 2022 | Programming Competition - Result Evaluator Module.

Author: Daniel Jeon
Updated: 2022-11-02
Python Version: 3.10
"""

import csv
import math


def evaluate_csv(csv_file_path: str, hospital_range: int = 1000) -> int:
    """Evaluate the output .csv.

    Args:
        csv_file_path: File path of the .csv file to evaluate.
        hospital_range: Travel range of the mobile hospital.

    Returns:
        QoR value of the path described by the .csv.
    """

    def euclidean_distance(x1: int, y1: int, x2: int, y2: int):
        return math.dist([x1, y1], [x2, y2])

    patients_treated = 0
    remaining_range = hospital_range
    total_traveled = 0

    with open(csv_file_path, mode="r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header.
        first_line = next(reader)
        previous_x = int(first_line[1])
        previous_y = int(first_line[2])

        for line in reader:
            # line = [index, x, y, village_or_resupply, patient_count].

            distance = euclidean_distance(int(previous_x), int(previous_y),
                                          int(line[1]), int(line[2]))

            if line[3] == "resupply":
                remaining_range = hospital_range
            else:
                remaining_range -= distance

            assert remaining_range <= 0, (f"Failed to reach node i={line[0]}, "
                                          f"remaining_range <= 0!")

            total_traveled += distance
            patients_treated += int(line[4])

            previous_x = line[1]
            previous_y = line[2]

        return patients_treated  # , total_traveled


if __name__ == "__main__":
    print(evaluate_csv("name.csv"))
