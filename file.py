"""
Created by
Emir Can
"""

dosya = open("file_name_txt","a",encoding="utf-8") #Open file read and write
i=0
for i in range(number): #Number can be file len but not len(file) because txt files characters include word.
    dosya.write("name_new_file_name{}.txt\n".format(i)) #Don't forget \n and \(one)
    i+=1