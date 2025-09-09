pairs = ['name:max', 'age:10']

my_dict = {i.split(':')[0]: i.split(':')[1]for i in pairs}

print('my dict -> ', my_dict)