from canvas import Canvas
from selectiontool import SelesionTool
from erasertool import EraserTool

if __name__ == '__main__':
    canvas = Canvas()
    # canvas.set_current_tool(EraserTool())
    canvas.set_current_tool(SelesionTool())
    canvas.mouse_up()
    canvas.mouse_down()

