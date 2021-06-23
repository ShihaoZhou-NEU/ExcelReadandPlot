import matplotlib.pyplot as plt
import xlrd
import pandas as pd

csv_data = pd.read_csv('plaque-5-force-contrainte-deformation.csv',header=None)  # 读取CSV
# file = 'plaque-2-force-contrainte-deformation.xlsx'
# wb = xlrd.open_workbook(filename=file)  # 打开文件
# print(wb.sheet_names())  # 获取所有表格名字
# print(csv_data[22])
# col_0 = csv_data[22]

# sheet1 = wb.sheet_by_name('Force-Deplacement')  # 通过名字获取表格
# sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
# col_0 = sheet1.col_values(0)  # 获取列内容
# col_1 = sheet1.col_values(1)


def removeNULL(col):
    NotNullCol = []
    for item in col:
        if item != '':
            NotNullCol.append(item)
        else:
            break
    return NotNullCol

def removeNULL_csv(col):
    NotNullCol = []
    for item in col:
        if pd.isnull(item):
            break
        else:
            NotNullCol.append(item)
            
    return NotNullCol


# col_0 = removeNULL_csv(col_0)
# col_1 = removeNULL(col_1)
# print(col_0)

# 画图


def getData(i, j):
    col_i = sheet1.col_values(i)  # 获取列内容
    col_j = sheet1.col_values(j)
    col_i = removeNULL(col_i)
    col_j = removeNULL(col_j)
    return col_i, col_j

def getDatafromCSV(i, j):
    col_i = csv_data[i]  # 获取列内容
    col_j = csv_data[j]
    col_i = removeNULL_csv(col_i)
    col_j = removeNULL_csv(col_j)
    return col_i, col_j

def drawPicture(i, j, shift):
    col_i, col_j = getData(i, j)
    plt.plot([item + shift for item in col_i], col_j, 'o')
    plt.axis([0, 7, 0, 9000])
    # 添加文本 #x轴文本
    plt.xlabel('x坐标轴')
    # y轴文本
    plt.ylabel('y坐标轴')
    # 标题
    plt.title('标题')
    plt.show()

# drawPicture(0,1,0)
# drawPicture(3,4,-0.5)
# drawPicture(6,7,-0.5)
# drawPicture(9,10,-0.5)
# drawPicture(12,13,-0.5)
# drawPicture(15,16,-0.5)


'''
drawPictureTogether(x轴的数据列，y轴的数据列，偏移值，一共几张图)
'''


def drawForcePictureTogether(i, j, shift, num):
    p = {}
    for n in range(num):
        # p["col_i" + str(n)], p["col_j" + str(n)] = getData(i, j)
        p["col_i" + str(n)], p["col_j" + str(n)] = getDatafromCSV(i, j)
        i = i+4
        j = j+4

    l0 = plt.plot([item + shift for item in p["col_i0"]], p["col_j0"], label = 'E1', linewidth=1.0)
    l1 = plt.plot([item + shift for item in p["col_i1"]], p["col_j1"], label = 'E2', linewidth=1.0)
    l2 = plt.plot([item + shift for item in p["col_i2"]], p["col_j2"], label = 'E3', linewidth=1.0)
    l3 = plt.plot([item + shift for item in p["col_i3"]], p["col_j3"], label = 'E4', linewidth=1.0)
    l4 = plt.plot([item + shift for item in p["col_i4"]], p["col_j4"], label = 'E5', linewidth=1.0)
    l5 = plt.plot([item + shift for item in p["col_i5"]], p["col_j5"], label = 'E6', linewidth=1.0)
    plt.axis([0, 8, 0, 8000])
    # 添加文本 #x轴文本
    plt.xlabel('Déplacement (mm)')
    # y轴文本
    plt.ylabel('Force(N)')
    # 标题
    plt.title('Plaque5-Force-Déplacement')
    # 图例
    plt.legend()
    plt.show()




def drawContraintePictureTogether(i, j, shift, num):
    p = {}
    for n in range(num):
        # p["col_i" + str(n)], p["col_j" + str(n)] = getData(i, j)
        p["col_i" + str(n)], p["col_j" + str(n)] = getDatafromCSV(i, j)
        i = i+4
        j = j+4

    l0 = plt.plot([item + shift for item in p["col_i0"]], p["col_j0"], label = 'E1', linewidth=1.0)
    l1 = plt.plot([item + shift for item in p["col_i1"]], p["col_j1"], label = 'E2', linewidth=1.0)
    l2 = plt.plot([item + shift for item in p["col_i2"]], p["col_j2"], label = 'E3', linewidth=1.0)
    l3 = plt.plot([item + shift for item in p["col_i3"]], p["col_j3"], label = 'E4', linewidth=1.0)
    l4 = plt.plot([item + shift for item in p["col_i4"]], p["col_j4"], label = 'E5', linewidth=1.0)
    l5 = plt.plot([item + shift for item in p["col_i5"]], p["col_j5"], label = 'E6', linewidth=1.0)
    # print(len(p["col_i5"]))
    # print(len(p["col_j5"]))
    plt.axis([0, 8, 0, 650])
    # 添加文本 #x轴文本
    plt.xlabel('Déplacement (mm)')
    # y轴文本
    plt.ylabel('Contrainte (MPa)')
    # 标题
    plt.title('Plaque5-Contrainte-Déplacement')
    # 图例
    plt.legend()
    plt.show()

drawForcePictureTogether(0, 1, -0.4, 6)
drawContraintePictureTogether(0,2,-0.4,6)