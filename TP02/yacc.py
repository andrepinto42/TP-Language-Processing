import ply.yacc as yacc
from lex import tokens,tokens_captured
from splitter import *
from lex import str_Input
from re import *
from buildFunctions import *
from buildParamsLex import getLiterals
import sys

lista_codigo = []


def push(code):
    lista_codigo.append(code)

def p_prog(p):
    "prog : comandos"

def p_comandos_varios01(p):
    "comandos : "

def p_comandos_varios02(p):
    "comandos : comando comandos "

def p_comando01(p):
    "comando : LEX"
    push(buildLexerInitial())

    #Use lexer to discover the literals that are being used
    literals_captured = getLiterals()
    push("literals = "+literals_captured)

    push("tokens = " +str(tokens_captured))


def p_comando02(p):
    "comando : YACC"
    push(buildLexerEnd())
    push(buildYaccInitial())

def p_comando03(p):
    "comando : code"


def p_comando04(p):
    "comando : COMMENTARY"
    # Do nothing because the commentary is not supposed to appear in the final code


def p_atrib02(p):
    "code : PARAMETER '=' CODE_EXPRESSION"
    code = p[3][2:-2]
    parameter = p[1][1:]

    push(parameter +" = "+code);

# Main expression for capturing lexer Code
def  p_atrib06(p):
    "code : TOKEN_ID  extra CODE_EXPRESSION"
#     #Cut the start of string because it has a '\n'
    token_ID = p[1][1:].strip()
    
    #Cut the start and end because it has '""' '""'    
    code = p[3][2:-2]
    
    extra = ""

    if p[2] == "":
        return

    if p[2] == r'!':
        push( buildFunctionLEX(token_ID,extra,code,False))
        return
    #Cut the start and end because it has '"' '"'
    extra = p[2][1:-1]

    # print("extra ->",extra," of token ",token_ID," with code block -> ",code)
    
    #Store the function in the global dictionary
    push( buildFunctionLEX(token_ID,extra,code))

def p_atrib_extra01(p):
    "extra : "
    p[0] = ""

def p_atrib_extra02(p):
    "extra : STR_ATRIB extra"
    p[0] = p[1] + p[2]

def p_atrib_extra03(p):
    "extra : SIGNAL extra"
    p[0] = p[1] + p[2]

#Guardar o numero de funcoes de gramatica reconhecidas
numGrammar = 0
last_inserted_grammar = 0

def p_atrib07(p):
    "code : GRAMMAR CODE_EXPRESSION"
    global numGrammar
    global last_inserted_grammar

    #Remover o %"" "" da gramatica capturada
    grammar_str= p[1][3:-2]

    #Caso exista um "+" na expressao entao
    #deve -se usar r' code: "+" '
    if r"'" in grammar_str:
        grammar_str = 'r"'+grammar_str+'"'
    else:
        grammar_str = "r'"+grammar_str+"'"

    code = p[2][2:-2].strip()

    push("def p_grammar"+str(numGrammar)+"(t):\n\t"+grammar_str)
    for piece in code.split("\n"):
        push("\t"+piece);
    
    #Store the index of the last grammar inserted 
    # so after the parsing is done we can add more code to the last segment
    last_inserted_grammar =len(lista_codigo)

    #Add \n at the end 
    push("")

    #Increase the counter for the number of functions of Grammar
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

#-------------------------
# Arranjar pedacos do codigo
#-------------------------

lista_codigo[last_inserted_grammar] = buildYaccEnd()

#--------------------------
#   Escrever para o file   
#--------------------------

import sys 
if (len(sys.argv) >=3):
    fileOutput = open(sys.argv[2],"w")
    for codigo in lista_codigo:
        print(codigo,file=fileOutput)
else:
    for codigo in lista_codigo:
        print(codigo)


# for line in sys.stdin:
#     parser.parse(line)
