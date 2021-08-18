//왕실의 나이트
#include<iostream>
#include<algorithm>
using namespace std;

char row; //열
int col; //행
int main() {
	int move[8][2] = { {1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1} }; //나이트가 움직일 때 갈 수 있는 경로의 경우의 수
	size_t sizeOfMove = sizeof(move) / sizeof(move[0]);
	cin >> row;
	cin >> col;
	int res = 0;

	//cout << row << endl << col << endl;
	for (size_t i = 0; i < sizeOfMove; i++) {
		char testRow=row+move[i][0];
		int testCol= col+move[i][1];
		if (testRow >= 'a' && testRow <= 'h') {
			if (testCol >= 1 && testCol <= 8) {
				res++;
			}
		}
	}

	cout << res << endl;
	return 0;
}
//아이디어 : 그냥 다 해보기 