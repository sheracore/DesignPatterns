from EditorState import EditorState


class Editor:
    def __init__(self):
        self._content = ""

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

    def create_state(self):
        return EditorState(self._content)

    def restore(self, state):
        self._content = state.get_content()
