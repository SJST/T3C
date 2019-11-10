# a=3
# if (a!=1) and (a!=2):
#     print(a)
from T3C_W_Write import  WriteSMD_Demand
from T3C_F_Method import Method
DirName="T3民事案件"
DemandDict=[{"ZD":"2","3":"4","flags":"Test"},{"ZD":"6","3":"4","flags":"Test"}]
SMDDict=[{"ZD":"2","5":"6","DB":"DB"},{"ZD":"8","3":"4","DB":"DB"}]
DiffDict=["6","8"]
LocationTime=Method.Method().locationTime()
def DelDiffData( DirName, DemandDict, SMDDict, DiffDict, LocationTime):
    fileName = "Diff_ZD_Dict"
    AfterDelResult = []
    AfterDelDemandResult = []
    AfterDelSMDResult = []
    TitleDemand = "这是需求里有,SMD里没有的字段:" + "\n"
    TitleSMD = "这是SMD里有,需求里没有的字段:" + "\n"
    SMDList = {}
    DemandList = {}
    path = "E:\GitHub\T3\T3C\T3C.SMD.Compare\T3C_AR_Result\T3民事案件" + DirName
    try:
        DiffDemandDict = DiffDict[0]  # 需求里有 SMD没有
        DiffSMDDict = DiffDict[1]  # SMD里有需求里没有
        for i, item in enumerate(DemandDict, 1):
            ZD = item.get("ZD")
            DB = item.get("flags")
            Result = {DB: ZD + "\n"}
            if ZD in DiffDemandDict:
                list(DemandDict).remove(item)
                DemandList.update(Result)
            else:
                AfterDelDemandResult.append(item)
        for j, items in enumerate(SMDDict, 1):
            ZD = items.get("ZD")
            DB = items.get("DB")
            Result = {DB: ZD + "\n"}
            if ZD in DiffSMDDict:
                list(SMDDict).remove(items)
                SMDList.update(Result)
            else:
                AfterDelSMDResult.append(items)
        WriteSMD_Demand.Write_SMD_Demand().WriteDiffZD(DirName, LocationTime, TitleDemand, fileName, TitleSMD,
                                                       DemandList, SMDList)
        AfterDelResult.append(AfterDelDemandResult)
        AfterDelResult.append(AfterDelSMDResult)
    except Exception as e:
        print(e)
    print("两个文档中存在的字段筛选完成,其他字段已经写入" + path + "...")
    return AfterDelResult
if __name__ == '__main__':
    a=DelDiffData( DirName, DemandDict, SMDDict, DiffDict, LocationTime)
    print(a)
