# convert A-Z to 0-25
def con(char):
    return ord(char)-ord('A')

# create a 26*101 table to record a station's next stations
table = [ [ [] for _ in range(101) ] for _ in range(26) ]

# record a station's next stations
N = int(input())
for _ in range(N):
    p,q = input().split(' ')
    table[con(p[0])][int(p[1:])] += [q]
    table[con(q[0])][int(q[1:])] += [p]

# travel along every route, recursively
def route( here, there, passby, transfer, table):
    print(here,'------>',there)
    if here == there:
        money.append( 10 + 5*int(passby/3) + 5*transfer )
        print('-- ARRIVED --')
        return

    # make a copy of options, with list slice
    options = table[con(here[0])][int(here[1:])][:]
    if not options:
        print('NO OPTIONS, return!')
        return

    for option in options:
        print('  (',options.index(option)+1,')',option,'in',options)
        table[con(here[0])][int(here[1:])].remove(option)   # remove
        table[con(option[0])][int(option[1:])].remove(here) # 2-way
        if here[0]==option[0]:
            route( option, stop, passby+1, transfer, table )
            print('Returned from',option,'to',here)
            table[con(here[0])][int(here[1:])].append(option)   # restore
            table[con(option[0])][int(option[1:])].append(here) # 2-way
        else:
            route( option, stop, passby+1, transfer+1, table )
            print('Returned from',option,'to',here)
            table[con(here[0])][int(here[1:])].append(option)   # restore
            table[con(option[0])][int(option[1:])].append(here) # 2-way
    print(here, 'runs out of options, return!')

money = []
start,stop = input().split(' ')
route( start, stop, 0, 0, table )
print(min(money))