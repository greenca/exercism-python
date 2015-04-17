zero = [' _ ', '| |', '|_|', '   ']
one = ['   ', '  |', '  |', '   ']
two = [' _ ', ' _|', '|_ ', '   ']
three = [' _ ', ' _|', ' _|', '   ']
four = ['   ', '|_|', '  |', '   ']
five = [' _ ', '|_ ', ' _|', '   ']
six = [' _ ', '|_ ', '|_|', '   ']
seven = [' _ ', '  |', '  |', '   ']
eight = [' _ ', '|_|', '|_|', '   ']
nine = [' _ ', '|_|', ' _|', '   ']

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]


def grid(num):

    # Check for valid number
    if not num.isdigit():
        raise ValueError('Invalid number')

    grid = ['', '', '', '']
    for digit in num:
        digit_grid = numbers[int(digit)]
        for i in range(4):
            grid[i] += digit_grid[i]

    return grid
        

def number(grid):

    # Check for valid input grid
    if len(grid) != 4:
        raise ValueError('Invalid number of rows')
    rowLen = len(grid[0])
    for row in grid:
        if len(row) != rowLen:
            raise ValueError('Invalid row length')
    
    num = ''
    for i in range(0, rowLen, 3):
        element = [grid[j][i:i+3] for j in range(4)]
            
        try:
            digit = str(numbers.index(element))
        except:
            digit = '?'
        
        num += digit

    return num
