#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")

#Token Classes
Comments = ["//", "/*", "/**", "*/", "**/"]
Symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
Markup = ["&lt;", "&gt;", "&quot;", "&amp;"]
Reserve = ["class", "constructor", "method", "funtion", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]


#stores the file into a list
tempTok =[] 
tempTok = file1.readlines()

#for each element in the list (Line)
for x in tempTok:
    
    if (x[0] == '/'):
       continue
    
    print(x)
    #for i in x:
    #   print(i)


   
    





#Closing files
file1.close
file2.close