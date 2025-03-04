# Max Reachable Posts

Hi there! I'm EthicKnight, and this is my implementation of a solution to a challenging graph traversal problem. The goal of this script is to determine the maximum number of posts that can be reached starting from any given post, given certain constraints.

## Problem Description

Given a set of posts connected by edges and each post being either initially "Red" (R) or "Green" (G), the task is to determine the maximum number of "Green" posts that can be reached starting from any post. The catch is that you can change the state of "Red" posts to "Green", but only in even numbers (0, 2, 4, etc.).

## Implementation Details

This solution involves several key components:

1. **Depth-First Search (DFS)**: To traverse the graph and count reachable posts.
2. **Configurations Generation**: To generate all possible configurations of posts where an even number of "Red" posts are turned "Green".
3. **Graph Representation**: Using adjacency lists to represent the connections between posts.
4. **Results Calculation**: To determine the maximum reachable posts for each starting post.

## Usage

To run this script, you need to provide the input via standard input (stdin). The input should be in the following format:

1. An integer `N` representing the number of posts.
2. `N-1` lines, each containing two integers representing a connection between two posts.
3. A string of length `N` consisting of characters 'R' and 'G' representing the initial state of each post.

### Example

Here's an example input:

```
5
1 2
2 3
3 4
4 5
RGRGG
```

You can run the script from the command line and provide the input like this:

```sh
python max_reachable_posts.py < input.txt
```

where `input.txt` contains the input data.

## Code

Here's the complete implementation:

```python name=max_reachable_posts.py
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
```

Feel free to reach out if you have any questions or suggestions!