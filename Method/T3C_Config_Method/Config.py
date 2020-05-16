class ConfigMethod:
    pass


def smd_config(key):
    data = {
        "smd_file_path": "D:\\SJT\\TestingAuto\\docs\\20_工程过程\\30_设计相关\\30_概要设计\\各服务概要设计",
        "need_field_list": [{"表名": "table"}, {"字段": "ZD"}, {"字段中文名": "ZWM"}, {"数据长度": "CD"},
            {"数据类型": "LX"}, {"代码类型": "DMLX"}, {"说明":"SM"}]
    }
    result = data.get(key)
    return result

