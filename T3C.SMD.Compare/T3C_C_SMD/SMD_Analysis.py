import xlrd
class SMD_Analysis:
    def GetSMDDate(self,path,sheet_name):

        bk=xlrd.open_workbook(path)
        sh = bk.sheet_by_name(sheet_name)
        row_num = sh.nrows
        data_list = []
        try:
            for i in range(2, row_num):
                row_data = sh.row_values(i)
                data = {}
                for index, key in enumerate(sh.row_values(1)):
                    data[key] = row_data[index]
                data_list.append(data)
        except Exception as e:
            print("获取SMD数据失败!失败信息如下"+"\n")
            print(e)
        print("SMD获取完成!开始进行下一步,请小主喝杯咖啡继续等待......")
        return data_list
    def SMDGoalData(self,data_list):
        SMDGoalData=[]
        try:
            for i,item in enumerate(data_list,1):
                ZD=item.get("字段中文名")
                LX=item.get("数据类型")
                CD=str(item.get("数据长度")).split(".")[0]
                JD=item.get("数据精度")
                DM=str(item.get("代码类型")).split(".")[0]
                SMing=item.get("说明")
                BWK=item.get("不为空")
                SMDdict={}
                SMDdict.update({"ZD":ZD,"LX":LX,"CD":CD,"JD":JD,"DM":DM,"SMing":SMing,"BWK":BWK})
                SMDGoalData.append(SMDdict)
        except Exception as e:
            print("获取SMD目标数据失败,失败信息如下"+"\n")
            print(e)
        print("SMD目标字段获取完成!开始进行下一步,请小主喝杯咖啡继续等待......")
        return SMDGoalData
    def SMDGoalDataCL(self,SMDGoalData):
        try:
            for i, item in enumerate(SMDGoalData,1):
                if item.get("SMing")=="UUID生成":
                    item.update({"SMing":"UUID"})
        except Exception as  e:
            print("SMD目标字段处理失败.信息如下"+"\n")
            print(e)
        print("SMD目标字段获取完成!开始进行下一步,请小主喝杯咖啡继续等待......")
        return SMDGoalData
    def CompareZD(self,DemandData,SMDData):
        DemandZD_List=[x.get("ZD") for x in DemandData if (x.get("ZD")!="")]
        SMDZD_List=[x.get("ZD") for x in SMDData if x.get("ZD")!=""]
        SMDLIst=[]
        DemandList=[]
        CmopareResult={}
        try:
            for item in DemandZD_List:
                if item not in SMDZD_List:
                    DemandList.append(item)
            for items in SMDZD_List:
                if items not in DemandZD_List:
                    SMDLIst.append(items)
        except Exception as e:
            print("字段情况对比失败,以下是失败信息"+"\n")
            print(e)
        CmopareResult.update({"S_SMD":DemandList,"S_Demand":SMDLIst})
        return CmopareResult



