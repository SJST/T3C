from T3_Z_Method import T3_01_FileMethod
from T3_02_ReadConfig import T3_01_ReadConfig
from T3_03_SwaggerData import T3_01_SwaggerData
from T3_04_SingleCode import T3_01_SingleCode
from T3_05_CsvHandle import T3_01_CsvHandle
from T3_06_WriteResult import T3_01_WriteResult
from T3_Z_Method import Method
from T3_07_SmdData import T3_01_init_smddata

if __name__ == '__main__':
    config_path = T3_01_ReadConfig.spilt_config_path("Z-Config", "Config.txt")
    dict_config_content = T3_01_ReadConfig.get_config_content(config_path)
    swagger_address = dict_config_content["Swagger"]
    ApiDescription = dict_config_content["ApiDescription"]
    # 从这往下是swagger数据处理方法
    post_address = T3_01_SwaggerData.get_post_address(swagger_address)
    swagger_data = T3_01_SwaggerData.get_swagger_data(post_address)
    definitions_data = T3_01_SwaggerData.get_definitions_data(swagger_data, "definitions")
    path_data = T3_01_SwaggerData.get_definitions_data(swagger_data, "paths")
    path_value_list = T3_01_SwaggerData.get_path_value(path_data)
    description_dto = dict_config_content["BodyKey"]
    #   T3_01_SwaggerData.get_config_api_value(path_value_list,ApiDescription)
    config_api_data = T3_01_SwaggerData.get_config_definitions_data(definitions_data, description_dto)
    value_code_field = T3_01_SwaggerData.get_code_field(config_api_data)
    #   SMD数据的处理方法
    smd_config_path = T3_01_ReadConfig.spilt_config_path("Z-Config", "ChangeSmdToJson.txt")
    smd_dict_config_content = T3_01_ReadConfig.get_config_content(smd_config_path)
    smd_address = smd_dict_config_content["address"]
    result = Method.get_one_smd_data(smd_address, "COL", 0, 1)
    smd_list = T3_01_init_smddata.get_need_data_list(result)
    DB_table = dict_config_content["DBtable"]
    Compare_smd = T3_01_init_smddata.get_compare_data(smd_list, DB_table)
    print(Compare_smd)
    print(value_code_field)
    Write_Compare = T3_01_init_smddata.Compare_data(Compare_smd,value_code_field)
    print(Write_Compare)



