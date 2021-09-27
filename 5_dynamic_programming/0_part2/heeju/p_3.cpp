#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n;
int main() {
	cin >> n;
	vector<int> list(n);
	for (int i = 0; i < n; i++) {
		cin >> list[i];
	}

	vector<int> d(100);
	d[0] = list[0];
	d[1] = max(list[1], list[0]);
	for (int i = 2; i < n; i++) {
		d[i] = max(d[i - 1], d[i - 2] + list[i]);
	}

	cout << d[n - 1];
}