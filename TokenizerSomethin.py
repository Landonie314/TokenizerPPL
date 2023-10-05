#Landon Jones_10/04/2023_PPL_Tokenizer
#Opening the jack files we need to read from
file1 = open("Main.jack", "r")
file2 = open("SquareGame.jack", "r")

#Token Classes
comments = ["//", "/*", "/**", "*/", "**/"]
symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
specialSymbol = ["<", ">", "\"", "&"]
markup = ["&lt;", "&gt;", "&quot;", "&amp;"]
reserve = ["class", "constructor", "method", "funtion", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this", "main"]

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
    smolTemp = x.split()
    for i in smolTemp:
        print(i)
    
    #each token
    """ for i in smolTemp:
        #What class does the token belong to?
        if i in comments:
            print("<comment> " + i + " </comment>")
        if i in symbols:
            print("<symbol> " + i + " </symbol>")
        if i in specialSymbol:
            if i == "<":
                print("<symbol> " + "&lt;" + " </symbol>")
            if i == ">":
                print("<symbol> " + "&gt;" + " </symbol>")
            if i == "\"":
                print("<symbol> " + "&quot;" + " </symbol>")
            if i == "&":
                print("<symbol> " + "&amp;" + " </symbol>")
        if i in reserve:
            print("<keyword>" + i + "</keyword>") """
    
    
    #for i in x:
    #   print(i)


for x in smolTemp:
    tester = x.split(";")
    for i in tester:
        print(i)

    





#Closing files
file1.close
file2.close