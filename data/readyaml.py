import yaml

with open("./data2.yml", "r", encoding='utf-8')as f:
    # 使用yaml加载数据
    data = yaml.safe_load(f)
    print("返回的字典数据:", data)
    # print("返回的数据类型:", type(data.get("name_str1")))
    # print("返回的数据类型:", type(data.get("name_data")))
