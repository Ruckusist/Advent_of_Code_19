from itertools import combinations
import copy
# PUZZLE | ????
# p1=[[1,4,4],[0,0,0]]
# p2=[[-4,-1,19],[0,0,0]]
# p3=[[-15,-14,12],[0,0,0]]
# p4=[[-17,1,10],[0,0,0]]

# EXAMPLE 2 | 4686774924
# p1=[[-8,-10,0],[0,0,0]]
# p2=[[5,5,10],[0,0,0]]
# p3=[[2,-7,3],[0,0,0]]
# p4=[[9,-8,-3],[0,0,0]]

# EXAMPLE 1 | 2772 
p1=[[-1,0,2],   [0,0,0]]
p2=[[2,-10,-7], [0,0,0]]
p3=[[4,-8,8],   [0,0,0]]
p4=[[3,5,-1],   [0,0,0]]

pset = [p1,p2,p3,p4]
states = [copy.copy(pset[:].copy())]

def print_state(state):
    for p in state: print(p)

for state in states:
    print_state(state)

def energy(x): return sum([abs(z) for z in x[0]]) * sum([abs(z) for z in x[1]])

max_runs  = 2772
for i in range(max_runs+1):
    try:
        cur_energy = sum([energy(p1),energy(p2),energy(p3),energy(p4)])
        if i == max_runs:
            print(f"CURRENTLY ON STEP {i}")
            print(f"planet Io        : pos: {p1[0]} | vel: {p1[1]} | energy: {energy(p1)}")
            print(f"planet Europa    : pos: {p2[0]} | vel: {p2[1]} | energy: {energy(p2)}")
            print(f"planet Ganymede  : pos: {p3[0]} | vel: {p3[1]} | energy: {energy(p3)}")
            print(f"planet Callisto  : pos: {p4[0]} | vel: {p4[1]} | energy: {energy(p4)}")
            print(f"Total energy in the system after {i} passes: {cur_energy}")
            # print("step 1; first update the velocity of every moon by applying gravity.")
        # states.append(pset[:])
        for pair in combinations(pset, 2):
            for x in range(len(pair[0][0])):
                planet1_p = pair[0][0][x]
                planet2_p = pair[1][0][x]
                if planet1_p == planet2_p: continue
                elif planet1_p > planet2_p:
                    pair[0][1][x] -= 1
                    pair[1][1][x] += 1
                elif planet1_p < planet2_p:
                    pair[0][1][x] += 1
                    pair[1][1][x] -= 1
        #print("step 2; update the position of every moon by applying velocity.")
        for update in range(len(pset)):
            planet = pset[update]
            for change in range(len(planet[0])):
                planet[0][change] += planet[1][change]

        if i == 10:
            break
    except KeyboardInterrupt:
        print(i)
        exit()

print(f"STATES {len(states)}")
for state in states:
    print_state(state)