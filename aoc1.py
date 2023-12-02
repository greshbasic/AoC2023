def aoc1a():
    global sum1
    total = 0
    line_count = 0
    with open('inputs/input1.txt','r') as file:
        lines = [line for line in file]
        for line in lines:
            current_code = ""
            num_count = 0
            line_count += 1
            for character in line:
                if num_count == 2:
                    break
                if character.isnumeric():
                    current_code += character
                    num_count += 1

            if len(current_code) == 1:
                current_code *= 2
    
            total += int(current_code)
    return total
    
def aoc1b():
    global sum1
    total = 0
    i = 1
    line_count = 0
    fixed_lines_list = []
    with open('inputs/input1.txt','r') as file:
        lines = [line for line in file]
        for line in lines:
            fixed_line = lineToNumHelper(line)
            fixed_lines_list.append(fixed_line)
            print(f"line {i}: {fixed_line}")
            i += 1
        for line in fixed_lines_list:
            current_code = ""
            num_count = 0
            line_count += 1
            for character in line:
                if num_count == 2:
                    break
                if character.isnumeric():
                    current_code += character
                    num_count += 1

            if len(current_code) == 1:
                current_code *= 2
    
            total += int(current_code)
    return total


def lineToNumHelper(line):
    num_string = ""
    line_length = len(line)
    for i in range(line_length):
        remaining = line_length - i
        if remaining >= 5:
            if line[i:(i+4)] == "nine" or line[i] == "9":
                num_string += "9"
            elif line[i:(i+5)] == "eight" or line[i] == "8":
                num_string += "8"
            elif line[i:(i+5)] == "seven" or line[i] == "7":
                num_string += "7"
            elif line[i:(i+3)] == "six" or line[i] == "6":
                num_string += "6"
            elif line[i:(i+4)] == "five" or line[i] == "5":
                num_string += "5"
            elif line[i] == "4":
                num_string += "4"
            elif line[i:(i+5)] == "three" or line[i] == "3":
                num_string += "3"
            elif line[i:(i+3)] == "two" or line[i] == "2":
                num_string += "2"
            elif line[i:(i+3)] == "one" or line[i] == "1":
                num_string += "1"
                
        elif remaining >= 4:
            if line[i:(i+4)] == "nine" or line[i] == "9":
                num_string += "9"
            elif line[i] == "8":
                num_string += "8"
            elif line[i] == "7":
                num_string += "7"
            elif line[i:(i+3)] == "six" or line[i] == "6":
                num_string += "6"
            elif line[i:(i+4)] == "five" or line[i] == "5":
                num_string += "5"
            elif line[i] == "4":
                num_string += "4"
            elif line[i] == "3":
                num_string += "3"
            elif line[i:(i+3)] == "two" or line[i] == "2":
                num_string += "2"
            elif line[i:(i+3)] == "one" or line[i] == "1":
                num_string += "1"
            
        elif remaining >= 3:
            if line[i] == "9":
                num_string += "9"
            elif line[i] == "8":
                num_string += "8"
            elif line[i] == "7":
                num_string += "7"
            elif line[i:(i+3)] == "six" or line[i] == "6":
                num_string += "6"
            elif line[i] == "5":
                num_string += "5"
            elif line[i] == "4":
                num_string += "4"
            elif line[i] == "3":
                num_string += "3"
            elif line[i:(i+3)] == "two" or line[i] == "2":
                num_string += "2"
            elif line[i:(i+3)] == "one" or line[i] == "1":
                num_string += "1"

        else:
            if line[i] == "9":
                num_string += "9"
            elif line[i] == "8":
                num_string += "8"
            elif line[i] == "7":
                num_string += "7"
            elif line[i] == "6":
                num_string += "6"
            elif line[i] == "5":
                num_string += "5"
            elif line[i] == "4":
                num_string += "4"
            elif line[i] == "3":
                num_string += "3"
            elif line[i] == "2":
                num_string += "2"
            elif line[i] == "1":
                num_string += "1"
    
    return num_string

print(aoc1a())
print(aoc1b())
