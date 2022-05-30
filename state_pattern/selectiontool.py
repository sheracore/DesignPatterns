from tool import Tool


class SelesionTool(Tool):

    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Drwa a dashed rectangle")