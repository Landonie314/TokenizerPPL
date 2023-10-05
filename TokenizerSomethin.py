#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
import re
re.compile('<title>(.*)</title>')
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")

#Token Classes
comments = ["//", "/*", "/**", "*/"]
symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "|", "~"]
specialSymbol = ["<", ">", "\"", "&"]
markup = ["&lt;", "&gt;", "&quot;", "&amp;"]
reserve = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]

#list to store different tokens for each line
smolTemp = []
tempNumer = 0
#stores the file into a list
tempTok =[] 
tempTok = file1.readlines()

#for each element in the list (Line)
for x in tempTok:
    print(x)
    #splitting each line into tokens
    smolTemp = filter(None, re.split(r'\s|([^\w@#/*?])', x))
    #for i in smolTemp:
    tempWord = ""
    #each token
    for i in smolTemp:
        #What class does the token belong to?
        if(tempNumer % 2 == 0):
            if i in comments:
                print("<comment> " + i + " </comment>")
                #Only reads the comment line tokens
                if(i == "//"):
                    break
                else:
                    print("<comment> " + "*/" + " </comment>")
                    break
                
            if i in symbols:
                print("<symbol> " + i + " </symbol>")
            elif i in specialSymbol:
                if i == "<":
                    print("<symbol> " + "&lt;" + " </symbol>")
                elif i == ">":
                    print("<symbol> " + "&gt;" + " </symbol>")
                elif i == "\"":
                    print("<symbol> " + "&quot;" + " </symbol>")
                    tempNumer += 1
                    continue
                elif i == "&":
                    print("<symbol> " + "&amp;" + " </symbol>")
            elif i in reserve:
                print("<keyword> " + i + " </keyword>")
            elif i.isdigit():
                if(int(i) >= 0):
                    print("<integerConstant " + i + " </integerConstant>") 
            else:
                print("<identifier> " + i + " </identifier>")
        else:
            if(i == "\""):
                tempNumer += 1
                print("<stringConstant " + tempWord + " </stringConstant>")
                print("<symbol> " + "&quot;" + " </symbol>")
            tempWord = tempWord + " " + i
            continue
          
    
#Closing files
file1.close()
file2.close()