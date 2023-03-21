from reportlab.lib.colors import black
from reportlab.platypus import Flowable


class LineSeparator(Flowable):
    def __init__(self, width=0, height=0, thickness=1, color=black):
        super().__init__()
        self.width = width
        self.height = height
        self.thickness = thickness
        self.color = color

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        x_start = self.canv._x
        y_start = self.canv._y + self.height / 2
        x_end = x_start + self.width
        y_end = y_start
        self.canv.line(x_start, y_start, x_end, y_end)

    def wrap(self, available_width, available_height):
        return self.width, self.height


