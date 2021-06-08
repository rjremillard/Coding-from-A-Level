from collections import defaultdict


def getData(path: str = "ukData.csv") -> defaultdict[dict]:
    """Forms adjacency dictionary from csv provided
    :param path: Fully qualified path to csv file
    :return: adjacency in form {nodeID#: {neighbourID#: weight, ...}, ...}
    """
    with open(path, "r") as f:
        rawData = f.read()

    adjacency = defaultdict(dict)
    for line in rawData.split("\n")[1:-1]:
        temp = line.replace(",", " ")
        temp = temp.replace("\"", "")
        node, *neighbours = temp.split()
        for n in neighbours:
            n = n.split(":")
            adjacency[node][n[0]] = n[1]
    
    return adjacency 


if __name__ == "__main__":
    adj = getData()
    for i in list(adj.keys())[:5]:
        print(i, adj[i])
