with open("input", "r", encoding="utf8") as f:
    lines = f.readlines()

puzzle = [[i for i in line.strip()] for line in lines]


def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY


def findWordInDirection(grid, n, m, word, index, x, y, dirX, dirY):
    if index == len(word):
        return True

    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(
            grid, n, m, word, index + 1, x + dirX, y + dirY, dirX, dirY
        )

    return False


def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    # Directions for 8 possible movements
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    for i in range(n):
        for j in range(m):

            # Check if the first character matches
            if grid[i][j] == word[0]:
                for dirX, dirY in directions:
                    if findWordInDirection(
                        grid, n, m, word, 0, i, j, dirX, dirY
                    ):
                        ans.append([i, j])
                        # break

    return ans


word_locations = searchWord(puzzle, "XMAS")

number_of_words = len(word_locations)

print(f"Number of XMAS's found: {number_of_words}")

# Part 2


def check_diag(grid, n, m, diag, x, y):
    # check that the diagonal is valid and get the point values
    points = []
    for point in diag:
        if not isValid(x + point[0], y + point[1], n, m):
            return False
        points.append(grid[x + point[0]][y + point[1]])

    if points == ["M", "S"] or points == ["S", "M"]:
        return True
    return False


def search_for_xmas(grid):
    ans = []
    n = len(grid)
    m = len(grid[0])

    # Directions for 8 possible movements
    directions = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                if check_diag(grid, n, m, directions[0], i, j) and check_diag(
                    grid, n, m, directions[1], i, j
                ):
                    ans.append([i, j])
    return ans


xmas_locations = search_for_xmas(puzzle)
number_of_xmas = len(xmas_locations)

print(f"Number of X-MAS's found: {number_of_xmas}")
