# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
Problem #1
https://www.hackerrank.com/challenges/python-loops/problem
"""


def print_squares(limit):
    square_list = [str(n ** 2) for n in range(limit)]
    print("\n".join(square_list))


"""
Problem #2
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""


def list_of_coordinates(x, y, z, n):
    coordinates = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n]
    print(coordinates)



"""
Problem #3
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


def print_runner_up(list_numbers):
    sorted_list = sorted(list(set(list_numbers)), reverse=True)
    print(sorted_list[1])


"""
Problem #4
https://www.hackerrank.com/challenges/word-order/problem
"""


def print_word_occ_order():
    n = int(input())
    occ_dict = dict()
    for _ in range(n):
        word = input().strip()
        if word in occ_dict:
            occ_dict[word] += 1
        else:
            occ_dict[word] = 1

    occ_numb = [str(occ) for occ in occ_dict.values()]
    print(f'{len(occ_dict)}\n{" ".join(occ_numb)}')


if __name__ == '__main__':
    # print_squares(5)
    # print_runner_up([2, 3, 6, 6, 5])
    # print_word_occ_order()
    list_of_coordinates(1, 1, 1, 2)
