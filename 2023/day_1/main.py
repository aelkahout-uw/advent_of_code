import re

def part_one(lines):
    
    total = 0

    for line in lines:
        a, *_, b = re.findall(r"\d", line * 2)
        total += int(a+b)

    return total

def part_two(lines):
    
    total = 0

    digits_mapping = {'one':'1',
                  'two':'2',
                  'three':'3',
                  'four':'4',
                  'five':'5',
                  'six':'6',
                  'seven':'7',
                  'eight':'8',
                  'nine':'9',
                  'zero':'0',
                  '1':'1',
                  '2':'2',
                  '3':'3',
                  '4':'4',
                  '5':'5',
                  '6':'6',
                  '7':'7',
                  '8':'8',
                  '9':'9',
                  '0':'0'}

    pattern = '0|zero|1|one|2|two|3|three|4|four|5|five|6|six|7|seven|8|eight|9|nine'
    
    for line in lines:
        a, *_, b = re.findall(rf"(?=({pattern}))", line * 2)
        total += int(digits_mapping[a] + digits_mapping[b])

    return total

def main():

    for file_name in ['Example','Input']:
        for game_part in ['_one','_two']:
            with open(file_name.lower() + game_part.lower() + '.txt','r') as file:
                lines = file.read().splitlines()

            if game_part == '_one':
                print(f'Day 3 - Part one | {file_name+game_part} result: {part_one(lines)}')
            else:
                print(f'Day 3 - Part two | {file_name+game_part} result: {part_two(lines)}')

if __name__ == "__main__":
    main()