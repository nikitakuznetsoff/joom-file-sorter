import sys
import math
import os

def merge_sort(input_filename: str, output_filename: str):
    buffer_first = "buffer1.txt"
    buffer_second = "buffer2.txt"

    # Копирование всех строк в буфферный файл
    input_file = open(input_filename, "r")
    buffer = open(buffer_first, "w")
    for line in input_file:
        buffer.write(line)
    input_file.close()
    buffer.close()

    step = 1    # Шаг слияния
    while True:
        left_reader = open(buffer_first, "r") 
        right_reader = open(buffer_first, "r")
        writer = open(buffer_second, "w")

        for i in range(step):
            right_reader.readline()
        
        left_line = left_reader.readline().strip()
        right_line = right_reader.readline().strip()

        # Условия выхода: шаг слияния стал больше количества строк в файле
        if not right_line:
            break
        
        while left_line or right_line:
            left_counter, right_counter = 0, 0
            while left_counter < step or right_counter < step:
                if right_counter >= step or (left_line < right_line and left_counter < step):
                    writer.write(left_line+'\n')
                    left_counter += 1
                    left_line = left_reader.readline().strip()
                else:
                    writer.write(right_line+'\n')
                    right_counter += 1
                    right_line = right_reader.readline().strip()
                    # Условие для случая, когда длина правой части меньше шага слияния
                    if not right_line:
                        right_counter = step
            
            # Перевод итераторов на соответствующее количество позиций
            for i in range(step - 1):
                left_reader.readline()
                right_reader.readline()
            
            left_line = left_reader.readline().strip()
            right_line = right_reader.readline().strip()

            # Добавление оставшихся строк в случае, когда количество строк некратно шагу слияния
            if left_line and not right_line:
                while left_line:
                    # print(left_line)
                    writer.write(left_line+'\n')
                    left_line = left_reader.readline().strip()
            
            if not left_line and not right_line:
                break
        
        buffer_first, buffer_second = buffer_second, buffer_first
        left_reader.close()
        right_reader.close()
        writer.close()
        step *= 2
    
    # Вычисление того, какой из буферных файлов использовался последним для записи
    # Переименование последнего использовавшегося, удаление второго
    degree = int(math.log(step))
    if degree % 2 == 0:
        os.rename(buffer_first, output_filename)
        os.remove(buffer_second)
    else:
        os.rename(buffer_second, output_filename)
        os.remove(buffer_first)


if __name__ == "__main__":
    try:
        filename_input = sys.argv[1]
    except IndexError:
        print("The input file name is missing")
        sys.exit()

    try:
        filename_output = sys.argv[2]
    except IndexError:
        print("The output file name is missing")
        sys.exit()

    try:
        input_file = open(filename_input, "r")
    except FileNotFoundError:
        print("Incorrect file name")
        sys.exit()

    input_file.close()
    merge_sort(filename_input, filename_output)