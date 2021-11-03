# Search Algorithms

## 그래프 저장

- 인접 행렬: 2차원 배열로 그래프의 연결 관계 표현
    - 노드 개수가 많을수록 메모리 낭비
    - 특정 두 노드의 연결 정보 획득 속도 빠름

- 인접 리스트: 리스트로 그래프의 연결 관계 표현
    - 연결된 정보만 저장하여 메모리 효율적 
    - 연결된 데이터를 하나씩 확인해야하므로 연결 정보 획득 속도가 느림

연결이 안되어있으면 무한의 비용(999999999)이라고 정의

## DFS

- Depth First Search
- 스택 자료구조 사용
- 동작 과정
    - 탐색 시작 노드를 스택에 삽입하여 방문 처리
    - 스택 최상단 노드에 `방문하지 않은 인접 노드 있으면` -> 인접 노드 스택에 넣고 방문 처리, `방문하지 않은 인접 노드 없으면` -> 스택에서 최상단 노드 꺼냄
    - 더이상 수행할 수 없으면 종료


```python
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=" ")
    for i in graph[v]:
        if  not visited[i]:
            dfs(graph, i, visited)

# graph: i번째와 연결된 노드를 graph[i]에 리스트로 저장하는 이차원 리스트
graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]

visited = [False]*(len(graph)+1)

dfs(graph, 1, visited)

```

## BFS

- Breadth First Search
- 큐 자료구조 사용
- 동작 과정
    - 탐색 시작 노드를 큐에 삽입하여 방문처리
    - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드들 모두 큐에 삽입 후 방문 처리
    - 더이상 수행할 수 없으면 종료

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]

visited = [False]*(len(graph)+1)

bfs(graph, 1, visited)


```

# Stack

First In Last Out
```python
stack = []

# 요소 추가
stack.append()

# 요소 삭제
stack.pop()
```

# Queue
First In First Out
```python
from collections import deque

queue = deque()

# 요소 추가
queue.append()

# 요소 삭제
queue.popleft()

# 리스트로 변경 가능
l = list(queue)
```