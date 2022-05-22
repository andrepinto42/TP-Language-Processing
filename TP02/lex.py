import ply.lex as lex
from re import sub

import sys

input_file=""

if len(sys.argv) >= 2:
    #Carregar o conteudo a partir de um ficheiro
    str_Input = open(sys.argv[1]).read()
    input_file = sys.argv[1]
    
else:
    str_Input = sys.stdin.read()


tokens_captured = []


#-----------------------
# Parametros do Lexer 
#-----------------------
tokens =[
    "LEX","YACC",
    "PARAMETER",
    "STR_ATRIB","TOKEN_ID","GRAMMAR","SIGNAL","COMMENTARY",
    "CODE_EXPRESSION"]

literals = ['=',"'",'"']

t_ignore = ' \t\r'

states = [
    ("LEXSTATE","inclusive"),
    ("YACCSTATE","inclusive")
]

def t_LEX(t):
    r'%\s*(?i)LEX'
    t.lexer.begin("LEXSTATE")
    return t


def t_YACC(t):
    r'%\s*(?i)YACC'
    t.lexer.begin("YACCSTATE")
    return t


def t_CODE_EXPRESSION(t):
    r'\"\"(.|\n)*?\"\"(?!\")'
    return t

def t_STR_ATRIB(t):
    r'"[^"](.|\n)*?[^"]"'
    return t

def t_SIGNAL(t):
    r'\!'
    return t

def t_COMMENTARY(t):
    r'\#.*'
    return t

def t_PARAMETER(t):
    r'%\w+'
    return t 
#------------------------------------
#       YACC - STATE
#------------------------------------


def t_YACCSTATE_GRAMMAR(t):
    r'\%\"\"(.|\n)*?\"\"'
    return t
#------------------------------------
#       LEX - STATE
#------------------------------------


def t_LEXSTATE_TOKEN_ID(t):
    r'\s*\w+'
    token_Found = sub("\s*","",t.value)
    if (token_Found != "error"):
        tokens_captured.append(token_Found)
    return t

def t_error(t):
    if (t.value[0] != '\n'):
        print("Wrong character!", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()