#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int x;
int main() {
	cin >> x;
	vector<int> d(x + 1);
	d[1] = 0;
	for (int i = 2; i < x + 1; i++) {
		d[i] = d[i - 1] + 1;
		if (i % 2 == 0)
			d[i] = min(d[i], d[i / 2] + 1);
		if (i % 3 == 0)
			d[i] = min(d[i], d[i / 3] + 1);
		if (i % 5 == 0)
			d[i] = min(d[i], d[i / 5] + 1);
	}

	cout << d[x] << endl;
}