"""
Name: Joachim Isaac.
Course: CS 2433-101, Fall 19, Dr. Stringfellow.
Purpose: To create a program that reads in values and computes
them using the bitwise operators. Then displays them neatly
on an output file.

Important points:(Things I learned):

--> Found out that you can't declare a constant variable in python.
Unless you declare a variable in a seperate file so that you
can't access it.

--> There is no switch in python, utilizing hash tables/(dictionaries)
is a good work around for the switch since you can access a value in
O(1) time via the hash table data structure and you can store mostly
anything for it's key and value including function or objects.

"""

import math




#Reads the input from the files line by line
#and stores each line as an array of values.
def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")

    #Handles both the opening and closing of the file
    #when reading in values.
    with open(file_name,'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return input_list


#Opens output file to output to.
def open_output_file():
    outfile = input("Please enter output file name: \n")
    file = open(outfile,'w')
    return file


(Remove)
#Splits all the values for table 1 into an array.
#and returns that array.
def split_table1_input(input_list):
    table1_input = []
    counter = 0

    for input in input_list:
        if len(input) == 1:
            counter += 1

        if counter < 2:
            table1_input.append(input)

#Changes all string numbers into integers that have to be operated on.
#It returns a new array with a mix of strings and integers.
    return convert_str_table1(table1_input)




#Converts all numbers into integers.
#It ignores the string characters then returns an updated array.
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





#Computes all the operations that have to occured in table 1
#afterwards it stores, the arguements, operands and the answers in sub-arrays.
def compute_table1_ops(table1_input):

    #Default values for the truth table.
    truth_table_values = [[0, 0],[0, 1],[1, 0],[1, 1]]

    #Computes how many ROWS is needed.
    ROWS = table1_input[0].pop(0) + len(truth_table_values)

    #Removes the empty array after the ROW value was popped and summed.
    table1_input.pop(0)

    COLS = 6

    #Adds the default values on the values that were read in.
    total_table_input = truth_table_values + table1_input
    result1 = []

    #Appends all the operands and answers into a list
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

#Groups all operands and answers into subarrays.
    for i in range(len(result1)):
        list.append(result1[i])
        counter += 1
        if counter == 6:
            result_2d.append(list)
            list = []
            counter = 0

#Adds on the symbols at the top of the table, so they can be displayed.
    result_2d = [['X','Y','&','|','^','~']] + result_2d

    return result_2d




(Remove)
#Splits all the values for table 2 into an array.
def split_table2_input(input_list):
    table2_input = []
    counter = 0

    for input in input_list:
        if len(input) == 1:
            counter += 1

        if counter == 2:
            table2_input.append(input)

    # Changes all string numbers into integers that have to be operated on.
    # It returns a new array with a mix of strings and integers.
    return convert_str_table2(table2_input)




#Converts all numbers into integers.
#It ignores the string characters then returns an updated array.
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




#Computes all the operations that have to occured in table 1
#and stores, the arguements, operands and the answers in subarrays.
def compute_table2_ops(table2_input):
    ROWS = table2_input[0].pop(0)
    table2_input.pop(0)
    COLS = 10
    result2 = []

    for index in range(ROWS):
        if len(table2_input[index]) == 2:
            result2.append([table2_input[index][0],table2_input[index][1],
                switch_2args(table2_input[index][0],table2_input[index][1])])
        elif len(table2_input[index]) == 3:
            result2.append([table2_input[index][0], table2_input[index][1], table2_input[index][2],
                switch_3args(table2_input[index][0], table2_input[index][1],table2_input[index][2])])
        elif len(table2_input[index]) == 4:
            result2.append([table2_input[index][0], table2_input[index][1], table2_input[index][2],
                table2_input[index][3],switch_4args(table2_input[index][0],table2_input[index][1],
                    table2_input[index][2],table2_input[index][3])])

    # Adds on the symbols at the top of the table, so they can be displayed.
    result2 = [['X', 'P', 'V', '>>', '<<', 'S', 'G', 'E', 'C', '2']] + result2

    return result2



#Prints out the first table
def CreateBitwiseTable(bitTable1,output_file):
    for index in range(len(bitTable1)):
        if type(bitTable1[index][0]) == str:
            # '%10s',"%10d" and others control the indentation. The number determines the amount of space indented.
            output_file.write("%10s %16s %16s %16s %16s %16s \n" %(bitTable1[index][0],bitTable1[index][1],
                bitTable1[index][2], bitTable1[index][3],bitTable1[index][4],bitTable1[index][5]))
        elif type(bitTable1[index][0]) == int:
            output_file.write("%10d %16d %16d %16d %16d %16d \n" % (bitTable1[index][0], bitTable1[index][1],
                bitTable1[index][2], bitTable1[index][3], bitTable1[index][4],bitTable1[index][5]))

    output_file.write("\n")




#Prints out the Second table, It prints different places(indentation) depending on
#the length of the subarray that is being checked and the first
#string in that array.
def moreBitwiseOps(bitTable2,outputfile):

    for index in range(len(bitTable2)):

        if len(bitTable2[index]) > 5:
            output_file.write("%10s %3s %2s %8s %8s %8s %8s %8s %8s %8s \n"%(bitTable2[index][0],
                bitTable2[index][1],bitTable2[index][2], bitTable2[index][3],bitTable2[index][4],
                    bitTable2[index][5],bitTable2[index][6],bitTable2[index][7],
                        bitTable2[index][8],bitTable2[index][9]))

        if len(bitTable2[index]) == 3:
            #'{:10}' and others control the indentation. the number determines the amount of space.
            if bitTable2[index][0] == '>':
                output_file.write("{:10d} {:15d} \n".format(bitTable2[index][1],bitTable2[index][2]))
            if bitTable2[index][0] == '<':
                output_file.write("{:10d} {:24d} \n".format(bitTable2[index][1], bitTable2[index][2]))
            if bitTable2[index][0] == 'E':
                output_file.write("{:10d} {:51d} \n".format(bitTable2[index][1], bitTable2[index][2]))
            if bitTable2[index][0] == 'C':
                output_file.write("{:10d} {:60d} \n".format(bitTable2[index][1], bitTable2[index][2]))
            if bitTable2[index][0] == '2':
                output_file.write("{:10d} {:69d} \n".format(bitTable2[index][1], bitTable2[index][2]))
        if len(bitTable2[index]) == 4 and bitTable2[index][0] == 'G':
            output_file.write("{:10d}{:4d}{:39d} \n".format(bitTable2[index][1],
                bitTable2[index][2],bitTable2[index][3]))
        if len(bitTable2[index]) == 5 and bitTable2[index][0] == 'S':
            output_file.write("{:10d}{:4d}{:3d}{:29d} \n".format(bitTable2[index][1], bitTable2[index][2],
                bitTable2[index][3],bitTable2[index][4]))

    output_file.write("\n")






#This is an implementation of a dictionary(hash table) with the functionality of a switch.
def switch_2args(argument,num):
    switcher = {
        '>': num >> 1,
        '<': num << 1,
        'E': int((num % 2) == 0),
        '2': isPower2(num),
        'C': count_bits(num),
    }
    return switcher.get(argument, "nothing")



#This is an implementation of a dictionary(hash table) with the functionality of a switch.
def switch_3args(argument, num, position):
    switcher = {
        'G': getBit(num, position)
    }
    return switcher.get(argument, "nothing")



#This is an implementation of a dictionary(hash table) with the functionality of a switch.
def switch_4args(argument, num, position, value):
#If the arguement is an 'S' then the fucntion setBit is accessed.
    switcher = {
        'S': setBit(num, position, value)
    }
    return switcher.get(argument, "nothing")



#gets the log2 of x.
def Log2(x):
    if x == 0:
        return False;
    return (math.log10(x) / math.log10(2))



#counts the bits of a number
def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count



#checks wether a number is a power of 2.
def isPower2(n):
    return int(math.ceil(Log2(n)) == math.floor(Log2(n)))




#gets the bit at a specific position.
def getBit(number,postion):
    num = bin(number)
    num = num[2:]
    if postion-1 <= len(num):
        return int(num[postion-1])
    else:
        return "Invalid position!"




#sets a bit at a specific position.
def setBit( number,  position,  value):
    mask = 1 << position
    return (number & ~mask) | ((value << position) & mask)















print("Name: Joachim Isaac\nProgram1: Bitwise Operations\n")

#Reads in the input returns and array of the input
input_list = read_input_files()

#Opens output file and stores the file object in a variable.
output_file = open_output_file()

output_file.write("Name: Joachim Isaac\nProgram1: Bitwise Operations\n\n")

#Splits apart the input for table 1 into a list
table1_list = split_table1_input(input_list)

#Splits apart the input for table 2 into a list
table2_list = split_table2_input(input_list)

#Computes the values for table1 and then prints the table.
CreateBitwiseTable(compute_table1_ops(table1_list),output_file)

#Computes the values for table2 and then prints the table.
moreBitwiseOps(compute_table2_ops(table2_list),output_file)

#Closes output file
output_file.close()

