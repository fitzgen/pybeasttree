# Ast data structure
class Tree(object):
    def __init__(self, children = None, id = None, length = None):
        self.children = children
        self.length = length
        self.id = set()

        if children and id:
            raise TypeError(
                "Invalid arguments: Tree.__init__ takes either children or an id, not both")
        elif not (children or id):
            raise TypeError(
                "Invalid arguments: Tree.__init__ must be called with either children or an id")
        elif children:
            self.id.update(*(child.id for child in self.children))
        else: # id
            self.id.add(id)

    def depth_first(self):
        pass
