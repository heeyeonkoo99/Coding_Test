//음료수 얼려 먹기
#include<iostream>
#include<cstring>
using namespace std;

int N;
int M; //가로 == 행의 개수
int result;
int** visited;
int** map;

bool dfs(int i, int j) {
	if (i < 0 || i >= N || j < 0 || j >= M)
		return false;
	if (map[i][j] == 0) {
		map[i][j] = 1;
		dfs(i - 1, j);
		dfs(i, j-1);
		dfs(i+1, j);
		dfs(i, j+1);
		return true;
	}
	return false;
}

int main() {
	cin >> N >> M;
	string* strMap = new string[N];

	map = new int*[N];
	visited = new int* [N];
	for (int i = 0; i < N; i++) {
		map[i] = new int[M];
		visited[i] = new int[M];
	}

	for (int i = 0; i < N; i++) {
		cin >> strMap[i];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int data;
			if (strMap[i][j] == '0')
				data = 0;
			else
				data = 1;
			map[i][j] = data;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (dfs(i, j) == true)
				result++;
		}
	}

	cout << result << endl;

	return 0;
}


