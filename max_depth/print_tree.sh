# 1: 0
echo -e "1"

#BASE
# 1: 1
# 2: 0 1
echo -e " 1\n2 3"

# 1: 4 = 2*(1+1) for 3 levels
# 2: 1 5
# 3: 0 1 3 1
echo -e "    1\n 2     3\n4 5   6 7"

# 1: 10 = 2*(2*(1+1)+1) for 4 levels
# 2: 4 11
# 3: 1 5 5 5
# 4: 0 1 3 1 3 1 3 1
echo -e "          1\n    2           3\n 4     5     6     7\n8 9   8 7   6 5   4 3"

# 1: 22 = 2*(2*(2*(1+1)+1)+1) for 5 levels
# 2: 10 23
# 3: 4 11 11 11
# 4: 1 5 5 5 5 5 5 5
# 5: 0 1 3 1 3 1 3 1 3 1 3 1 3 1 3 1
echo -e "                      1\n          2                       3\n    4           5           6           7\n 8     9     8     7     6     5     4     3\n1 2   3 4   5 6   7 8   1 2   3 4   5 6   7 8"
