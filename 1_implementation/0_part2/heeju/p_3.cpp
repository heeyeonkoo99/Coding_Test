#include<iostream>
#define SIZE_OF_DIRECTION 4
using namespace std;

int n; //세로의 크기 
int m; //가로의 크기

int x; //서쪽으로부터 떨어진 칸
int y; //북쪽으로부터 떨어진 칸

int dir; //0:북,1:동,2:남,3:서

int main() {
	int** map;
	int res = 0;

	//(x,y)
	int move[SIZE_OF_DIRECTION][2] = { {0,-1},{1,0},{0,1},{-1,0} };

	cin >> n >> m;
	cin >> y >> x;


	//map 생성
	map = new int*[n];
	for (int i = 0; i < n; i++)
		map[i] = new int[m];

	//map 구성
	for (size_t i = 0; i <n;i++){
		for (size_t j = 0; j < m;j++){
			cin >> map[i][j];
		}
	}

	int cnt = 0;
	while (1) {
		int tempX = x;
		int tempY = y;
		int tempDir;
		//방향 먼저 바꾸고
		if (dir == 0)
			dir = 3;
		else
			dir--;
		cnt++;
		//움직이는 것이 가능한지 확인하기
		tempDir = cnt == 4 ? (dir + 2) % SIZE_OF_DIRECTION : dir;
		tempX += move[tempDir][0];
		tempY += move[tempDir][1];
		if (map[tempY][tempX] == 0) {
			x = tempX;
			y = tempY;
			map[y][x] = 1;
		}
		else if (cnt == 4)
			break;
	}

	res = cnt;
	cout << res << endl;
	return 0;
}

