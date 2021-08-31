#include<iostream>
#include<cstring>
#define STR_DIS (1)
using namespace std;

int N; //세로
int M; //가로
int res;
int** map;

void bfs(int i, int j,int dis) {
	if (i < 0 || i >= N || j < 0 || j >= M)
		return;
	if (map[i][j] == 1) { //방문하지 않은 미로
		if (i + j != 0)
			dis++;
		map[i][j] = dis;
		bfs(i + 1, j,dis);
		bfs(i, j + 1,dis);
	}
}

int main() {
	cin >> N >> M;
	string* strMap = new string[N];
	for (int i = 0; i < N; i++) {
		cin >> strMap[i];
	}

	map = new int* [N];
	for (int i = 0; i < N; i++) {
		map[i] = new int[M];
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

	bfs(0, 0,STR_DIS);
	cout << map[N-1][M-1] << endl;



}