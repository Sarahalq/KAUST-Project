ont_name = {}
f1 = open('/home/qabbaasa/Documents/summer_project/hp.obo', 'r')
for line in f1:
    if line.startswith('id:'):
        item = line.strip().split(" ")
        key = item[1]

    else:

        if line.startswith('name:'):
            items = line.strip().split(" ")
            newline = " ".join(items[1:])
            ont_name[key] = newline
        else:
            continue


print(ont_name)