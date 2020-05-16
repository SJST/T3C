import pymongo
import traceback
class MongoCLient:
    def MongoCLient(self,DBName,CollectionName,Method,ListData,):
        try:
            mogoclient = pymongo.MongoClient("localhost", port=27017)
            db= mogoclient[DBName]
            collection=db[CollectionName]
            if Method=="insert":
                for i ,item in  enumerate(ListData,1):
                    collection.insert(item)
            if Method=="patch":
                for i,item in enumerate(ListData,1):
                    ZD=item.get("ZD")
                    collection.update({"ZD": str(ZD)}, {"$set": item})
            if Method=="select":
                course_detail = collection.find()
                for num, item in enumerate(course_detail, 1):
                    print(item)
            if Method=="delete":
                for i, item in enumerate(ListData, 1):
                    collection.delete_one(item)
        except Exception as e:
            log=traceback.print_exc()
            print(log)
