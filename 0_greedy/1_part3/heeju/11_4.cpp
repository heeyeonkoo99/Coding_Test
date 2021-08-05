#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n;
int main() {
	vector<int> arr;
	int total = 0;
	int target = 1;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int data;
		cin >> data;
		arr.push_back(data);
		total += data;
	}

	sort(arr.begin(), arr.end());
	for (int i = 0; i < n; i++) {
		if (target < arr[i])
			break;
		target += arr[i];
	}

	cout << target << endl;
}