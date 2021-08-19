#include<iostream>
#define SIZE_OF_DIRECTION 4
using namespace std;

int n; //������ ũ�� 
int m; //������ ũ��

int x; //�������κ��� ������ ĭ
int y; //�������κ��� ������ ĭ

int dir; //0:��,1:��,2:��,3:��

int main() {
	int** map;
	int res = 0;

	//(x,y)
	int move[SIZE_OF_DIRECTION][2] = { {0,-1},{1,0},{0,1},{-1,0} };

	cin >> n >> m;
	cin >> y >> x;


	//map ����
	map = new int*[n];
	for (int i = 0; i < n; i++)
		map[i] = new int[m];

	//map ����
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
		//���� ���� �ٲٰ�
		if (dir == 0)
			dir = 3;
		else
			dir--;
		cnt++;
		//�����̴� ���� �������� Ȯ���ϱ�
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

