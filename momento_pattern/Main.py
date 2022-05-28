from Editor import Editor
from Histoty import History

editor = Editor()
history = History()

editor.content = 'a'
history.push(editor.create_state())

editor.content = 'c'
history.push(editor.create_state())

editor.content = 'd'
editor.restore(history.pop())

print(editor.content)
