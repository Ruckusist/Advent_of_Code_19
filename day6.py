
dataset = []
dataset2 = [
    "A)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
]

with open('d6.txt', 'r') as f:
    for line in f.readlines(): dataset.append(line.strip('\n'))

list_of_planets = []
for i in dataset2:
    x, y = i.split(")")
    list_of_planets.append(x)
    list_of_planets.append(y)
list_of_planets = set(list_of_planets)

# print(list_of_planets)
# exit()

graph = {}
for connection in dataset2:
    p1, p2 = connection.split(')')

    base_planet = graph.get(p1, None)

    if not base_planet:
        graph[p1] = []
    
    graph[p1].append(p2)

    # print(f'{p1} --> {p2}')
    #  break

new_set = {}
for planet in sorted(list_of_planets):
    new_set[planet] = 0
    print(f"| working on this planet: {planet}")
    counter = new_set[planet]
    def check_graph(p):
        global counter
        global graph
        for k, v in graph.items():
            if p == v:  continue
            print(f"is {p} in {v} ?? {p==v}")
            for x in v:
                if p in x:
                    counter += 1
                    check_graph(x)

    check_graph(planet)
    print(f"Planet: {planet} Orbits {counter} things")
    # break

# print(graph)