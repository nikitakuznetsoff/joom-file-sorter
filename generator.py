import sys
import random


def generate_line(max_length: int) -> str:
    values = [0] * max_length
    for i in range(max_length):
        rand_value = random.randint(0, 61)
        if rand_value < 10:
            rand_value += 48
        elif rand_value < 36:
            rand_value += 65 - 10
        else:
            rand_value += 97 - 36
        values[i] = chr(rand_value)
    return ''.join(values)


if __name__ == "__main__":
    try:
        lines_number = sys.argv[1]
        lines_number = int(lines_number)
    except IndexError:
        print("Missing the number of lines")
        sys.exit()
    except ValueError:
        print("The number of lines must be an integer")
        sys.exit()

    try:
        max_length = sys.argv[2]
        max_length = int(max_length)
    except IndexError:
        print("Missing max length of line")
        sys.exit()
    except ValueError:
        print("The maximum length of line must be an integer")
        sys.exit()
    
    with open("large_file.txt", "w") as file:
        small_number = int(max_length * 0.01)
        if small_number < 5:
            small_number = 5
        file.write(generate_line(small_number)+'\n')

        for i in range(lines_number-1):
            line = generate_line(max_length)
            file.write(line+"\n")