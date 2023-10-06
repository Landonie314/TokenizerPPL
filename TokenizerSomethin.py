#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
import re
re.compile('<title>(.*)</title>')
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")
f1 = open("MainT.xml", "w")
f2 = open("SquareGameT.xml", "w")


#Token Classes
comments = ["//", "/*", "/**", "*/"]
symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "|", "~"]
specialSymbol = ["<", ">", "\"", "&"]
markup = ["&lt;", "&gt;", "&quot;", "&amp;"]
reserve = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]

#list to store different tokens for each line
smolTemp = []
#stores number of double quotes
tempNumer = 0
#stores the file into a list
tempTok =[] 
tempTok = file1.readlines()

#for each element in the list (Line)
for x in tempTok:
    #print(x)
    #splitting each line into tokens
    smolTemp = filter(None, re.split(r'\s|([^\w@#/*?])', x))
    #for i in smolTemp:
    #will store stringConstants
    tempWord = ""
    #each token
    for i in smolTemp:
        #What class does the token belong to?
        if(tempNumer % 2 == 0):
            if i in comments:
                f1.write("<comment> " + i + " </comment>")
                #Only reads the comment line tokens
                if(i == "//"):
                    break
                else:
                    f1.write("<comment> " + "*/" + " </comment>")
                    break           
            if i in symbols:
                f1.write("<symbol> " + i + " </symbol>")
            elif i in specialSymbol:
                if i == "<":
                    f1.write("<symbol> " + "&lt;" + " </symbol>")
                elif i == ">":
                    f1.write("<symbol> " + "&gt;" + " </symbol>")
                elif i == "\"":
                    f1.write("<symbol> " + "&quot;" + " </symbol>")
                    tempNumer += 1
                    continue
                elif i == "&":
                    f1.write("<symbol> " + "&amp;" + " </symbol>")
            elif i in reserve:
                f1.write("<keyword> " + i + " </keyword>")
            #numberConstants
            elif i.isdigit():
                if(int(i) >= 0):
                    f1.write("<integerConstant " + i + " </integerConstant>") 
            else:
                f1.write("<identifier> " + i + " </identifier>")
        #if currently inside of double quotes
        else:
            if(i == "\""):
                tempNumer += 1
                #build the String constants
                f1.write("<stringConstant " + tempWord + " </stringConstant>")
                f1.write("<symbol> " + "&quot;" + " </symbol>")
            tempWord = tempWord + " " + i
            #next iteration
            continue
           
#Closing files
file1.close()
file2.close()
f1.close()
f2.close()