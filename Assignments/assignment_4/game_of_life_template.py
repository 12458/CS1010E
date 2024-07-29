import random


def print_society(society: list) -> None:
    """
    Pretty prints a given society.

    Parameters:
        society (list): The society to be printed.
    """
    print("\n".join([" ".join(row) for row in society]))


def build_society(m: int, n: int) -> list:
    """
    Builds an m by n society randomly assigned with * and -

    Parameters:
        m (int): The number of rows of the society.
        n (int): The number of columns of the society.

    Returns:
        the resulting randomly built society.
    """
    choices = ["-", "*"]
    return [[random.choice(choices) for _ in range(n)] for _ in range(m)]


def model_society(txt) -> list[list]:
    """
    txt is a multi-line strin
    """
    lines = txt.replace(" ", "").strip().split("\n")
    return [list(line.strip()) for line in lines if len(line) > 0]


def gol(cell_value: bool, live_neigh: int) -> bool:
    if cell_value:  # If the cell is currently alive
        if live_neigh < 2 or live_neigh > 3:
            return False  # Dies due to loneliness or overcrowding
        else:
            return True  # Survives
    else:  # If the cell is currently dead
        if live_neigh == 3:
            return True  # Becomes alive due to reproduction
        else:
            return False  # Stays dead


def tabulate(rules):
    """
    rules : a functional representation of Game of Life rules
    """
    results = []
    for current_value in ["live", "dead"]:
        neighbor_results = []
        for live_neighbors in range(9):  # 0 to 8 neighbors
            result = rules(True if current_value == "live" else False, live_neighbors)
            neighbor_results.append("live" if result else "dead")
        results.append((current_value, neighbor_results))
    return results


def destiny(society: list, coordinates: tuple, gol) -> str:
    """
    Determines the liveliness of the cell in coordinates in the next generation.

    Parameters:
        society      (list): The society.
        coordinates (tuple): The tuple representing the coordinates whose
                             destiny is to be determined.
        gol                : The function representing Game of Life rules
    Returns:
        the cell's destiny.
    """
    row, col = coordinates
    rows, cols = len(society), len(society[0])

    # Get current state of the cell
    current_state = society[row][col] == "*"

    # Count live neighbors
    live_neighbors = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and society[i][j] == "*":
                live_neighbors += 1

    # Apply game of life rules
    next_state = gol(current_state, live_neighbors)

    # Return the result
    return "*" if next_state else "-"


def evolve(society, n, gol) -> tuple:
    """
    Evolves the society by n iterations given the rules in Game Of Life.

    Parameters:
        society (list): The society to be evolved.
        n        (int): The number of evolutions to perform.
        gol           : The function representing Game of Life rules
    Returns:
        a tuple consisting of the
            (1) resulting society
            (2) number of evolutions before arriving at stability.
    """
    rows, cols = len(society), len(society[0])
    current_society = [
        row[:] for row in society
    ]  # Create a deep copy of the input society

    for iteration in range(n):
        next_society = [[""] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                next_society[i][j] = destiny(current_society, (i, j), gol)

        if next_society == current_society:
            return (next_society, iteration)

        current_society = next_society

    return (current_society, n)


def migrate(society: list) -> list:
    """
    Causes a society to migrate based on the population census.

    Parameters:
        society (list): The given society.

    Returns:
        the resulting society after migration.
    """
    # Count live cells in each row and create a list of tuples
    row_data = []
    for i, row in enumerate(society):
        census = row.count("*")
        row_data.append((i, census, row))

    # Sort the rows based on census in descending order
    # The negative sign before census ensures descending order
    # The original index i is used as a tie-breaker to maintain relative order
    sorted_rows = sorted(row_data, key=lambda x: (-x[1], x[0]))

    # Create the new society with sorted rows
    new_society = [row for _, _, row in sorted_rows]

    return new_society


def main(m=5, n=6, num_of_evolutions=10, gol=gol):

    # ======= DO NOT EDIT THE CODE SNIPPETS BEYOND THIS POINT ========
    # (1) Build a random society of m by n.
    society = build_society(m, n)
    print("Initial Society:")
    print_society(society)

    # (2) Evolve the society for num_of_evolution iterations.
    result, num_evolutions_to_stability = evolve(society, num_of_evolutions, gol)
    print("After {} evolutions, resulting society:".format(num_of_evolutions))
    print_society(result)
    print("Number of evolutions to achieve stability:", num_evolutions_to_stability)

    # (3) Perform migration on the society.
    after_migration = migrate(result)
    print("Resulting society after migration:")
    print_society(after_migration)


if __name__ == "__main__":
    main()
