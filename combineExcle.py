import xlrd
import xlwt
import setBorder
import handleFile



def getStyle(stype):

    # 表头
    if stype == "title":
        # 字体格式
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 16 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.horz = 0x02
        align.vert = 0x01
        style.alignment = align
        return style

        # 表头
    if stype == "title1":
        # 字体格式
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 14 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.horz = 0x02
        align.vert = 0x01
        style.alignment = align
        return style
    #单元格格式
    if stype == "cell":
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 11 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.vert = 0x01
        style.alignment = align
        return style



# 解析json并将内容输出到邮件
def saveExcleOnDay(sheet,workbook,var):
    # now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 创建一个worksheet
    worksheet = workbook.add_sheet(sheet.name)
    for i in range(0,3):
        first_col = worksheet.col(i*3)  # 获取第一列
        first_col.width = 256 * 20  # 设置第一列列宽
    tall_style = xlwt.easyxf('font:height 400')  # 设置行高
    worksheet.write_merge(0, 0, 0, 8, "幼鲜知价格表（" + sheet.name + "）            单位：元/斤",getStyle("title"))
    worksheet.write_merge(1, 1, 0, 2, "幼鲜知蔬菜价格表",getStyle("title1"))
    worksheet.write_merge(1, 1, 3, 5, "幼鲜知肉禽价格表",getStyle("title1"))
    worksheet.write_merge(1, 1, 6, 8, "幼鲜知水果价格表",getStyle("title1"))
    for i in range(0,2):
        row = worksheet.row(i)
        row.set_style(tall_style)  # 设置行高
    for index in range(2, sheet.nrows):
        row = sheet.row(index)
        for j, cell in enumerate(row):
            worksheet.write(index,j,cell.value,getStyle("cell"))
            first_row = worksheet.row(index)
            first_row.set_style(tall_style)  # 设置行高

def combineExcle():
        # 往前获取一周的文件
        wbs = []
        paths = handleFile.getDatePath(True)
        for i in paths:
            try:
                xlrd.open_workbook(i)
                wbs.append(xlrd.open_workbook(i))
            except:
                pass
        begin = wbs[0].sheet_by_index(0).name
        end = wbs[len(wbs) - 1].sheet_by_index(0).name
        workbook = xlwt.Workbook(style_compression=2)
        for b, i in enumerate(wbs):
            saveExcleOnDay(i.sheet_by_index(0), workbook, b)
        workbook.save(begin + "--" + end + ".xls")
        return begin + "--" + end + ".xls"
if __name__ == "__main__":
    combineExcle()