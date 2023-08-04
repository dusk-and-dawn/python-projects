# wa_analysis
lines = []
names_lst = []
lines_by_user = {}

def wa_analysis(filepath, *name):
    return filereading(filepath), naming(*name)

def filereading(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

def naming(*name):
    for x in name:
        names_lst.append(x)
    return store_lines(names_lst)    

def store_lines(names_lst):
    for i in names_lst:
        lines_by_user[i] = 0
    for i in names_lst: 
        for x in lines:
            if i in x:
                lines_by_user[i].append(x)

print(lines_by_user)
wa_analysis('/home/plotty/Downloads/_chat_cosmic.txt', 'Kathrin', 'David', 'Kochanie', 'Jh'))


