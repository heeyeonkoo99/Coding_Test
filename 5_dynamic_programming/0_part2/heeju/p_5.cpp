#include<iostream>
#include<vector>
#include<algorithm>
#define MAX (10001)
using namespace std;

int n;
int m;
int main() {
	cin >> n >> m;

	vector<int> valueList(n);
	vector<int> d(m + 1);
	d.assign(m + 1, MAX);

	for (int i = 0; i < n; i++) {
		cin >> valueList[i];
	}

	for (int i = 0; i < n; i++) {
		int cur = valueList[i];
		for (int j = cur; j <= m; j++) {
			if (d[j - cur] != MAX)
				d[j] = min(d[j], d[j - cur] + 1);
		}
	}

	if (d[m] != MAX)
		cout << d[m] << endl;
	else
		cout << -1 << endl;
}
