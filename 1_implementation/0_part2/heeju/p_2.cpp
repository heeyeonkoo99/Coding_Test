//�ս��� ����Ʈ
#include<iostream>
#include<algorithm>
using namespace std;

char row; //��
int col; //��
int main() {
	int move[8][2] = { {1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1} }; //����Ʈ�� ������ �� �� �� �ִ� ����� ����� ��
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
//���̵�� : �׳� �� �غ��� 