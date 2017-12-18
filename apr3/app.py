import os.path, ast, pickle
try:
    with open("file.txt", "ab") as file, open(os.path.join(os.pardir, "contacts.txt"), "r+") as file2:
        val = str(file2.read())
        new_dict = ast.literal_eval(val)
        for key, item in new_dict.items():
            if key == 'Ivan':
                new_val = str("\n"+ key + ":"+ str(item))
                pickle.dump(new_val, file)
                file.flush()
                #file.write(str(new_val))
except FileNotFoundError as e:
    print(e)

lists = []
with open("file.txt", "rb") as f:
    while 1:
        try:
            lists.append(pickle.load(f))
        except EOFError:
            break
    print(lists)




  #  f_list = pickle.load(f)
  #  for line in f_list:
 #       print(line)
