# wa_analysis
lines = []
names_lst = []
lines_by_user = {}

def filereading(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    return lines
# def naming(*name):
#     for x in name:
#         names_lst.append(x)

# def store_lines(names_lst):
#     for i in names_lst:
#         lines_by_user[i] = 0
#     for i in names_lst: 
#         for x in lines:
#             if i in x:
#                 lines_by_user[i].append(x)

print(filereading('/home/curiosity/python projects/_chat_cosmic.txt'))
# def wa_analysis(filepath, *name):

