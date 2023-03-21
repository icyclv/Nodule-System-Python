import io
import os
import time
from functools import partial

import PIL
import cv2
import numpy as np
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm, inch, mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, Frame, ListFlowable, \
    ListItem, KeepTogether, Flowable, FrameSplitter, PageTemplate, BaseDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import CMYKColor, black, Color


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




class Graphs:
    # 绘制标题
    @staticmethod
    def draw_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Title']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 14  # 字体大小
        ct.leading = 12  # 行间距
        ct.textColor = colors.black  # 字体颜色
        ct.alignment = 1  # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    @staticmethod
    def draw_subTitle(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Title']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 12  # 字体大小
        ct.leading = 12  # 行间距
        ct.textColor = colors.black  # 字体颜色
        ct.alignment = 1  # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制小标题
    @staticmethod
    def draw_little_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Normal']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 12  # 字体大小
        ct.leading = 15  # 行间距
        ct.bold = True
        ct.textColor = colors.black  # 字体颜色
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制普通段落内容
    @staticmethod
    def draw_text(text: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 10
        ct.wordWrap = 'CJK'  # 设置自动换行
        ct.alignment = 0  # 左对齐
        ct.firstLineIndent = ct.fontSize * 2  # 第一行开头空格
        ct.leading = 12
        return Paragraph(text, ct)

    @staticmethod
    def draw_paragraphs(text: str,sep='\n'):
        lines = text.split(sep)
        paragraphs = []
        for line in lines:
            paragraphs.append(Graphs.draw_text(line))
        return paragraphs

    # 绘制表格
    @staticmethod
    def draw_table(data):
        # 列宽度
        style = [
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
            ('FONTSIZE', (0, 0), (-1, 0), 10),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
            # ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
            # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
            # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
            # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
            # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
        ]
        table = Table(data, style=style)
        return table

    # 创建图表
    @staticmethod
    def draw_bar(bar_data: list, ax: list, items: list):
        drawing = Drawing(500, 250)
        bc = VerticalBarChart()
        bc.x = 45  # 整个图表的x坐标
        bc.y = 45  # 整个图表的y坐标
        bc.height = 200  # 图表的高度
        bc.width = 350  # 图表的宽度
        bc.data = bar_data
        bc.strokeColor = colors.black  # 顶部和右边轴线的颜色
        bc.valueAxis.valueMin = 5000  # 设置y坐标的最小值
        bc.valueAxis.valueMax = 26000  # 设置y坐标的最大值
        bc.valueAxis.valueStep = 2000  # 设置y坐标的步长
        bc.categoryAxis.labels.dx = 2
        bc.categoryAxis.labels.dy = -8
        bc.categoryAxis.labels.angle = 20
        bc.categoryAxis.categoryNames = ax

        # 图示
        leg = Legend()
        leg.fontName = 'SimSun'
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = 475  # 图例的x坐标
        leg.y = 240
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = items
        drawing.add(leg)
        drawing.add(bc)
        return drawing
    @staticmethod
    def draw_list(data,n):
        data = [data[i:i + n] for i in range(0, len(data), n)]
        t = Table(data)

        # 设置Table样式
        t.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),
        ]))

        # 设置每行的列宽
        col_width = doc.width / n
        t._argW = [col_width] * n
        return t

    # 绘制图片
    @staticmethod
    def draw_img(file=None, width=4 * cm):
        if isinstance(file, np.ndarray):
            img = PIL.Image.fromarray(file)
        else:
            img = PIL.Image.open(file)
        size = img.size
        buf = io.BytesIO()
        img.save(buf, format='JPEG')
        buf.seek(0)

        img = Image(buf)  # 读取指定路径下的图片
        img.drawWidth = width  # 设置图片的宽度
        img.drawHeight = (size[1] / size[0] * 4) * cm  # 设置图片的高度
        # img.hAlign = hAlign
        return img


