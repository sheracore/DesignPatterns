from tool import Tool

class Canvas:
    def __init__(self):
        self._tool = Tool

    def mouse_down(self):
        self._tool.mouse_down()

    def mouse_up(self):
        self._tool.mouse_up()

    def get_current_tool(self):
        return self._tool

    def set_current_tool(self, tool):
        self._tool = tool