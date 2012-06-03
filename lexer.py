__all__ = ("lexer","tokens")

tokens = ( "LPAREN","RPAREN", "RBRACKET", "LBRACKET", "NUMBER", "COMMA", "COLON", "ATTR")

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_NUMBER = r"-?\d+\.\d+E-?\d+|-?\d+\.\d+|\d+"
t_COMMA = ","
t_COLON = ":"
#t_ATTR = r"\[[\w,\.&%{}\-=_]+\]"
t_ATTR = r"\[[^]]*\]"


#def t_NUMBER(t):
#    r'\d+'
#    try:
#        t.value = int(t.value) except ValueError: print("Integer value too large %d", t.value) t.value = 0 return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()
