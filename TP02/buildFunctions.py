
def buildFunctionLEX(token,regex,code):
    str_first = "def t_"+token+"(t):\n\t"

    str_regex=""
    #There needs to be content to apply the regex 
    if (regex != ""):
        str_regex = "r'"+regex+"'\n\t"
    
    code = code.split(";")
    str_code = ""
    for piece in code:
        str_code += piece.strip() +"\n\t"
    
    str_end = "return t\n"
    return str_first + str_regex + str_code + str_end

def buildLexerInitial():
    return """#-------------------
# Lexer Code
#-------------------

import ply.lex as lex
"""

def buildLexerEnd():
    return "\nlexer = lex.lex()\n"

def buildYaccInitial():
    return """#-------------------
# Yacc Code
#-------------------

import ply.yacc as yacc
"""

def buildYaccEnd():
    return"""
parser = yacc.yacc()
parser.parse("5+5")
"""
