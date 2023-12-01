import util

input = util.get_input(1)

# Part 1
sum = 0

for line in input:
    cal_value = ""

    for char in line:
        if char.isdigit():
            cal_value += char
            break
    
    for char in reversed(line):
        if char.isdigit():
            cal_value += char
            break

    if len(cal_value) > 0:
        sum += int(cal_value)

print(f"Part 1: {sum}")

# Part 2
word_numbers = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

sum = 0

for line in input:
    cal_value = ""

    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            cal_value += char
            break
        else:
            matched_words = [word for word in word_numbers.keys() if line[i:].startswith(word)]

            if len(matched_words) > 0:
                cal_value += word_numbers[matched_words[0]]
                break
    
    for i in range(len(line), 0, -1):
        char = line[i - 1]
        if char.isdigit():
            cal_value += char
            break
        else:
            matched_words = [word for word in word_numbers.keys() if line[:i].endswith(word)]

            if len(matched_words) > 0:
                cal_value += word_numbers[matched_words[0]]
                break

    sum += int(cal_value)

print(f"Part 2: {sum}")