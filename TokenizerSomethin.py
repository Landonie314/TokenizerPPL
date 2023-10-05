#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
import re
re.compile('<title>(.*)</title>')
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")

#Token Classes
comments = ["//", "/*", "/**", "*/", "**/"]
symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "|", "~"]
specialSymbol = ["<", ">", "\"", "&"]
markup = ["&lt;", "&gt;", "&quot;", "&amp;"]
reserve = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]

#list to store different tokens for each line
smolTemp = []
tester = []

#stores the file into a list
tempTok =[] 
tempTok = file1.readlines()

#for each element in the list (Line)
for x in tempTok:
    print(x)
    #splitting each line into tokens
    #smolTemp = x.split()
    smolTemp = filter(None, re.split(r'\s|([^\w@#/*"?])', x))
    #for i in smolTemp:
    #    print(i)
    
    #each token
    for i in smolTemp:
        #What class does the token belong to?
        if i in comments:
            print("<comment> " + i + " </comment>")
        elif i in symbols:
            print("<symbol> " + i + " </symbol>")
        elif i in specialSymbol:
            if i == "<":
                print("<symbol> " + "&lt;" + " </symbol>")
            elif i == ">":
                print("<symbol> " + "&gt;" + " </symbol>")
            elif i == "\"":
                print("<symbol> " + "&quot;" + " </symbol>")
            elif i == "&":
                print("<symbol> " + "&amp;" + " </symbol>")
        elif i in reserve:
            print("<keyword>" + i + "</keyword>")
        else:
            print("<idenifier>" + i + "</identifier>")
    
    
    #for i in x:
    #   print(i)


for x in smolTemp:
    tester = x.split(";")
    for i in tester:
        print(i)

    





#Closing files
file1.close
file2.close