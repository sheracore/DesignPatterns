from tool import Tool


class EraserTool(Tool):

    def mouse_down(self):
        print("Eraser icon")

    def mouse_up(self):
        print("Erase somthing")