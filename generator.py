words = ["my","name","is","entt","nine"];
from random import randint;
def randomSentenceGenerator(word):
    randomIndex= randint(0,len(words)-1);
    return f'{words[randomIndex]} {word} '

with open('./text.txt') as file:
    para = file.read();
    wordsList = para.split();
    sentences_list = list(map(randomSentenceGenerator,wordsList))
    paraCount = int(input("paragraph count :"))
    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(''.join(sentences_list)+'\n\n')