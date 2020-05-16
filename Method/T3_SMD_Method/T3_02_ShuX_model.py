import re
import pymongo
import traceback


class Model:

    def __init__(self, RangeDataList):
        self.RangeDataList = RangeDataList
        print("开始执行属性赋值")
        print(RangeDataList)

    def get_array_value(self,data):
        for i, item in data:
            if item.get("LX") == "ARRAY VC":
                item.update({"RCLX": "ARRAYVC"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_ay_value(self):
        for i, item in self.RangeDataList:
            ZWM = item.get("ZWM")
            if re.search(r'案由', str(ZWM)) or re.search(r'罪名', str(ZWM)):
                item.update({"RCLX": "AY"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_mc_value(self):
        for i, item in self.RangeDataList:
            ZWM = item.get("ZWM")
            CD = item.get("CD")
            if re.search(r'名称$', str(ZWM)) and CD == "600":
                item.update({"RCLX": "VC600"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_single_value(self):
        for i, item in self.RangeDataList:
            DM = item.get("DM")
            if re.search(r'1140', str(DM)):
                item.update({"RCLX": "单值代码"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_time_value(self):
        for i, item in self.RangeDataList:
            LX = item.get("LX")
            if LX == "DT":
                item.update({"RCLX": "时间戳"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_data_value(self):
        for i, item in self.RangeDataList:
            LX = item.get("LX")
            if LX == "RQ":
                item.update({"RCLX": "日期"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_int_value(self):
        for i, item in self.RangeDataList:
            LX = item.get("LX")
            if LX == "NUM":
                item.update({"RCLX": "NUM"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_n_value(self):
        for i, item in self.RangeDataList:
            LX = item.get("LX")
            if LX == "N":
                item.update({"RCLX": "N"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def get_person_value(self):
        for i, item in self.RangeDataList:
            ZWM = item.get("ZWM")
            ZD = item.get("ZD")
            if re.search(r'人', str(ZWM)) and not re.search(r'^bh', str(ZD)):
                item.update({"RCLX": "人员"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)
            elif re.search(r'人', str(ZWM)) and re.search(r'^bh', str(ZD)):
                item.update({"RCLX": "UUID"})
                MongodbClient(item).patch_data()
                self.RangeDataList.remove(item)

    def __str__(self):
        return "赋值完成"


class MongodbClient:
    def __init__(self, item):
        self.DB_name = "LMK_DB",
        self.Collection = "smd_data",
        self.Method = "patch"
        self.item = item

    def patch_data(self):
        mogoclient = pymongo.MongoClient("localhost", port=27017)
        db = mogoclient[self.DB_name]
        collection = db[self.Collection]
        ZD = self.item.get("ZD")
        collection.update({"ZD": str(ZD)}, {"$set": self.item})

    def __str__(self):
        return "%s 赋值完成,赋值为%s" % (self.item.get("ZWM"), self.item.get("RCLX"))



