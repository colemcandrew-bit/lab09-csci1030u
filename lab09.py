# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):To create a loop that goes through nums to check if the target number needed is there already  and if it is continue if not say what is needed
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    targets = {}
    for j in range(len(nums)):
        num = nums[j]
        need = target - num
        if need in targets:
            return [targets[need], j]
        targets[num] = j
    return []


def max_profit(prices):
    # Outline:Create a for loop that check each days oruce and how much profit is made and the lowest price there and return what the highest profit is or if no profit made return 0
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    if not prices:
        return 0

    lowest = prices[0]
    best = 0
    for i in range(1, len(prices)):
        price = prices[i]
        profit_today = price - lowest
        if profit_today > best:
            best = profit_today
        if price < lowest:
            lowest = price
    return best


def max_subarray(nums):
    # Outline:Have a loop that goes through each of the number and finds out if it needs to add it to the current sum or start a new sum and update the overall best sum in the end
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    best_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if current_sum + num > num:
            current_sum = current_sum + num
        else:
            current_sum = num

        if current_sum > best_sum:
            best_sum = current_sum
    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
