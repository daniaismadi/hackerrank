import unittest

"""
Author: Dania Ismadi
Date: September 6, 2020

Problem: Metals
Link: https://www.hackerrank.com/contests/juniper-hackathon/challenges/metals/problem

Mr. Octopus has recently shut down his factory and want to sell of his metal rods
to a local businessman.

In order to maximize profit, he should sell the metal of same size and shape. If
he sells N metal rods of length L, he receives N x L x metal_price. The remaining
smaller metal rods will be thrown away. To cut the metal rods, he needs to pay
cost_per_cut for every cut.

What is the maximum amount of money Mr.Octopus can make?

"""


def max_profit(cost_per_cut, metal_price, lengths):
    """
    Return the maximum profit Mr. Octopus can make from selling
    metal rods as specified in lengths for metal_price and with cost_per_cut
    constraint.

    :param cost_per_cut:    (int) the price to pay for every cut
    :param metal_price:     (int) the price of the metal
    :param lengths:         (list) array of integers representing the length of
                            each rod
    :return:                (int) maximum profit
    """

    max_profit = 0
    max_length = max(lengths)

    for length in range(1, max_length):
        total_cuts = 0
        total_pieces = 0

        dp = [0] * (len(lengths) + 1)
        for i in range(len(lengths)):
            curr_rod_length = lengths[i]

            num_cuts = 0
            if curr_rod_length % length != 0:
                # this means we need to cut the rod to fit the length
                num_cuts += 1
            if curr_rod_length > length:
                # we need to cut the rod as it is too long for length
                num_cuts += (curr_rod_length // length) - 1

            # calculate profit if we cut
            profit = ((total_pieces+(curr_rod_length//length))*length*metal_price) - \
                     ((total_cuts + num_cuts)*cost_per_cut)

            if dp[i] < profit:
                # this means profit is greater if we do cut
                # if dp[i] >= profit, this means it is better if we do not cut
                total_cuts += num_cuts
                total_pieces += curr_rod_length//length

            dp[i+1] = max(dp[i], profit)

        # update max_profit if needed
        curr_profit = dp[-1]
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit


class TestMetals(unittest.TestCase):
    """
    Test class for Metals.

    """

    def test1(self):
        self.assertEqual(
            max_profit(25, 1, [20, 40, 21, 20, 20, 20, 20, 20, 20]),
            155)

    def test2(self):
        self.assertEqual(
            max_profit(1, 10, [26, 103, 59]),
            1770)

    def test3(self):
        self.assertEqual(
            max_profit(100, 10, [26, 103, 59]),
            1230)
