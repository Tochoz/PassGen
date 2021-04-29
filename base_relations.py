def last_id():
    with open('data', 'r') as file:
        last_id = int(list(file)[-1].split()[0])
        return last_id

def add_pack(pack):
    password, resource = pack
    with open('data', 'a') as file:
        id = last_id() + 1
        file.write('\n{0} {1} {2}'.format(str(id).zfill(6), password, resource))
    print('Saving success. Your pack has id -- ' + str(id).zfill(6))

def get_resouces():
        with open('data', 'r') as file:
            list_res = [i.split()[-1][:-1] for i in file]
        return list_res

def get_pass(id):
    with open('data', 'r') as file:
        return list(file)[id].split()[1]