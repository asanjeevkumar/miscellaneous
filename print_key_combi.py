import sys

# Print all possible words when using a T9 keyboard
#
#   -------------------------
#   |       |  ABC  |  DEF  |
#   |   1   |   2   |   3   |
#   -------------------------
#   |  GHI  |  JKL  |  MNO  |
#   |   4   |   5   |   6   |
#   -------------------------
#   | PQRS  |  TUV  | WXYZ  |
#   |   7   |   8   |   9   |
#   -------------------------
#   |       |       |       |
#   |   *   |   0   |   #   |
#   -------------------------
#
# Given a list of keys presses generate all the possible words
# when using T9 predictive text (a press of a key can mean any of the
# characters on it).
#
# e.g. pressing 4 then 6 has 9 possible words:
#
#   gm
#   gn
#   go
#   hm
#   hn
#   ho
#   im
#   in
#   io
#
# Key mapping is provided below.
#
# Expected answers are provided when running the script as:
#
#   python words.py 43556 | sort
#   python words.py 9427 | sort
#
#



digit_keys = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def possible_words(digits, parent_char = '', parent_char_len = 0):

    count = 0
    if parent_char_len == 0:
        parent_char_len = len(digits)
    for num in digits:
        char_result  = ''
        count += 1
        data_1 = digit_keys[num]
        for char_val in data_1:
            char_result = char_val
            if parent_char:

                char_result = parent_char+char_val

            if len(digits)> count:
                char_result = possible_words(digits[count:], char_result, parent_char_len)
            if len(char_result) == parent_char_len:
                print(char_result)

    return char_result
def main():

    digits = [4,5,6,3]
    possible_words(digits)


if __name__ == "__main__":
    main()