from tool import Tool


class SelesionTool(Tool):

    def mouse_down(self):
        print("Brush icon")

    def mouse_up(self):
        print("Draw a line")