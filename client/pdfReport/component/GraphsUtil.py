import io

import PIL
import numpy as np
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Table, TableStyle, Image


class GraphsUtil:
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
            paragraphs.append(GraphsUtil.draw_text(line))
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

    @staticmethod
    def draw_list(data,width,n):
        data = [data[i:i + n] for i in range(0, len(data), n)]
        t = Table(data)

        # 设置Table样式
        t.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),
        ]))

        # 设置每行的列宽
        col_width = width / n
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
