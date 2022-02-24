"""
Created by

Emir Can
"""

path = os.chdir("C:\\Your\\Path\\Adress\\") #\\ must be dont forget.
i=0
for file in os.listdir(path): #Go to path directory
    new_file_name = "add_name_or_dont{}.txt".format(i) #new_file_name = u can change the name
    #if u add name files names change name1.txt,name2.txt ...
    #if dont add name filens name change like 1.txt 2.txt ...
    os.rename(file, new_file_name) #Operation system call the rename function and change file 
    i +=1