def nearest_neighbor(graf, list_except):
    min_value = 9999
    min_key = None
    for key, value in graf.items():
        if value < min_value and  key  not in list_except :
            min_value = value
            min_key = key
    return min_key, min_value

def nearest_neighbor1(list_check:list, grafs:list):
    min_value = 9999
    min_key = None
    min_lc = None
    for lc in list_check:
        for key, value in graf[lc].items():
            if value < min_value and  key  not in list_check:
                min_value = value
                min_key = key
                min_lc= lc
    return min_key, min_value, min_lc


graf = {'A':{'B': 3, 'F': 2},
        'B': {'A': 3, 'C': 3, 'G': 6},
        'C': {'B': 3, 'G': 1, 'E': 2, 'D': 3},
        'D': {'C': 3, 'E': 5},
        'E': {'D': 5, 'C': 2, 'G': 3, 'F': 4},
        'F': {'A': 2, 'E': 4, 'G': 3},
        'G': {'B': 6, 'C': 1, 'E': 3, 'F': 3}}

start = 'A'
list_except = []
for key, value in graf.items():
    neighbor =  nearest_neighbor(value, list_except)
    list_except.append(neighbor[0])
    # print(key, neighbor, list_except)

list_added = ['A']
n = 1
while n<len(graf):
    min_neighbor = nearest_neighbor1(list_added, graf)
    list_added.append(min_neighbor[0])
    print(min_neighbor, list_added)
    n+=1
