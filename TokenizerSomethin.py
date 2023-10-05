#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")

#Token Classes
Comments = ["//", "/*", "/**", "*/", "**/"]
Symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]


tempTok =[] 
tempTok = file1.readlines()

for x in tempTok:
    if (x == ""):
        continue
    
    #if (x[0] == '/'):
    #    continue
    
    print(x)
    #for i in x:
   #     print(i)


   
    





#Closing files
file1.close
file2.close