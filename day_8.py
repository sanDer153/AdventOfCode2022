

def first_star():
    with open("day_8_input") as f:
        tree_grid = [list(map(int, row.strip("\n"))) for row in f]
        visible_grid = [[0 for j in range(len(tree_grid[0]))] for i in range(len(tree_grid))]
        for row in range(len(tree_grid)):
            for col in range(len(tree_grid)):
                if all(tree_grid[row][col] > tree_grid[r][col] for r in range(row)) or \
                   all(tree_grid[row][col] > tree_grid[r][col] for r in range(row + 1, len(tree_grid))) or \
                   all(tree_grid[row][col] > tree_grid[row][c] for c in range(col)) or \
                   all(tree_grid[row][col] > tree_grid[row][c] for c in range(col + 1, len(tree_grid[0]))):
                    visible_grid[row][col] = 1
                
        print(sum([sum(row) for row in visible_grid]))

def second_star():
    with open("day_8_input") as f:
        tree_grid = [list(map(int, row.strip("\n"))) for row in f]
        max_scenic_score = 0
        for row in range(1, len(tree_grid) - 1):
            for col in range(1, len(tree_grid) - 1):
                view_vect = [1, 1, 1, 1] #up, dow, left, right
                while row - (view_vect[0]+1) >= 0 and tree_grid[row - view_vect[0]][col] < tree_grid[row][col]:
                    view_vect[0] += 1
                while row + (view_vect[1]+1) < len(tree_grid) and tree_grid[row + view_vect[1]][col] < tree_grid[row][col]:
                    view_vect[1] += 1
                while col - (view_vect[2]+1) >= 0 and tree_grid[row][col - view_vect[2]] < tree_grid[row][col]:
                    view_vect[2] += 1
                while col + (view_vect[3]+1) < len(tree_grid) and tree_grid[row][col + view_vect[3]] < tree_grid[row][col]:
                    view_vect[3] += 1
                
                max_scenic_score = max(max_scenic_score, view_vect[0]*view_vect[1]*view_vect[2]*view_vect[3])
        print(max_scenic_score)

first_star()
second_star()