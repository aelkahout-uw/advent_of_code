import re

def part_one(lines):

    total = 0

    for line in lines:
        flag = True
        for game in line.split(';'):
            blue = re.findall(r'(\d+)\s+blue', game)
            blue.append(0)
            green = re.findall(r'(\d+)\s+green', game)
            green.append(0)
            red = re.findall(r'(\d+)\s+red', game)
            red.append(0)
            game_number = re.findall(r'Game\s(\d+):',line)[0]

            if int(blue[0]) > 14 or int(red[0]) > 12 or int(green[0]) > 13:
                flag = False

        if flag:
            total += int(game_number)
    
    return total

def part_two(lines):
    total = 0

    for line in lines:

        blue = re.findall(r'(\d+)\s+blue', line)
        red = re.findall(r'(\d+)\s+red', line)
        green = re.findall(r'(\d+)\s+green', line)

        max_blue = max(int(x) for x in blue)
        max_red = max(int(x) for x in red)
        max_green = max(int(x) for x in green)

        total += (max_blue * max_red * max_green)

    return total

def main():

    for file_name in ['Example','Input']:
        with open(file_name.lower() + '.txt','r') as file:
            lines = file.read().splitlines()

        for line in lines:

            blue = re.findall(r'(\d+)\s+blue', line)
            red = re.findall(r'(\d+)\s+red', line)
            green = re.findall(r'(\d+)\s+green', line)    

        print(f'Day 3 - Part one | {file_name} result: {part_one(lines)}')
        print(f'Day 3 - Part two | {file_name} result: {part_two(lines)}')

if __name__ == "__main__":
    main()
