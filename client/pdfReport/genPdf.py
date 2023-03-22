import os
from functools import partial

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, Spacer

from pdfReport.component.FooterCanvas import FooterCanvas
from pdfReport.component.GraphsUtil import GraphsUtil
from pdfReport.component.LineSeparator import LineSeparator

pdfmetrics.registerFont(TTFont('SimSun',  "./resources/simsun.ttc"))



def genPDF(pdf_config,file_name,time_str=None,patient_info=None,nodule_info=None,nodule_imgs=None,appearance=None,diagnosis=None):
    content = list()
    doc = SimpleDocTemplate(file_name, pagesize=A4, topMargin=20)
    # 标题
    title = pdf_config['title']
    subTitle = pdf_config['subTitle']
    line = LineSeparator(width=doc.width, height=0.1 * inch, thickness=1, )
    spacing = Spacer(1, 0.1 * inch)
    text_spacing= Spacer(1, 0.5 * inch)
    content.append(GraphsUtil.draw_title(title))
    content.append(GraphsUtil.draw_subTitle(subTitle))
    content.append(line)

    # 病人信息
    if pdf_config['showInfo'] == True and len(patient_info) > 0:

        content.append(GraphsUtil.draw_list(patient_info,doc.width, 3))
        content.append(line)

    #结节信息
    if pdf_config['showTable'] == True and len(nodule_info) > 1:
        content.append(GraphsUtil.draw_little_title("结节信息"))
        content.append(GraphsUtil.draw_table(nodule_info))
        content.append(line)

    #结节图像
    if pdf_config['showImage'] == True and len(nodule_imgs) > 0:
        content.append(GraphsUtil.draw_little_title("结节图像"))
        content.append(spacing)

        for i in range(len(nodule_imgs)):

            d = [GraphsUtil.draw_img(t) for t in nodule_imgs[i]]
            content.append(GraphsUtil.draw_little_title("结节{}".format(i + 1),10))
            content.append(spacing)
            table = Table([d], rowHeights=[max(max(d[0].drawHeight, d[1].drawHeight), d[2].drawHeight)],
                          hAlign='CENTER')
            content.append(table)
            content.append(spacing)
        content.append(line)

    #
    if pdf_config['showAppearance'] == True:
        content.append(GraphsUtil.draw_little_title("影像所见"))
        content.extend(GraphsUtil.draw_paragraphs(appearance))
        content.append(text_spacing)
    if pdf_config['showDiagnosis'] == True:
        content.append(GraphsUtil.draw_little_title("诊断意见"))
        content.extend(GraphsUtil.draw_paragraphs(diagnosis))

    if pdf_config['showFooter'] == True:
        doc.build(content, canvasmaker=partial(FooterCanvas, leftMargin=doc.leftMargin, width=doc.width,
                                               time=time_str))
    else:
        doc.build(content)




