
def part_one(lines):

    total = 0
    for line in lines:
        count = 0
        winning_numbers = line.replace('  ', ' ').replace(' | ', ':').replace(': ', ':').split('|')[0].split(':')[1].split(' ')
        numbers_we_have = line.replace('  ', ' ').replace(' | ', '|').split('|')[1].split(' ')

        for number in winning_numbers:
            if number in numbers_we_have:
                count += 1
        
        if count > 0:
            total += 2**(count-1)
    
    return total

def part_two(lines):

    my_list = [1 for _ in range(len(lines))]

    for line in lines:
        count = 0
        card_number = int(line.replace('  ',' ').replace('  ',' ').split(':')[0].split(' ')[1])
        winning_numbers = line.replace('  ', ' ').replace(' | ', ':').replace(': ', ':').split('|')[0].split(':')[1].split(' ')
        numbers_we_have = line.replace('  ', ' ').replace(' | ', '|').split('|')[1].split(' ')

        for number in winning_numbers:
            if number in numbers_we_have:
                count += 1

        for s in range(my_list[card_number-1]):
            for i in range(count):
                my_list[card_number + i] += 1
    
    return sum(my_list)


def main():

    for file_name in ['Example','Input']:
        with open(file_name.lower() + '.txt','r') as file:
            lines = file.read().splitlines()

        print(f'Day 4 - Part one | {file_name} result: {part_one(lines)}')
        print(f'Day 4 - Part two | {file_name} result: {part_two(lines)}')

if __name__ == "__main__":
    main()