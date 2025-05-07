def printnxn(nxn):
    for i in nxn:
        print(*i)

def max_node(*args):
    Max = [-100000, 0, 0]
    for item in args:
        if Max[0] < item[0]:
            Max = item
    
    return Max