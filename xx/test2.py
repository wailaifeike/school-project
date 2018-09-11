# _*_ coding:utf-8 _*_
import os, sys, sqlite3, string
from xlrd import open_workbook

cx = sqlite3.connect("check.db")
cu = cx.cursor()
cu.execute("""create table movieBook2 (id integer primary key,
                                      numMovie integer,
                                      chineseName text,
                                      size real,
                                      enName,
                                      typeMovie,
                                      pubYear,
                                      soundChanl,
                                      movieScore real,
                                      movieActor text,
                                      movieDirector text,
                                      summary text
                                )""")

excelName = "a.xlsx"

bk = open_workbook(excelName, encoding_override="utf-8")
for s in bk.sheets():
    print("sheet:", s.name)

try:
    sh = bk.sheet_by_name("1080PRip")
except:
    print
    "no sheet in %s named sheet1" % excelName
    nrows = sh.nrows - 16
    ncols = sh.ncols
    print
    os.getcwd(), "nrows %d,ncols %d" % (nrows, ncols)
    # cell_value = sh.cell_value(0,12)
    print(sh.cell_value(3163, 1))
    row_list = []
    print
    "开始导入------------------->>>>>>>"
    for i in range(1, nrows):
        row_date = sh.row_values(i)
        row_list.append(row_date)
        n = i - 1
        cx.execute(
            "insert into movieBook(numMovie,chineseName,size,enName,typeMovie,pubYear,soundChanl,movieScore,movieActor,movieDirector,summary)values (?,?,?,?,?,?,?,?,?,?,?)",
            (int(row_list[n][0]), row_list[n][1], row_list[n][2], row_list[n][3], row_list[n][4], row_list[n][5],
             row_list[n][6], row_list[n][7], row_list[n][8], row_list[n][9], row_list[n][10]))
        cx.commit()
        # print row_list[n][4]
    cu.close()
    print
    "导入完成------------------->>>>>>>"
    # print len(row_list[3])

