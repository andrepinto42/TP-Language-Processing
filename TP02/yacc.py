import ply.yacc as yacc
from test import tokens 
from splitter import *
from test import str_Input
from re import *
from buildFunctions import *

import sys

token_Dictio = {}

def p_prog(p):
    "prog : comandos"

def p_comandos_varios01(p):
    "comandos : "

def p_comandos_varios02(p):
    "comandos : comandos comando"

def p_comando01(p):
    "comando : atrib"

def p_comando02(p):
    "comando : LEX"
    print("LEX FOUND")

def p_comando03(p):
    "comando : YACC"
    print("YACC FOUND")

def p_comando04(p):
    "comando : COMMENTARY COMMENTARYTOKEN"
    print("COMMENTARY FOUND", " -> ", p[2])


def p_atrib01(p):
    "atrib : LITERALS '=' STR_ATRIB"
    print("literals =", splitter(p[3]))


def p_atrib02(p):
    "atrib : IGNORE '=' STR_ATRIB"
    print("Ignore must be this ->",p[3]);


def p_atrib03(p):
    "atrib : TOKENS '=' STR_ATRIB"
    #Remove the " " from the begin and the end
    str_Tokens = p[3][1:-1]

    str_Tokens = str_Tokens.split(" ")
    print("TOKENS must be this ->",str_Tokens);


def  p_atrib04(p):
    "atrib : TOKEN_ID STR_ATRIB CODE_EXPRESSION"
    #Cut the start of string because it has a '\n'
    token_ID = p[1][1:]
    
    #Cut the start and end because it has '"' '"'
    regex = p[2][1:-1]

    #Cut the start and end because it has '""' '""'
    code = p[3][2:-2]
    # print("regex ->",regex," of token ",token_ID," with code block -> ",code)
    
    #Store the function in the global dictionary
    token_Dictio[token_ID] = buildFunctionLEX(token_ID,regex,code)
    
#Expression where there is no regex needed
def  p_atrib05(p):
    "atrib : TOKEN_ID  CODE_EXPRESSION"
    token_ID = p[1][1:]
    
    code = p[2][2:-2]
    # print("regex ->",regex," of token ",token_ID," with code block -> ",code)
    
    #Store the function in the global dictionary
    token_Dictio[token_ID] = buildFunctionLEX(token_ID,"",code)
        

def p_error(p):
    print("Error in",p)

parser = yacc.yacc()



parser.parse(str_Input)

final_code = buildDefault()

for token in token_Dictio:
    final_code += "\n" +token_Dictio[token]

final_code += buildEnd()

print(final_code)


quit()

# for line in sys.stdin:
#     parser.parse(line)
