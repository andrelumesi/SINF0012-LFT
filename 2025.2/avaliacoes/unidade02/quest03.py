import ply.lex as lex
import ply.yacc as yacc
import quest04 as sa

# List of token names.   This is always required
tokens = (
   'NUM',
   'CIRCUNFLEXO',
   'ABREPAREN',
   'FECHAPAREN',
   'ID',
   'SHIFT',
   'HASH',
   'EXCLAMACAO'
)

# Regular expression rules for simple tokens
t_CIRCUNFLEXO    = r'\^'
t_ABREPAREN = r'\('
t_FECHAPAREN  = r'\)'
t_ID = '[A-Z]+'
t_NUM = '[1-7][0-7]*' 
t_SHIFT = '>>'
t_HASH = '\\#'
t_EXCLAMACAO = '!'
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
data = '''BCA >> BCA # !11111'''
lexer.input(data)

# tok = lexer.token()
# while (tok):
#     print (tok.value, tok.type)
#     tok =  lexer.token()


# excmd -> excmd ^ excmd            | excmd # excmd         | id        
#                | excmd >> excmd         | ! num                         | id ( excmd )   


def p_excmd_hash1(p):
    'excmd1 : excmd2 HASH excmd1'
    p[0]=sa.ExcmdHash(p[1], p[3])

def p_excmd_hash2(p):
    'excmd1 : excmd2'
    p[0] = p[1]

def p_excmd_circunflexo1(p):
    'excmd2 : excmd2 CIRCUNFLEXO excmd3'
    p[0]=sa.ExcmdCircunflexo(p[1], p[3])


def p_excmd_circunflexo2(p):
    'excmd2 : excmd3'
    p[0] = p[1]


def p_excmd_shift1(p):
    'excmd3 : excmd3 SHIFT excmd4'
    p[0]=sa.ExcmdShift(p[1], p[3])


def p_excmd_shift2(p):
    'excmd3 : excmd4'
    p[0] = p[1]


def p_excmd_notNum1(p):
    'excmd4 : EXCLAMACAO NUM'
    p[0]=sa.ExcmdNotNum(p[2])

def p_excmd_notNum2(p):
    'excmd4 : excmd5'
    p[0] = p[1]


def p_excmd_ID(p):
    'excmd5 : ID'
    p[0]=sa.ExcmdId(p[1])

def p_excmd_call(p):
    'excmd5 : ID ABREPAREN excmd1 FECHAPAREN'
    p[0]=sa.Excmdcall(p[1], p[3])

parser = yacc.yacc()

result = parser.parse(debug=True)
