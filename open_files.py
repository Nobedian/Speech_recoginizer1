import os

def open_file_E(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('E:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                os.startfile(root + '\\' + name)


def open_file_H(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('H:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                os.startfile(root + '\\' + name)


def open_file_F(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('F:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                os.startfile(root + '\\' + name)

