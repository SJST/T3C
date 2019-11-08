'''Demand Analysis Model'''
import xlrd
import os
import re
class DA:
    #指定用户输入需求所在路径,通过路径找到输入的文件(打开文件)，获取所有的数据
    #第一步 根据需求文档模式，需要先将文件夹下所有的文件
    def GetDFL(self,dirnameDA):
        DA_FlieList=[]
        try:
            for root, dirs, files in os.walk(dirnameDA, topdown=False):
                for name in files:
                    Files=root+"\\"+name
                    DA_FlieList.append(Files)
                    #print(os.path.join(files, name))
        except Exception as e:
            print("获取文件列表失败,以下是失败信息" + "\n")
            print(e)
            exit()
        print("获取文件列表成功!开始进行下一步,请小主喝杯咖啡继续等待...")
        return DA_FlieList
    #第二步遍历文件列表,将打开所有文件,遍历文件下所有的sheet获取所有数据,如果数据已经存在则过滤
    def GetDemandData(self,DemandFileNameList):
        data_list = []
        global path
        global i
        for i,path in enumerate(DemandFileNameList,1):

            try:
                bk = xlrd.open_workbook(path)
                # 根据需求文档需要过滤掉"代码（业务类型）","索引页"
                for name in bk.sheet_names():
                    if name!=('代码（业务类型）') and(name!= '索引页') :
                        sheet=bk.sheet_by_name(name)
                        row_num = sheet.nrows
                        for a in range(1, row_num):
                            row_data = sheet.row_values(a)


                            data = {}
                            for index, key in enumerate(sheet.row_values(0),0):
                                data[key] = row_data[index]


                            if data not in data_list: #过滤相同字段
                                data_list.append(data)


                    break
            except Exception as e:
                print("获取"+path+"失败"+",以下是失败信息" + "\n")
                print(e)
                exit()

        print("xxx!开始进行下一步,请小主喝杯咖啡继续等待...")
        return data_list

