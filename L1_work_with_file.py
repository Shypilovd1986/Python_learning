'''
work with file
work with module pickle
'''
import pickle
shop_list_file = 'C:\\MPP\\shop_list.data'
shop_list = ['apple', 'raspbarry', 'strawbarry']
f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()

f_read = open(shop_list_file,'rb')
f_load = pickle.load(f_read)
f_read.close()
print(f_load)
# f_open = open(r'C:\MPP\test.txt', 'w')
# text = 'Some summer day \nI and my daughter \ngo to the stadium'
# f_open.write(text)
# f_open.close()
# f_read = open(r'C:\MPP\test.txt')
# while True:
#         line = f_read.readline()
#         if len(line) <= 0:
#             break
#         print(line, end = '')


