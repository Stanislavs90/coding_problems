start = 0

edges = [
    [[1,7]],
    [[2,6],[3,20],[4,3]],
    [[3,14]],
    [[4,2]],
    [],
    [],
]

#0(v^2) time  | o(v) space
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    # list
    minDistance = [float('inf') for _ in range(numberOfVertices)]
    minDistance[start] = 0

    visited = set()
    

    while len(visited) != numberOfVertices:
        # grab the vertex with the min value and not visted
        vertex, currentMinDistance = getVertexWithMinDistance(minDistance, visited)
        # if in inf stop
        if currentMinDistance == float('inf'):
            break
        # add to visted list
        visited.add(vertex)
        # loop through all edges
        for edges in edges[vertex]:
            destination, distanceToDestination = edges

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistance[destination]
            if newPathDistance < currentDestinationDistance:
                minDistance[destination] = newPathDistance

        return list(map(lambda x: -1 if x == float('inf') else x, minDistance))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance

    return vertex, currentMinDistance


print(dijkstrasAlgorithm(start,edges))