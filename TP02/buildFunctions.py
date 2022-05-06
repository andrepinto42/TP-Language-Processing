
def buildFunctionLEX(token,regex,code):
    str_first = "def t_"+token+"(t):\n\t"

    str_regex=""
    #There needs to be content to apply the regex 
    if (regex != ""):
        str_regex = "r'"+regex+"'\n\t"
    
    code = code.split(";")
    str_code = ""
    for piece in code:
        str_code += piece +"\n\t"
    
    str_end = "return t\n"
    return str_first + str_regex + str_code + str_end

def buildDefault():
    return "import ply.lex as lex\n"

def buildEnd():
    return "\nlexer = lex.lex()\n"