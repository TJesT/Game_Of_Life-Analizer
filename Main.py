print()
size = int(input())
print()
space_d = [ [j for j in input()] for i in range(size) ]
space_n = [ [space_d[i][j] for j in range(size)] for i in range(size) ]
dead_space = [['x' for j in range(size)] for i in range(size)]
all_states = []
now = 0
z = 0

flag = False
while(True):
    space_d = [ [space_n[i][j] for j in range(size)] for i in range(size) ]
    for state in all_states:
        if (space_d == state):
            print("Yes\n%d"%(now))
            flag = True
            break
    if (flag == True):
        break
    if space_d == dead_space:
        print("No\n%d"%(now))
        break
    all_states.append(space_d)
    now += 1
    for x in range(size):
        for y in range(size):
            z = 0
            if x-1 >= 0 and y-1 >= 0 and (space_d[(x-1)%size][(y-1)%size] == '*'):
                z += 1
            if y-1 >= 0 and (space_d[x][(y-1)%size] == '*'):
                z += 1
            if y-1 >= 0 and x+1 < size and (space_d[(x+1)%size][(y-1)%size] == '*'):
                z += 1
            if x+1 < size and (space_d[(x+1)%size][y] == '*'):
                z += 1
            if x+1 < size and y+1 < size and (space_d[(x+1)%size][(y+1)%size] == '*'):
                z += 1
            if y+1 < size and (space_d[x][(y+1)%size] == '*'):
                z += 1
            if x-1 >= 0 and y+1 < size and (space_d[(x-1)%size][(y+1)%size] == '*'):
                z += 1
            if x-1 >= 0 and (space_d[(x-1)%size][y] == '*'):
                z += 1
            if space_d[x][y] == 'x':
                if z == 3:
                    space_n[x][y] = '*'
            else:
                if z < 2 or z > 3:
                    space_n [x][y] = 'x'
    