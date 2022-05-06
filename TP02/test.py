import ply.lex as lex

str_Input =r'''
%% LeX
%literals = "+-/*=()"
%ignore = " \t\n"
%tokens = "VAR NUMBER"
VAR "[a-zA-Z_][a-zA-Z0-9_]*" ""print("Found a ID")""

NUMBER "\d+(\.\d+)?" ""t.value = float(t.value)""
error   ""error(f"Illegal character {t.value[0]}"); t.lexer.skip(1)"" 

%% YAcc
%precedence = [(+,-,),(*,/),(,UMINUS)]
# symboltable : dictionary of variables
ts = { }
'''

#Store the last state that the parser is
lastState = ""

tokens =[
    "LEX","YACC","COMMENTARY",
    "COMMENTARYTOKEN",
    "LITERALS","TOKENS","IGNORE","PRECEDENCE",
    "STR_ATRIB","TOKEN_ID",
    "CODE_EXPRESSION"]

literals = ['=','+','-',"'",'"','[',']','(',')']

t_ignore = ' \t\r'

states = [
    ("LEXSTATE","inclusive"),
    ("YACCSTATE","inclusive"),
    ("COMMENTARYSTATE","inclusive")
]

def t_COMMENTARY(t):
    r'//'
    t.lexer.begin("COMMENTARYSTATE")
    return t

def t_COMMENTARYSTATE_COMMENTARYTOKEN(t):
    r'.+'
    return t

def t_LEX(t):
    r'%%\s*(?i)LEX'
    t.lexer.begin("LEXSTATE")
    lastState = "LEXSTATE"
    return t


def t_YACC(t):
    r'%%\s*(?i)YACC'
    t.lexer.begin("YACCSTATE")
    lastState = "YACCSTATE"
    return t

def t_YACCSTATE_PRECEDENCE(t):
    r'%precedence'
    return t

def t_LEXSTATE_LITERALS(t):
    r'%literals'
    return t

def t_LEXSTATE_IGNORE(t):
    r'%ignore'
    return t

def t_LEXSTATE_TOKENS(t):
    r'%tokens'
    return t

def t_LEXSTATE_CODE_EXPRESSION(t):
    r'"".*""'
    return t

def t_LEXSTATE_STR_ATRIB(t):
    r'".+?"'
    return t


def t_LEXSTATE_TOKEN_ID(t):
    r'\n\w+'
    return t

def t_error(t):
    if (t.value[0] != '\n'):
        print("Wrong character!", t.value[0])
    else:
        t.lexer.begin(lastState)
    t.lexer.skip(1)


lexer = lex.lex()


lexer.input(str_Input)

print(str_Input)
print("\nStarting Parsing")

for tok in lexer:
    print(tok)

# import sys

# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)