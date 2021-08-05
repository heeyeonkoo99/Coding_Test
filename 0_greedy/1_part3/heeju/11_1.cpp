#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
int main() {
	vector<int> arr;
	int cnt = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end()); //오름차순 정렬

	while (n != 0) {
		int max = arr.back();
		n = n - max;
		arr.pop_back();
		cnt++;
	}
	
	cout << cnt << endl;
	return 0;
}