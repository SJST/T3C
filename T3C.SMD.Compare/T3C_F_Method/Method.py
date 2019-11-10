import os
import time
class Method:
    def locationTime(self):
        LocateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        RQ = str(LocateTime).split()[0]
        SJ = str(LocateTime).split()[1]
        a = "".join([x for x in (RQ.split("-"))])
        b = "".join([x for x in (SJ.split(":"))])
        dictionaryMC = a + b
        return dictionaryMC
    #根据客户输入创建结果文件夹放在AR_Result下
    def CreatDir(self,Name):
        a=str(Name).split("\\")[-1]
        b=str(a).split(".")[0]
        c=str(a).split(".")[1]
        DirName=b+c
        path="..\\T3C_AR_Result\\"+DirName
        if not os.path.exists(path):
            os.mkdir(path)
        return DirName
    def LXChange(self,LX):
        LX_Dict={
            "CID":"VC",
            "RID":"VC",
            "N":"INT",
            "M":"N",
            "F":"INT",
            "D":"D",
            "DT":"DT",
            "Cn":"VC",
            "Cdx":"ARRAY VC",
            "Cgl":"ARRAY VC",
            "Cpc":"VC",
            "ID":"VC"

        }
        ChangeLX=dict(LX_Dict)[LX]
        return ChangeLX
#list 去重
    def QC(self,List):
        Result=[]
        ZDlist=[]
        for i,item in enumerate(List,1):
            ZD=item.get("ZD")
            if ZD not in ZDlist:
                Result.append(item)
                ZDlist.append(ZD)
        return Result
    #将两次结果合并
    def ResultHB(self,Demand,SMD):
        Result_SMD=dict(SMD).get("Del")
        Result_Demand=dict(Demand).get("Del")
        Result={"S_SMD":Result_Demand,"S_Demand":Result_SMD}
        return Result
    #根据传过来的ZD和其他属性判断是否相同
    # def PDQT(self,ZD:
    # def CompareZD(self,DemandData,SMDData):
    #     ResultSMD=Method.Method().QC(SMDData)
    #     ResultDemand=Method.Method().QC(DemandData)
    #     DemandZD_List=[x.get("ZD") for x in ResultDemand if (x.get("ZD")!="")]
    #     SMDZD_List=[x.get("ZD") for x in ResultSMD if x.get("ZD")!=""]
    #     SMDLIst=[]
    #     DemandList=[]
    #     CmopareResult={}
    #     try:
    #         for item in DemandZD_List:
    #             if item not in SMDZD_List:
    #                 DemandList.append(item)
    #         for items in SMDZD_List:
    #             if items not in DemandZD_List:
    #                 SMDLIst.append(items)
    #     except Exception as e:
    #         print("字段情况对比失败,以下是失败信息"+"\n")
    #         print(e)
    #     CmopareResult.update({"S_SMD":DemandList,"S_Demand":SMDLIst})
    #     return CmopareResult