def footer(canvas, doc,time=None):
    canvas.saveState()

    x_start = doc.leftMargin
    y_start = 70
    x_end = x_start + doc.width
    y_end = y_start
    canvas.line(x_start, y_start, x_end, y_end)
    canvas.setFont('SimSun', 10)
    canvas.drawString(x_start, 50, "诊断医师: ____________________")
    canvas.drawString(x_start+250, 50, "审核医师: ____________________")
    canvas.drawString(x_start, 30, "报告时间: %s" % time)
    canvas.setFont('SimSun', 8)
    canvas.drawString(x_start, 20, "注:本报告仅供临床医师参考")


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
        y_start = 70
        x_end = x_start + self.width
        y_end = y_start
        self.line(x_start, y_start, x_end, y_end)
        self.setFont('SimSun', 10)
        self.drawString(x_start, 50, "诊断医师: ____________________")
        self.drawString(x_start + 250, 50, "审核医师: ____________________")
        self.drawString(x_start, 30, "报告时间: %s" % self.time)
        self.setFont('SimSun', 8)
        self.drawString(x_start, 20, "注:本报告仅供临床医师参考")

if __name__ == '__main__':
    # 创建内容对应的空列表
    cur_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../src/resources/simsun.ttc")
    pdfmetrics.registerFont(TTFont('SimSun', "../src/resources/simsun.ttc"))
    content = list()
    title = 'xxx医院'
    subTitle = 'AI智能分析系统报告'

    doc = SimpleDocTemplate('report.pdf', pagesize=A4, topMargin=20)
    # #
    # page_template = PageTemplate(id='my_page_template',frames=[
    # Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='frame1')],
    #                              onPage=MyPageTemplate(doc))
    #
    # doc.addPageTemplates([page_template])
    content.append(Graphs.draw_title(title))
    content.append(Graphs.draw_subTitle(subTitle))

    line = LineSeparator(width=doc.width, height=0.1 * inch, thickness=1, )
    content.append(line)



    patient_data = {
        '姓名': '张三',
        '性别': '男',
        '检测时间': '2023-03-16 10:30',
        '科室': '放射科',
        '床位': 'A101',
    }
    patient_list = [key + ":" + value for key, value in patient_data.items()]

    content.append(Graphs.draw_list(patient_list, 3))
    content.append(line)

    data = [
        ['序号', '坐标', '置信度',"直径", '类别','恶性概率'],
        ['1', 'x: 1.2, y: 1.2, z: 1.2', '0.99', '1.2cm', '恶性', '0.99'],
        ['2', 'x: 1.2, y: 1.2, z: 1.2', '0.99', '1.2cm', '恶性', '0.99'],
    ]

    content.append(Graphs.draw_little_title("结节信息"))
    content.append(Graphs.draw_table(data))
    content.append(line)


    # 添加图片
    img1 = cv2.imread('hh.jpg')
    img2 = 'h2.jpg'
    img3 = 'h3.jpg'
    spacing = Spacer(1, 0.1 * inch)
    # 3张图片同一行显示，图片之间的间距为10
    data = [[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],[img1, img2, img3],]
    for i in range(len(data)):
        d = [ Graphs.draw_img(t) for t in data[i]]
        content.append(Graphs.draw_little_title("结节{}".format(i+1)))
        table = Table([d], rowHeights=[max(max(d[0].drawHeight, d[1].drawHeight), d[2].drawHeight)], hAlign='CENTER')
        content.append(table)
        content.append(spacing)


    content.append(line)
    content.append(Graphs.draw_little_title("影像所见"))
    content.extend(Graphs.draw_paragraphs("左侧第7前肋骨折,断端稍分离，未见明显移位:左侧第8前助内侧皮质连续性中断:\n左侧第9肋腋部骨折，断端重叠约16mm;第10后肋骨折，断端-顿,重叠约6mm."))

    content.append(line)
    content.append(Graphs.draw_little_title("诊断意见"))
    content.extend(Graphs.draw_paragraphs("左侧第7前肋骨折,断端稍分离，未见明显移位:左侧第8前助内侧皮质连续性中断:左侧第9肋腋部骨折，断端重叠约16mm;第10后肋骨折，断端-顿,重叠约6mm."))
    # 生成pdf文件

    doc.build(content,canvasmaker=partial(FooterCanvas, leftMargin=doc.leftMargin,width=doc.width,time='2020-03-16 10:30'))