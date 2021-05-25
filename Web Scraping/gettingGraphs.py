from requests import get
from collections import defaultdict

def getData(url: str, percent=100) -> dict:
    """Gets data at url
    :param url: url to get, hopefully `https://www.cs.utah.edu/~lifeifei/research/tpq/cal.cedge`, or similar
    :param percent: Optional - how much of the data should be considered
    :return adjacency: in form {node#: {neighbour#: weight, ...}, ...}, note that the graph is weighted
    """
    resp = get(url)

    if resp.status_code == 200:
        data = [
            line.split() for line in resp.text.split("\n")
        ][:-1]

        adjacency = defaultdict(lambda: defaultdict(int))
        for vertex in data[:int(len(data) * (percent/100))]:  # Avoid last (empty)
            # Vertex: [vertex#, start#, end#, weight]
            adjacency[vertex[1]][vertex[2]] = vertex[3]

        return adjacency 

    else:
        raise Exception("Non-200 Status Code")

if __name__ == "__main__":
    url = "https://www.cs.utah.edu/~lifeifei/research/tpq/cal.cedge"
    print(getData(url))
