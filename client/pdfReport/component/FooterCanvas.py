from reportlab.pdfgen import canvas


class FooterCanvas(canvas.Canvas):
    def __init__(self, *args,leftMargin,width,time, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.leftMargin = leftMargin
        self.width = width
        self.time = time
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for i in range(len(self._saved_page_states)):
            state = self._saved_page_states[i]

            self.__dict__.update(state)
            if i == len(self._saved_page_states)-1:
                self.add_footer()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def add_footer(self ):
        x_start = self.leftMargin
        y_start = 90
        x_end = x_start + self.width
        y_end = y_start
        self.line(x_start, y_start, x_end, y_end)
        self.setFont('SimSun', 10)
        self.drawString(x_start, 50, "诊断医师: ____________________")
        self.drawString(x_start + 250, 50, "审核医师: ____________________")
        self.drawString(x_start, 30, "报告时间: %s" % self.time)
        self.setFont('SimSun', 8)
        self.drawString(x_start, 20, "注:本报告仅供临床医师参考")