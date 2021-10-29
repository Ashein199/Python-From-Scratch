# with open('./about.txt','w') as file:
#     file.write("I'm Entt Nine.")

#     #other work

# with open('./about.txt','a') as file: #amend
#     file.write("\n20 years old")

list =["I'm Entt Nine.","\n20 years old"]
with open('./about.txt','w') as file:
    file.writelines(list)
