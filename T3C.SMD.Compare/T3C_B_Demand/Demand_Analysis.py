'''Demand Analysis Model'''
import xlrd
import os
import re
from  T3C_F_Method import Method
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
        global flagsDict
        for i,path in enumerate(DemandFileNameList,1):
            fliename=str(path).split("\\")[-1]

            # try:
            bk = xlrd.open_workbook(path)
            # 根据需求文档需要过滤掉"代码（业务类型）","索引页"
            for name in bk.sheet_names():
                try:
                    if name =="信息项":
                        flagsDict={"flags":fliename}
                    else:
                        flagsDict={"flags":name}
                    if name!=('代码（业务类型）') and(name!= '索引页') :
                        sheet=bk.sheet_by_name(name)
                        row_num = sheet.nrows
                        for a in range(1, row_num):
                            row_data = sheet.row_values(a)
                            data = {}
                            for index, key in enumerate(sheet.row_values(0),0):
                                data[key] = row_data[index]

                            #
                            ZDZT=data.get("修改类别")
                            XGSJ=data.get("修改时间")
                            ZD=data.get("数据库字段中文名")
                            if data not in data_list and    ((ZDZT!="删")and( not re.search("删",str(XGSJ)))and(
                                ZD!=""
                            )) : #过滤相同字段，删除修改类别是删除的字段
                                data.update(flagsDict)
                                data_list.append(data)
                except Exception as e:
                    print("获取"+path+"失败"+",以下是失败信息" + "\n")
                    print(e)
                    exit()

        print("获取需求数据成功!开始进行下一步,请小主喝杯咖啡继续等待...")
        print(data_list)
        return data_list
   # 循环数据list 获取想要的数据
    def GetGoalFeild(self,data_list):
        GoalList=[]
        global ZD
        for i ,item in enumerate(data_list,1):
            ZD = item.get("数据库字段中文名")
            if ZD=="":
                ZD=item.get("建议显示名")
            try:
                GoalDict={}
                LX=item.get("类型")
                CD=item.get("长度")
                KXX=item.get("可选项")
                JD=item.get("")
                flags=item.get("flags")
                GoalDict.update({"ZD":ZD,"LX":LX,"CD":CD,"KXX":KXX,"JD":JD,"flags":flags})
                GoalList.append(GoalDict)
            except Exception as  e:
                print("获取"+ZD+"数据失败,以下是失败信息"+"\n")
                print(e)
                exit()
        print("获取需求目标数据成功!开始进行下一步,请小主喝杯咖啡继续等待...")
        return GoalList
    #将获取到的目标字段进行处理
    # 添加些必要字段
    def CL_Add(self,GoalList):
        try:
            for i,item in enumerate(GoalList,1):
                KXX=item.get("KXX")
                LX=item.get("LX")
                if LX=="RID"or"ID":
                    item.update({"SMing":"UUID","CD":"32","DM":""})
                elif LX=="N" and (re.search(r'\\n\d',KXX)):
                    item.update({"SMing":"","CD":"100","DM":""})
                elif LX=="BO":
                    item.update({"SMing":"","CD":"100","DM":"11400009"})
                else:
                    item.update({"SMing":"","CD":"","DM":""})
        except Exception as e:
            print("字段添加失败,下面是失败信息!")
            print(e)
        print("字段添加成功！开始进行下一步,请小主喝杯咖啡继续等待...")
        return GoalList
#LX 字段需要处理,方案是建立一个dict dict的key是原LX value 是SMD的LX 通过传过来的LX进行转换
    def LX_CL(self,GoalList):
        try:
            for i ,item in enumerate(GoalList,1):
                LX=item.get("LX")
                ChangeLX=Method.Method().LXChange(LX)
                item.update({"LX":ChangeLX})
        except Exception as e:
            print("类型转换失败，失败信息如下"+"\n")
            print(e)
        print("类型转换成功!开始进行下一步,请小主喝杯咖啡继续等待...")
        return GoalList








