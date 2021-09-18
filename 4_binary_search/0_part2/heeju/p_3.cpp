#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
int m;
int main() {
	cin >> n >> m;
	vector<int> ddeokHeightList;

	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		ddeokHeightList.push_back(temp);
	}

	int res = 0;
	int start = 0;
	int end = *max_element(ddeokHeightList.begin(), ddeokHeightList.end());
	while (start <= end) {
		int mid = (start + end) / 2;
		int total = 0;
		for (int i = 0; i < n; i++) {
			if (ddeokHeightList[i] > mid)
				total += ddeokHeightList[i] - mid;
		}
		/*
		if (res > m)
			start = mid + 1;
		else if (res == m)
			break;
		else
			end = mid - 1;
		*/
		if (total < m) //¿ÞÂÊÅ½»ö ÇÊ¿ä
			end = mid - 1;
		else {
			res = mid;
			start = mid + 1;
		}
	}

	cout << res << endl;
}