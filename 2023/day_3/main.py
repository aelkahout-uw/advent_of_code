def has_digits_around(matrix, row, col):

    indices = []

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if matrix[i][j].isdigit():
                    indices.append((i,j))
    
    return indices

def find_symbol_indices(matrix, symbols):
    rows = []
    cols = []

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element in symbols:
                rows.append(i)
                cols.append(j)
    
    return rows,cols

def get_consecutive_numbers(matrix, row, col):
    
    if 0 <= col < len(matrix[0]):

        start_index = col
        end_index = col
        
        while start_index > 0 and str(matrix[row][start_index - 1]).isdigit():
            start_index -= 1

        while end_index < len(matrix[0]) - 1 and str(matrix[row][end_index+1]).isdigit():
            end_index += 1

        result = ''.join(str(matrix[row][i]) for i in range(start_index, end_index + 1))

        if result.isdigit():
            return int(result)
        
def filter_list(tuples_to_filter):
    result = []
    for x, y in tuples_to_filter:
        if (x, y+1) not in tuples_to_filter:

            result.append((x,y))

    return result

def part_one(arr, symbol_rows, symbol_cols):

    total = 0

    for i in range(len(symbol_rows)):
        indices_to_check = has_digits_around(arr, symbol_rows[i], symbol_cols[i])
        filtered_list = filter_list(indices_to_check)
        
        for e in filtered_list:
            if has_digits_around(arr, symbol_rows[i], symbol_cols[i]):
                total += get_consecutive_numbers(arr,e[0],e[1])
        
    return total

def part_two(arr, symbol_rows, symbol_cols):

    total = 0

    for i in range(len(symbol_rows)):
        indices_to_check = has_digits_around(arr, symbol_rows[i], symbol_cols[i])
        filtered_list = filter_list(indices_to_check)
        
        if len(filtered_list) == 2:
            product = get_consecutive_numbers(arr,filtered_list[0][0],filtered_list[0][1]) * get_consecutive_numbers(arr,filtered_list[1][0],filtered_list[1][1])
            total += product
        
    return total

def main():
    
    for file_name in ['Example','Input']:
        with open(file_name.lower() + '.txt','r') as file:
            lines = file.read()

        all_symbols = ''.join(set(char for char in lines if char not in '.0123456789\n'))

        arr = []
        for line in lines.splitlines():
            arr.append(list(line))

        symbol_rows, symbol_cols = find_symbol_indices(arr,all_symbols)
        
        print(f'Day 3 - Part one | {file_name} result: {part_one(arr, symbol_rows, symbol_cols)}')
        print(f'Day 3 - Part two | {file_name} result: {part_two(arr, symbol_rows, symbol_cols)}')

if __name__ == "__main__":
    main()