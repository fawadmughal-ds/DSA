from collections import deque

def bfs(graph, start):
    visited = set() 
    queue = deque([start]) 
    traversal_order = [] 
    
    while queue:
        node = queue.popleft() 
        
        if node not in visited:
            visited.add(node)  
            traversal_order.append(node) 
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    result = bfs(graph, start_node)
    print("BFS traversal starting from node", start_node, ":", result)
