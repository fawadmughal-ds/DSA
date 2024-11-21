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


