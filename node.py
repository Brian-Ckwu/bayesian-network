# Diagnosis: 1, 0, -1 three values?

class Node(object):
    def __init__(self, name: str, index: int, parents: list = [], children: list = []):
        self._name = name
        self._id = index
        self._parents = parents
        self._children = children
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name
    
    @property
    def parents(self):
        return self._parents
    
    @property
    def children(self):
        return self._children

if __name__ == "__main__":
    node = Node("cough", 0)
    print(node.name)
    node.name = "H"
    print(node.name)
    print(node._name)