l = []
a = 1

def add_star():
    u = int(input("\n\n\n\tEnter number of star: "))
    while True:
        l.append('*')
        if len(l) == u:
            print(l)
            break
        else:
            print(l)
    return remove_star()

def remove_star():
    while True:
        l.pop()
        if len(l) == 1:
            print(l)
            break
        else:
            print(l)
    
    return add_star()


add_star()