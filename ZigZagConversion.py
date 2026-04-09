def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows   # store each row
    i = 0                   # current row
    step = 1                # direction (down = 1, up = -1)

    for ch in s:
        rows[i] += ch

        # change direction at top or bottom
        if i == 0:
            step = 1
        elif i == numRows - 1:
            step = -1

        i += step

    return "".join(rows)