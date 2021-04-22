# https://codeforces.com/problemset/problem/189/A

import sys
sys.setrecursionlimit(5000)


def max_ribbon_cuts(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum in memo:
            return memo[target_sum]

        if target_sum == 0:
            return []

        if target_sum < 0:
            return None

        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num

            # if remainder >= 0:
            remiander_combination = helper(remainder, numbers)

            if remiander_combination != None:
                combination = remiander_combination + [num]

                if(shortest_combination == None or len(shortest_combination) < len(combination)):
                    shortest_combination = combination

        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return helper(target_sum, numbers)


user_inputs = list(map(eval, input.split(" ")))
print(len(max_ribbon_cuts(user_inputs[0], user_inputs[1:3])))
