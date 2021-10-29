with open('./text.txt') as file:
    para = file.read();

    paraCount = int(input("paragraph count :"))
    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(para+'\n\n')