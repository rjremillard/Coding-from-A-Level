import collections
import xml.etree.ElementTree as ET
from collections import defaultdict

# https://osdatahub.os.uk/downloads/open/OpenRoads?_ga=2.92733149.1918177763.1623146350-1602117164.1623146350
# SE is box covering York
tree = ET.parse("Web Scraping/data/OSOpenRoads_SE.gml")
root = tree.getroot()

adjacency = defaultdict(defaultdict)

for child in root:
    if child:
        node = child[0]
        # Only want RoadLinks (for now...)
        if "RoadLink" in node.tag:
            end = node[4].attrib["{http://www.w3.org/1999/xlink}href"]
            start = node[5].attrib["{http://www.w3.org/1999/xlink}href"]
            coords = list(map(float, node[2][0][0].text.split()))
            weight = (
                (coords[0] - coords[-2]) ** 2 +
                (coords[1] - coords[-1]) ** 2
                ) ** .5

            adjacency[end][start] = weight
            adjacency[start][end] = weight

with open("Web Scraping/ukData.csv", "w") as f:
    f.write("nodeID,neighbours\n")
    for i in list(adjacency.keys())[:5]:
        neighbours = ""
        for j in adjacency[i].keys():
            neighbours += f"{j}:{adjacency[i][j]} "
        f.write(f"{i},\"{neighbours[:-2]}\"\n")
