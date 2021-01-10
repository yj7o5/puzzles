#!/usr/bin/env python3

"""
Notes:
For part A uses Floyd-Warshall to update all vertices distances to shortest distance and then appliesa DFS for first node
For part B for each vertex performs a DFS to pick the one with the longest path
"""

import sys
import re

INF = float('inf')

def update_path(graph):
    total = len(graph)
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if graph[i][k] == INF or graph[k][j] == INF:
                    continue

                if graph[i][j] != 0 and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

def find_distance(cities, compare, curr_city_index):
    visited_cities = []
    total_cities = len(cities)

    total_distance = 0
    while len(visited_cities) < (total_cities - 1):
        destinations = cities[curr_city_index]
        visited_cities.append(curr_city_index)

        next_city_idx = 0
        next_city = INF if compare(0, 1) else -INF

        for i in range(len(destinations)):
            if i in visited_cities:
                continue

            dest = destinations[i]
            if dest > 0 and compare(dest, next_city):
                next_city = dest
                next_city_idx = i

        total_distance += next_city
        curr_city_index = next_city_idx

    return total_distance

def construct_graph(lines):
    p = r"(\w+) to (\w+) = (\d+)"
    edges = []
    vertices = []
    for line in lines:
        src, dst, dist = re.match(p, line).groups()
        edges.append((src, dst, int(dist)))

        if src not in vertices:
            vertices.append(src)
        if dst not in vertices:
            vertices.append(dst)

    graph = [[INF if i!=j else 0 for j in range(len(vertices))] for i in range(len(vertices))]

    for (src, dst, dist) in edges:
        i, j = vertices.index(src), vertices.index(dst)
        graph[i][j] = dist
        graph[j][i] = dist

    return graph

def find_shortest_path_distance(data):
    graph = construct_graph(data)

    update_path(graph)

    return find_distance(graph, lambda x,y: x < y, 0)

def find_longest_path_distance(data):
    graph = construct_graph(data)

    max_dist = -INF
    # dfs on each node
    for i in range(len(graph)):
        max_dist = max(max_dist, find_distance(graph, lambda x,y: x > y, i))

    return max_dist

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

with open(filename) as file:
    text = file.read().strip()
    data = text.split("\n")

    print("Part A: ", find_shortest_path_distance(data))
    print("Part B: ", find_longest_path_distance(data))
