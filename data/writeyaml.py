import yaml

data = {'Search_Data': {'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                        'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 在data目录下新建文件abc.yml文件,


with open("./abc.yml", "w", encoding='utf-8')as f:
    yaml.safe_dump(data, f, encoding='utf-8', allow_unicode=True)
