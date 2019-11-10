from T3C_F_Method import Method
from T3C_W_Write import WriteSMD_Demand
class Compare:
    def SMDQC(self,SMDList):
        ResultSMD = Method.Method().QC(SMDList)
        return  ResultSMD

    def DemandQC(self, DemandList):
        ResultSMD = Method.Method().QC(DemandList)
        return ResultSMD
    def SMD_Demand_ZD_Compare(self,DemandList,SMDlist):
        ResultSMD = Method.Method().QC(SMDlist)
        ResultDemand = Method.Method().QC(DemandList)
        DemandZD_List = [x.get("ZD") for x in ResultDemand if (x.get("ZD") != "")]
        SMDZD_List = [x.get("ZD") for x in ResultSMD if x.get("ZD") != ""]
        SMDLIst = []
        DemandList = []
        CmopareResult = {}
        try:
            for item in DemandZD_List:
                if item not in SMDZD_List:
                    DemandList.append(item)
            for items in SMDZD_List:
                if items not in DemandZD_List:
                    SMDLIst.append(items)
        except Exception as e:
            print("字段情况对比失败,以下是失败信息" + "\n")
            print(e)
        CmopareResult.update({"S_SMD": DemandList, "S_Demand": SMDLIst})
        return CmopareResult
    #获取需求比SMD多的字段的具体位置+字段
    def SMDLess(self,QCDemand,CmopareResult):
        DelList=[]
        CommentList=[]
        SMDLess=CmopareResult.get("S_SMD")
        for i, item in enumerate(QCDemand, 1):
                ZD = item.get("ZD")
                DB= item.get("flags")
                Result=str({DB:ZD})+"\n"
                if ZD in SMDLess:
                    DelList.append(Result)
                else:
                    CommentList.append(item)
        DemandDict={"Del":DelList,"Com":CommentList}
        return DemandDict

    # 获取需求比SMD多的字段的具体位置+字段
    def DemandLess(self, QCSMD, CmopareResult):
        DelList = []
        CommentList = []
        DemandLess = CmopareResult.get("S_Demand")
        for i, item in enumerate(QCSMD, 1):
            ZD = item.get("ZD")
            DB = item.get("DB")
            Result = str({DB: ZD}) + "\n"
            if ZD in DemandLess:
                DelList.append(Result)
            else:
                CommentList.append(item)
        SNDDict = {"Del": DelList, "Com": CommentList}
        return SNDDict

    #写成需要的格式输出文件

    # 比较后将比较完的不同的字段从两个列表中删除
    # def DelDiffData(self,DirName, DemandDict, SMDDict, DiffDict,LocationTime):
    #     fileName="Diff_ZD_Dict"
    #     AfterDelResult=[]
    #     AfterDelDemandResult=[]
    #     AfterDelSMDResult=[]
    #     TitleDemand="这是需求里有,SMD里没有的字段:"+"\n"
    #     TitleSMD="这是SMD里有,需求里没有的字段:"+"\n"
    #     SMDList=[]
    #     DemandList=[]
    #     path="..\\T3C_AR_Result\\"+DirName
    #     try:
    #         DiffDemandDict=dict(DiffDict).get("S_SMD")#需求里有 SMD没有
    #         DiffSMDDict=dict(DiffDict).get("S_Demand")#SMD里有需求里没有
    #         for i,item in enumerate(DemandDict,1):
    #             ZD = item.get("ZD")
    #             DB= item.get("flags")
    #             Result={DB:ZD+"\n"}
    #             if ZD in DiffDemandDict:
    #                 list(DemandDict).remove(item)
    #                 DemandList.append(Result)
    #                 print(DemandList)
    #             else:
    #                 AfterDelDemandResult.append(item)
    #         for j,items in enumerate(SMDDict,1):
    #             ZD = items.get("ZD")
    #             DB=items.get("DB")
    #             Result={DB:ZD+"\n"}
    #             if ZD in DiffSMDDict:
    #                 list(SMDDict).remove(items)
    #                 SMDList.append(Result)
    #                 print(SMDList)
    #             else:
    #                 AfterDelSMDResult.append(items)
    #         WriteSMD_Demand.Write_SMD_Demand().WriteDiffZD(DirName,LocationTime,TitleDemand,fileName,TitleSMD,
    #                                                        DemandList, SMDList )
    #         AfterDelResult.append(AfterDelDemandResult)
    #         AfterDelResult.append(AfterDelSMDResult)
    #     except Exception as e:
    #         print(e)
    #     print("两个文档中存在的字段筛选完成,其他字段已经写入"+path+"...")
    #     return AfterDelResult
    #

