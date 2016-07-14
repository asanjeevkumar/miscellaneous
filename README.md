# miscellaneous
challenges miscellaneous code scripts
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
