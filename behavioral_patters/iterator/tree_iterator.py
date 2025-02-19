class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration

def traverse_in_order(root):
  def traverse(current):
    if current.left:
      for left in traverse(current.left):
        yield left
    yield current
    if current.right:
      for right in traverse(current.right):
        yield right
  for node in traverse(root):
    yield node


""" My Approach """
def traverse(node):
    if node.left:
        yield from traverse(node.left)
    yield node.value
    if node.right:
        yield from traverse(node.right)


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1,
                Node(2),
                Node(3))

    #     1
    #    / \
    #   2   3
    #  / \   \
    # 10  20  30

    root2 = Node(1,
                Node(2, Node(10), Node(20)),
                Node(3, right=Node(30)))

    it = iter(root)

    print([next(it).value for x in range(3)])

    for x in root:
        print(x.value)

    for y in traverse_in_order(root2):
        print(y.value)


"""
Generator practises
"""

class GeneratorTest:
    def __init__(self, list_of_legends):
        self.list_of_legends = list_of_legends

    def generator(self):
        for legend in self.list_of_legends:
            if legend == 'cvj':
                continue
            yield legend
        for x in range(5):
            yield str(x) + "__@@@"
        yield 10
        yield 20
        yield 43


t = GeneratorTest(list_of_legends=['asdf','bukh','cvj','dtry','evh'])
for x in t.generator():
    print(x)


class Grok:
    def __init__(self, list_of_groks):
        self.list_of_groks = list_of_groks

    def __iter__(self):
        return GrokIterator(self.list_of_groks)

class GrokIterator:
    def __init__(self, list_of_groks):
        self.inx = 0
        self.list_of_groks = list_of_groks

    def __next__(self):
        if self.inx < len(self.list_of_groks):
            res = self.list_of_groks[self.inx]
            self.inx += 1
            return res
        raise StopIteration

g = Grok(list_of_groks=['asdf','bukh','cvj','dtry','evh'])
for l in g:
    print(l)


class GrokB:
    def __init__(self, list_of_groks):
        self.inx = 0
        self.list_of_groks = list_of_groks

    def __iter__(self):
        return self

    def __next__(self):
        if self.inx < len(self.list_of_groks):
            res = self.list_of_groks[self.inx]
            self.inx += 1
            return res
        raise StopIteration



g = GrokB(list_of_groks=['a','ff','gg','hh','jj'])
for l in g:
    print(l)