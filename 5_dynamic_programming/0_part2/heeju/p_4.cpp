#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n;
int main() {
	cin >> n;
	vector<int> d(1001);
	d[1] = 1;
	d[2] = 3;
	for (int i = 3; i < n + 1; i++) {
		d[i] = d[i - 1] + d[i - 2] * 2;
	}

	cout << d[n] << endl;


}