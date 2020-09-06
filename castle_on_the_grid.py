import unittest

"""
Author: Dania Ismadi
Date: September 7 2020

Problem: Castle on the Grid
Link: https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

You are given a square grid with some cells open (.) and some blocked (X). Your
playing piece can move along any row or column until it reaches the edge of the
grid or a blocked cell. Given a grid, a start and an end position, determine
the number of moves it will take to get to the end position.

"""


def minimum_moves(grid, start_x, start_y, goal_x, goal_y):
    """
    Return an integer denoting the minimum moves required to get from the
    starting position (start_x, start_y) to the goal (goal_x, goal_y).

    Args:
        grid:       (list[strings]) an array of strings representing the rows
                    on the grid
        start_x:    (int) starting x value
        start_y:    (int) starting y value
        goal_x:     (int) goal x value
        goal_y:     (int) goal y value

    Returns:        (int) an integer denoting the minimum moves required to get
                    from the starting position to the goal
    """

    # 0: not visited or discovered
    # -1: discovered
    # 1: visited
    dp_visits = []

    # predecessor matrix
    dp_pre = []

    # initialise matrices
    for i in range(len(grid)):
        dp_visits.append([0] * len(grid[i]))
        dp_pre.append([None] * len(grid[i]))

    # discovered queue with initial start node
    queue = [(start_x, start_y)]
    # set position in matrix to discovered
    dp_visits[start_x][start_y] = -1

    while len(queue) > 0:
        curr_pos = queue.pop(0)
        x, y = curr_pos[0], curr_pos[1]

        # check if it is goal node
        if x == goal_x and y == goal_y:
            # break out of loop as we have found our goal node
            break

        # set position in matrix to visited
        dp_visits[x][y] = 1

        # find all possible moves

        # up direction
        for i in range(x, -1, -1):
            if grid[i][y] == "X":
                # not possible to go any further
                break
            # else, add position to discovered queue and add predecessor
            # if node is not yet visited or discovered
            if dp_visits[i][y] == 0:
                queue.append((i, y))
                dp_visits[i][y] = -1
                dp_pre[i][y] = (x, y)

        # down direction
        for i in range(x, len(grid)):
            if grid[i][y] == "X":
                break
            if dp_visits[i][y] == 0:
                queue.append((i, y))
                dp_visits[i][y] = -1
                dp_pre[i][y] = (x, y)

        # right direction
        for i in range(y, len(grid[0])):
            if grid[x][i] == "X":
                break
            if dp_visits[x][i] == 0:
                queue.append((x, i))
                dp_visits[x][i] = -1
                dp_pre[x][i] = (x, y)

        # left direction
        for i in range(y, -1, -1):
            if grid[x][i] == "X":
                break
            if dp_visits[x][i] == 0:
                queue.append((x, i))
                dp_visits[x][i] = -1
                dp_pre[x][i] = (x, y)

    # backtrack to find solution
    num_steps = 0
    pos = dp_pre[goal_x][goal_y]
    while pos:
        num_steps += 1
        pos = dp_pre[pos[0]][pos[1]]

    return num_steps


class TestCastleGrid(unittest.TestCase):
    """
    Test class for Castle on the Grid.

    """

    def test1(self):
        self.assertEqual(
            minimum_moves([".X.", ".X.", "..."], 0, 0, 0, 2),
            3
        )

    def test2(self):
        self.assertEqual(
            minimum_moves(["...", ".X.", ".X."], 2, 0, 0, 2),
            2
        )

    def test3(self):
        self.assertEqual(
            minimum_moves(["...", ".X.", ".X."], 2, 0, 2, 2),
            3
        )
