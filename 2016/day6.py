import os

def rekt(lst):
    return min(set(lst), key=lst.count)

def get_input():
    FILE = []
    with open(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            "day6input.txt"
        )
    ) as f:
        for i in f.readlines():
            FILE.append(i.strip('\n'))
    return FILE

puzzle = get_input()
answer = []
for i in range(len(puzzle[0])):
    subset = []
    for x in range(len(puzzle)):
        subset.append(puzzle[x][i])
    answer.append(rekt(subset))
print(answer)
