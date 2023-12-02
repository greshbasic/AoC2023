def aoc2a():
    lines_stripped = []
    games_dict = {}
    elf_bag = [12,13,14]
    id_sum = 0
   
    with open('inputs/input2.txt','r') as file:
        lines = [line for line in file]
        
    for line in lines:
        lines_stripped.append(line.strip())
    
    for line in lines_stripped:

        for i in range(len(line)):
            if line[i] == " ":
                
                for j in range(i+1, len(line)):
                    if line[j] == ":":
                        curr_game_data = line[j+1:]
                        curr_game_num = int(line[i+1:j])
                break
            
        elf_handful = [0,0,0]
        
        skip_next = False
        for i in range(len(curr_game_data)):
            if curr_game_data[i] == ";":
                if elf_handful[0] > elf_bag[0] or elf_handful[1] > elf_bag[1] or elf_handful[2] > elf_bag[2]:
                    break
                else:
                    elf_handful = [0,0,0]
            else:
                if skip_next:
                    skip_next = False
                    continue
                if curr_game_data[i].isnumeric():
                    if not curr_game_data[i+1].isnumeric():
                        if curr_game_data[i+2] == "r":
                            elf_handful[0] += int(curr_game_data[i])
                        elif curr_game_data[i+2] == "g":
                            elf_handful[1] += int(curr_game_data[i])
                        elif curr_game_data[i+2] == "b":
                            elf_handful[2] += int(curr_game_data[i])
                    else:
                        if curr_game_data[i+3] == "r":
                            elf_handful[0] += int(curr_game_data[i:i+2])
                            skip_next = True
                        elif curr_game_data[i+3] == "g":
                            elf_handful[1] += int(curr_game_data[i:i+2])
                            skip_next = True
                        elif curr_game_data[i+3] == "b":
                            elf_handful[2] += int(curr_game_data[i:i+2])
                            skip_next = True
                        
        if elf_handful[0] > elf_bag[0] or elf_handful[1] > elf_bag[1] or elf_handful[2] > elf_bag[2]:
            pass
        else:
            id_sum += curr_game_num

    return id_sum
    
def aoc2b():
    
    # find max r g and b from each game
    # multiply r * g * b
    # add that to power
    
    power = 0
    return power

if __name__ == "__main__":
    print(f"Part 1: {aoc2a()}")
    print(f"Part 2: {aoc2b()}")