import io
import os

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
    ListItem, KeepTogether, Flowable,FrameSplitter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.colors import CMYKColor, black, Color


class LineSeparator(Flowable):
    def __init__(self, width=0, height=0, thickness=1, color=black):
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
        ct.leading = 12  # 行间距
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
        ct.firstLineIndent = ct.fontSize*2  # 第一行开头空格
        ct.leading = 12
        return Paragraph(text, ct)

    # 绘制表格
    @staticmethod
    def draw_table(*args):
        # 列宽度
        col_width = 120
        style = [
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
            ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
            # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
            # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
            # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
            # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
        ]
        table = Table(args, colWidths=col_width, style=style)
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

    # 绘制图片
    @staticmethod
    def draw_img(path=None,np_file=None,width=4 * cm ):
        if path is None:
            PIL_img = PIL.Image.fromarray(np_file)
        else:
            PIL_img = PIL.Image.open(path)

        buf = io.BytesIO()
        PIL_img.save(buf, format='JPEG')
        buf.seek(0)

        img = Image(buf)  # 读取指定路径下的图片
        img.drawWidth = width # 设置图片的宽度
        img.drawHeight = (data.shape[1]/data.shape[0] * 4) * cm  # 设置图片的高度
        # img.hAlign = hAlign
        return img


if __name__ == '__main__':
    # 创建内容对应的空列表
    content = list()
    title = 'xxx医院'
    subTitle = 'AI智能分析系统报告'

    doc = SimpleDocTemplate('report.pdf', pagesize=A4, topMargin=10)
    cur_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../src/resources/simsun.ttc")
    pdfmetrics.registerFont(TTFont('SimSun',cur_path ))
    # 添加标题
    content.append(Graphs.draw_title(title))
    content.append(Graphs.draw_subTitle(subTitle))

    line = LineSeparator(width=doc.width, height=1 * inch, thickness=1, )

    # 添加图片
    img1 = Graphs.draw_img('h2.jpg')
    img2 = Graphs.draw_img('h2.jpg')
    img3 = Graphs.draw_img('h2.jpg')
    #3张图片同一行显示，图片之间的间距为10
    data = [[img1, img2, img3]]
    table = Table(data, rowHeights=[max(max(img1.drawHeight,img2.drawHeight),img3.drawHeight)], hAlign='CENTER')
    spacing = Spacer(1, 0.2 * inch)
    # 定义表格的样式，使其水平居中和垂直居中
    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ])
    table.setStyle(table_style)
    content.append(table)
    content.append(line)
    # 添加段落文字
    content.append(Graphs.draw_text(
        '众所周知，大数据分析师岗位是香饽饽，近几年数据分析热席卷了整个互联网行业，与数据分析的相关的岗位招聘、培训数不胜数。很多人前赴后继，想要参与到这波红利当中。那么数据分析师就业前景到底怎么样呢？'))
    # 添加小标题
    content.append(Graphs.draw_title(''))
    content.append(Graphs.draw_little_title('不同级别的平均薪资'))
    content.append(line)
    content.append(spacing)
    # 添加表格
    data = [
        ('职位名称', '平均薪资', '较上年增长率'),
        ('数据分析师', '18.5K', '25%'),
        ('高级数据分析师', '25.5K', '14%'),
        ('资深数据分析师', '29.3K', '10%')
    ]

    patient_data = {
        '姓名': '张三',
        '性别': '男',
        '检测时间': '2023-03-16 10:30',
        '科室': '放射科',
        '床位': 'A101',
    }
    patient_list = [key+" : "+value for key, value in patient_data.items()]
    n = 3
    patient_rows = [patient_list[i:i + n] for i in range(0, len(patient_list), n)]

    # 创建Table对象

    elements = []
    t = Table(patient_rows)

    # 设置Table样式
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),
    ]))

    # 设置每行的列宽
    col_width = doc.width / n
    t._argW = [col_width] * n

    content.append(t)

    content.append(Graphs.draw_table(*data))

    #添加黑色分割线
    
    # 生成图表
    content.append(Graphs.draw_title(''))
    content.append(Graphs.draw_little_title('热门城市的就业情况'))
    b_data = [(25400, 12900, 20100, 20300, 20300, 17400), (15800, 9700, 12982, 9283, 13900, 7623)]
    ax_data = ['BeiJing', 'ChengDu', 'ShenZhen', 'ShangHai', 'HangZhou', 'NanJing']
    leg_items = [(colors.red, '平均薪资'), (colors.green, '招聘量')]
    content.append(Graphs.draw_bar(b_data, ax_data, leg_items))

    # 生成pdf文件


    doc.build(content)