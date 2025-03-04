from itertools import combinations
import sys

def dfs(graph, node, visited, flags):
    stack = [node]
    count = 0
    
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            count += 1
            for neighbor in graph[current]:
                if not visited[neighbor] and flags[neighbor] == 'G':
                    stack.append(neighbor)
                    
    return count

def generate_configurations(initial_flags):
    red_indices = [i for i, flag in enumerate(initial_flags) if flag == 'R']
    configurations = []
    # Generate all combinations of even counts of red indices
    for r in range(0, len(red_indices) + 1, 2):
        for combo in combinations(red_indices, r):
            config = list(initial_flags)
            for idx in combo:
                config[idx] = 'G'
            configurations.append(''.join(config))
    return configurations

def max_reachable_posts(N, connections, initial_flags):
    # Convert connections to an adjacency list
    graph = [[] for _ in range(N)]
    for u, v in connections:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    results = []
    configurations = generate_configurations(initial_flags)
    
    for start in range(N):
        max_posts = 0
        for flags in configurations:
            if flags[start] == 'R':
                continue
            visited = [False] * N
            count = dfs(graph, start, visited, flags)
            max_posts = max(max_posts, count)
        results.append(max_posts)
    
    return results

def main():
    # Read input from standard input
    data = sys.stdin.read().strip().split()
    
    # Parse the input
    index = 0
    N = int(data[index])
    index += 1
    connections = []
    for _ in range(N - 1):
        u = int(data[index])
        v = int(data[index + 1])
        connections.append((u, v))
        index += 2
    initial_flags = data[index]
    
    # Get the results
    results = max_reachable_posts(N, connections, initial_flags)
    
    # Print the results one by one
    for res in results:
        print(res)

if __name__ == "__main__":
    main()

