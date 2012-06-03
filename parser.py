import sys
from lexer import lexer, tokens

start = "tree"

from ast import Tree

def p_tree(t):
    """
    tree : node metadata COLON NUMBER
         | node metadata
    """
    branch_length = None
    if len(t) == 5:
        branch_length = t[4]

    if type(t[1]) == list:
        t[0] = Tree(children = t[1], length = branch_length)
    else:
        t[0] = Tree(id = t[1], length = branch_length)

def p_node(t):
    """
    node : NUMBER
         | LPAREN tree_list RPAREN
    """
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]


def p_tree_list(t):
    """
    tree_list : tree
              | tree COMMA tree_list
    """
    if len(t) == 4:
        t[0] = t[3]
        t[0].insert(0, t[1])
    else:
        t[0] = [t[1]]



def p_metadata(t):
    """
    metadata : ATTR
    """

    #t[0] = {}
    # Eventually return a key value dictionary.
    t[0] = t[1]

def p_error(t):
    #print("Syntax error at '%s'" % t.value)
    print("Syntax error at '%s'" % t)

import ply.yacc as yacc
yacc.yacc()

if __name__ == "__main__":
    tree_file = open(sys.argv[1], "r")
    contents = tree_file.read()
    for line in contents.splitlines():
        if line.startswith("tree"):
            tree = yacc.parse(line[18:-1], lexer=lexer)
            for id in tree.depth_first():
                print id
