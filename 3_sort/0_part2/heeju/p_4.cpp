#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n; //두 배열의 원소의 개수
int k; //최대로 바꿔치기 할 수 있는 개수

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


	//a는 올림차순 정렬, b는 내림차순 정렬
	sort(a, a + n);
	sort(b, b + n, [](int i, int j) {return (i > j); });

	//바꿔치기 연산 수행
	for (int i = 0; i < k; i++) {
		a[i] = b[i];
	}

	int result = 0;
	for (int i = 0; i < n; i++) {
		result += a[i];
	}

	cout << result;
}