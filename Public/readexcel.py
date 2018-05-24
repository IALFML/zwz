import  xlrd
file_url="C:/Users/admin/PycharmProjects/python/Test_project/Datebase/logindata.xlsx"

def open_excel(file=file_url):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

# def excel_table_byindex(file=file_url, colnameindex=0, by_index=0):
#     data = open_excel(file)
#     table = data.sheets()[by_index]
#     nrows = table.nrows
#     colnames = table.row_values(colnameindex)
#     list = []
#     for rownum in range(1, nrows):
#         row = table.row_values(rownum)
#         if row:
#             app = {}
#             for i in range(len(colnames)):
#                 app[colnames[i]] =row[i]
#             list.append(app)
#     return list


def excel_data(file=file_url, colnameindex=0, by_index=0):

    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []

    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                # app[colnames[i]] =row[i]
                type = table.cell_type(rownum,i)
                name = table.cell_value(rownum,i)
                if type == 0:#空0
                    name = ""
                elif type == 1:#字符串1
                    name = name
                elif type == 2 and name%1==0:#数字2
                    name = int(name)
                elif type == 3:#日期3
                    date_value = xlrd.xldate_as_tuple(name,0)
                    name = datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
                elif type == 4:#布尔4
                    if name == 1:
                        name = True
                    else:
                        name =False
                elif type == 5:#error 5
                    name = error
                app[colnames[i]]=name
            list.append(app)
    return list


if __name__=="__main__":
    print(excel_data(file_url,0))





