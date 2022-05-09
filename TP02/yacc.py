import ply.yacc as yacc
from test import tokens 
from splitter import *
from test import str_Input
from re import *
from buildFunctions import *
from buildParamsLex import run
import sys

lista_codigo = []

#Guardar o numero de funcoes de gramatica reconhecidas
numGrammar = 0
def push(code):
    lista_codigo.append(code)

def p_prog(p):
    "prog : comandos"

def p_comandos_varios01(p):
    "comandos : "
    push(buildYaccEnd())

def p_comandos_varios02(p):
    "comandos : comando comandos "

def p_comando01(p):
    "comando : LEX"
    push(buildLexerInitial())


def p_comando02(p):
    "comando : YACC"
    push(buildLexerEnd())
    push(buildYaccInitial())

def p_comando03(p):
    "comando : code"

def p_atrib01(p):
    "code : LITERALS '=' STR_ATRIB"    
    push("literals = "+str(splitter(p[3])))


def p_atrib02(p):
    "code : IGNORE '=' STR_ATRIB"
    push("ignore = "+ p[3]);


def p_atrib03(p):
    "code : PRECEDENCE '=' CODE_EXPRESSION"
    #Trim "" "" from the code expression
    code = p[3][2:-2]
    push("precedence = " + code);

def p_atrib04(p):
    "code : TOKENS '=' STR_ATRIB"
    #Remove the " " from the begin and the end
    str_Tokens = p[3][1:-1]

    str_Tokens = str_Tokens.split(" ")
    push("tokens = " +str(str_Tokens))


def  p_atrib05(p):
    "code : TOKEN_ID STR_ATRIB CODE_EXPRESSION"
    #Cut the start of string because it has a '\n'
    token_ID = p[1][1:].strip()
    
    #Cut the start and end because it has '"' '"'
    regex = p[2][1:-1]

    #Cut the start and end because it has '""' '""'
    code = p[3][2:-2]
    # print("regex ->",regex," of token ",token_ID," with code block -> ",code)
    
    #Store the function in the global dictionary
    push(buildFunctionLEX(token_ID,regex,code))
    
#Expression where there is no regex needed
def  p_atrib06(p):
    "code : TOKEN_ID  CODE_EXPRESSION"
    token_ID = p[1][1:]
    
    code = p[2][2:-2]
    # print("regex ->",regex," of token ",token_ID," with code block -> ",code)
    
    #Store the function in the global dictionary
    push( buildFunctionLEX(token_ID,"",code))

def p_atrib07(p):
    "code : GRAMMAR CODE_EXPRESSION"
    global numGrammar

    #Remover o %"" "" da gramatica capturada
    grammar_str= p[1][3:-2]

    grammar_str = 'r"'+grammar_str+'"'
    code = p[2][2:-2].strip()
    push("def p_grammar"+str(numGrammar)+"(p):\n\t"+grammar_str+"\n\t"+code+"\n");
    numGrammar += 1



def p_atrib08(p):
    "code : CODE_EXPRESSION"
    #Cut the "" code "" from the string
    code = p[1][2:-2]
    push(code)

def p_error(p):
    print("Error in",p)

parser = yacc.yacc()

parser.parse(str_Input)

fileOutput = open("output.py","w")

for codigo in lista_codigo:
    print(codigo,file=fileOutput)


run()

quit()

# for line in sys.stdin:
#     parser.parse(line)
