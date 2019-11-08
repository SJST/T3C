'''StartProcess'''
from T3C_B_Demand import Demand_Analysis
if __name__ == '__main__':
    dirnameDA = str(input("请输入需求文件地址:"))
    DA_FlieList=Demand_Analysis.DA().GetDFL(dirnameDA)

    #E:\T3cProjectDoctment\02_中台信息项\信息项\中台\民事\子表\中台_民事_支付令审查案件_送达债务人及异议信息.xlsx
    Data = Demand_Analysis.DA().GetDemandData(DA_FlieList)
    print(Data)
    #filenameSMD=str(input("请输入SMD地址:"))


