#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N;//���� ����
int M;//���� ����

int main() {
	cin >> N >> M;
	vector<vector<int>> arr(N, vector<int>(M, 0)); //�迭 ����

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int data;
			cin >> data;
			arr[i][j] = data;
		}
	}

	int maxNum = 0;
	for (int i = 0; i < N; i++) {
		sort(arr[i].begin(), arr[i].end());
		if (maxNum <= arr[i][0])
			maxNum = arr[i][0];
	}

	cout << maxNum << endl;

}
