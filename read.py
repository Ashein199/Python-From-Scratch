# file = open('./text.txt');
# for line in file:
#     print(line)

# file.seek(0)
# line_list = file.readlines();
# print(line_list)

# file.seek(50)  
# para = file.read(100)
# print(para)

# file.close();

with open('./text.txt') as file: #can be use as above #no need to close file
    for line in file:
        print(line)
print("...........other work")
