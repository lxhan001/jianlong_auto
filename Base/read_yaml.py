from ruamel.yaml import YAML


def get_data(file_name, login_data):  # ����yaml���ݺ�������ÿ��������keyȡֵ������
    with open('./Data/'+file_name, 'r') as f:
        yaml = YAML(typ='safe').load(f)
        dict_yaml = yaml[login_data]
        list_data = []
        for i in dict_yaml.values():
            list_data.append(i)
        return list_data
