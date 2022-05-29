from tooltype import ToolType

class Canvas:
    def __init__(self, tool_type):
        self.tool_type = ToolType


    def mouse_down(self):
        if self.tool_type == ToolType.SELECTION:
            print("Selection icon")
        if self.tool_type == ToolType.BRUSH:
            print("Brush icon")
        if self.tool_type == ToolType.ERASER:
            print("Eraser icon")

    def mouse_up(self):
        if self.tool_type == ToolType.SELECTION:
            print("Draw dashed rectangle")
        if self.tool_type == ToolType.BRUSH:
            print("Deaw a line")
        if self.tool_type == ToolType.ERASER:
            print("Erase somthing")
