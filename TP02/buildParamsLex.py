import ply.lex as lex


literals_captured = []


tokens =[
    "YACC","GRAMMAR_OPEN",
    "GRAMMAR_CLOSE",
    "LITERAL","D_POINT",
    "WORD"
]

t_ignore = ' \t\r\n'

states = [
    ("YACCSTATE","inclusive"),
    ("GRAMMARSTATE","inclusive")
]

def t_YACC(t):
    r'%%\s*(?i)YACC'
    t.lexer.begin("YACCSTATE")
    return t

def t_YACCSTATE_GRAMMAR_OPEN(t):
    r'\%""'
    t.lexer.begin("GRAMMARSTATE")
    return t


def t_GRAMMARSTATE_GRAMMAR_CLOSE(t):
    r'""'
    t.lexer.begin("YACCSTATE")
    return t

# valid "+" '.'
# invalid "+'
def t_GRAMMARSTATE_LITERAL(t):
    # r"(['\"]).\1"
    r"(\".\")|('.')"
    literals_captured.append(t.value[1])
    return t

def t_GRAMMARSTATE_WORD(t):
    r"\w+"
    return t

def t_GRAMMARSTATE_D_POINT(t):
    r":"
    return t


def t_default(t):
    r'.'
    t.lexer.skip(1)


def t_error(t):
    print("Error at",t.value[0])
    t.lexer.skip(1)


def run():
    lexer = lex.lex()

    #Carregar o conteudo a partir de um ficheiro
    str_Input = open("input_PLY_SIMPLE.txt").read()
    lexer.input(str_Input)

    print("\nStarting Parsing First ITERATION")

    for tok in lexer:
        pass

    print(literals_captured)
