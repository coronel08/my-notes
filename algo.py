# ------------------------------------------------- Chapter 6 Breadth-first-search
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person, "is a mango seller")
                return True
            else: 
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")



# --------------------------------------------------------------- Chap 7 Dijkstra's algorithm
# Create a dict with nested dict values. 
graph2 = {}
graph2["start"] = {}
graph2["start"]["a"] = 6
graph2["start"]["b"] = 2
print(graph2["start"].keys())
# Continue building out nodes.
graph2["a"] = {}
graph2["a"]["fin"] = 1
graph2["b"] = {}
graph2["b"]["a"] = 3 
graph2["b"]["fin"] = 5
graph2["fin"] = {}

# code for the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# code for the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = [] # array to keep track of nodes

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Algo for search
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph2[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    print(node, cost, neighbors)
    node = find_lowest_cost_node(costs)

