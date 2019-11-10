'''StartProcess'''
from T3C_F_Method import Method
from T3C_B_Demand import Demand_Analysis
from T3C_C_SMD import SMD_Analysis
from T3C_E_Compare import Demand_SMD
from T3C_W_Write import WriteSMD_Demand
if __name__ == '__main__':
    dirnameDA = str(input("请输入需求文件地址:"))
    filenameSMD = str(input("请输入SMD地址:"))
    DirCreate=Method.Method().CreatDir(filenameSMD)
    DA_FlieList=Demand_Analysis.DA().GetDFL(dirnameDA)
    LocationTime=Method.Method().locationTime()
    #E:\T3cProjectDoctment\02_中台信息项\信息项\中台\民事\子表\中台_民事_支付令审查案件_送达债务人及异议信息.xlsx
    DemandData = Demand_Analysis.DA().GetDemandData(DA_FlieList)
    #
    DemandGoalData=Demand_Analysis.DA().GetGoalFeild(DemandData)
    #[{'ZD': '序号', 'LX': 'RID', 'CD': None, 'KXX': ''},
    NewDemandGoal=Demand_Analysis.DA().CL_Add(DemandGoalData)
    #
    ChangeLXDemandData=Demand_Analysis.DA().LX_CL(NewDemandGoal)
    # {'ZD': '提货申请日期', 'LX': 'D', 'CD': 32, 'KXX': '', 'SMing': 'UUID', 'DM': ''},
    # -------------------------------------------------------------------------------------------------------------

    SMDData=SMD_Analysis.SMD_Analysis().GetSMDDate(filenameSMD,"COL")
    #
    SMDGoalData=SMD_Analysis.SMD_Analysis().SMDGoalData(SMDData)
    #
    SMDDataCL=SMD_Analysis.SMD_Analysis().SMDGoalDataCL(SMDGoalData)
    #
    #----------------------------------------------------------------------------------
    QC_Demand=Demand_SMD.Compare().DemandQC(DemandGoalData)
    QC_SMD=Demand_SMD.Compare().SMDQC(SMDDataCL)
    DiffZD=Demand_SMD.Compare().SMD_Demand_ZD_Compare(ChangeLXDemandData,SMDDataCL)
    SMDLess=Demand_SMD.Compare().SMDLess(QC_Demand,DiffZD)
    DemandLess=Demand_SMD.Compare().DemandLess(QC_SMD,DiffZD)
    HB_Result=Method.Method().ResultHB(SMDLess,DemandLess)
    TitleDemand="这是Demand里面有的,SMD里没有的"+"\n"
    TitleSMD = "这是SMD里面有的,Demand里没有的" + "\n"
    Name="Diff_ZD"
    W=WriteSMD_Demand.Write_SMD_Demand().WriteDiffZD(DirCreate,LocationTime,TitleDemand,Name,TitleSMD,HB_Result)



