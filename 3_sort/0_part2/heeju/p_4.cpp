#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n; //�� �迭�� ������ ����
int k; //�ִ�� �ٲ�ġ�� �� �� �ִ� ����

int main() {
	cin >> n >> k;
	
	int* a = new int[n];
	int* b = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}


	//a�� �ø����� ����, b�� �������� ����
	sort(a, a + n);
	sort(b, b + n, [](int i, int j) {return (i > j); });

	//�ٲ�ġ�� ���� ����
	for (int i = 0; i < k; i++) {
		a[i] = b[i];
	}

	int result = 0;
	for (int i = 0; i < n; i++) {
		result += a[i];
	}

	cout << result;
}