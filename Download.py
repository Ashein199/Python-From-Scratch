from urllib.request import urlretrieve

link = input("image link :");
imgName = input("img name :");
urlretrieve(link,'img/'+imgName+'.jpg')