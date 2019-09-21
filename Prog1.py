"""
Name: Joachim Isaac.
Course: CS 2433-101, Fall 19, Dr. Stringfellow.
Purpose: To create a program that reads in values and computes
them using the bitwise operators. Then displays them neatly
on an output file.
 """




def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")
    with open(file_name,'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return input_list


def split_table1_input(input_list):
    table1_input = []
    counter = 0

    for input in input_list:
        if len(input) == 1:
            counter += 1

        if counter < 2:
            table1_input.append(input)

    return convert_str_table1(table1_input)



def convert_str_table1(table1_input):
    index = 0

    while index < len(table1_input):
        if len(table1_input[index]) <= 1:
            table1_input[index][0] = int(table1_input[index][0])
        elif len(table1_input[index]) == 2:
            table1_input[index][0] = int(table1_input[index][0])
            table1_input[index][1] = int(table1_input[index][1])

        index += 1

    return table1_input



def compute_table1_ops(table1_input):
    truth_table_values = [[0, 0],[0, 1],[1, 0],[1, 1]]
    ROWS = table1_input[0].pop(0) + len(truth_table_values)
    table1_input.pop(0)
    COLS = 6
    total_table_input = truth_table_values + table1_input
    result1 = []

    for index in range(ROWS):
        for c_input in range(COLS):
            if c_input == 0:
                result1.append(total_table_input[index][0])
            elif c_input == 1:
                result1.append(total_table_input[index][1])
            elif c_input == 2:
                result1.append(total_table_input[index][0] & total_table_input[index][1])
            elif c_input == 3:
                result1.append(total_table_input[index][0] | total_table_input[index][1])
            elif c_input == 4:
                result1.append(total_table_input[index][0] ^ total_table_input[index][1])
            elif c_input == 5:
                result1.append(~total_table_input[index][0])
    list = []
    result_2d = []
    counter = 0

    for i in range(len(result1)):
        list.append(result1[i])
        counter += 1
        if counter == 6:
            result_2d.append(list)
            list = []
            counter = 0

    result_2d = [['X','Y','&','|','^','~']] + result_2d

    return result_2d



def split_table2_input(input_list):
    table2_input = []
    counter = 0

    for input in input_list:
        if len(input) == 1:
            counter += 1

        if counter == 2:
            table2_input.append(input)

    return convert_str_table2(table2_input)



def convert_str_table2(table2_input):
    index = 0

    while index < len(table2_input):
        if len(table2_input[index]) <= 1:
            table2_input[index][0] = int(table2_input[index][0])
        elif len(table2_input[index]) == 2:
            table2_input[index][1] = int(table2_input[index][1])
        elif len(table2_input[index]) == 3:
            table2_input[index][1] = int(table2_input[index][1])
            table2_input[index][2] = int(table2_input[index][2])
        elif len(table2_input[index]) == 4:
            table2_input[index][1] = int(table2_input[index][1])
            table2_input[index][2] = int(table2_input[index][2])
            table2_input[index][3] = int(table2_input[index][3])

        index += 1

    return table2_input

def compute_table2_ops(table2_input):
    ROWS = table2_input[0].pop(0)
    table2_input.pop(0)
    COLS = 10
    result1 = []
    for index in range(ROWS):
        for c_input in range(COLS):


    return table2_input








## now i can deal with this!



def CreateBitwiseTable(bitTable1):
    for index in range(len(bitTable1)):
        if type(bitTable1[index][0]) == str:
            print("%2s %16s %16s %16s %16s %16s" %(bitTable1[index][0],bitTable1[index][1],bitTable1[index][2], bitTable1[index][3],bitTable1[index][4],bitTable1[index][5]))
        elif type(bitTable1[index][0]) == int:
            print("%2d %16d %16d %16d %16d %16d" % (bitTable1[index][0], bitTable1[index][1], bitTable1[index][2], bitTable1[index][3], bitTable1[index][4],bitTable1[index][5]))


















print("Name: Joachim Isaac\nProgram1: Bitwise Operations\n")
input_list = read_input_files()

list1 = split_table1_input(input_list)
list2 = split_table2_input(input_list)

# print(compute_table1_ops(list1))
print(compute_table2_ops(list2))







# CreateBitwiseTable(result)

# print(split_table2_input(input_list))





#splits the input into an array of arrays to work with to do calculations.
#[['2', '0'], ['0', '2'], ['5', '7'], ['35', '7'] [1,3,2,4]]

#1 I have to make a fucntion that calculates and stores all the values. For each set of values it computes their is
#certain postion it ditributes or spaces the value to.
#the way it reads in things is the way it can print out things
#may have to use a switch state ment but it may not be necessary; we will see.
# keep in mind that when i make the function to make the first table it will have an array that has the truth table part there before it computes the
#values we have read in .