#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n;
bool func(int i, int j) { return (i > j); }
int main() {
	cin >> n;
	vector<int>  numArr;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		numArr.push_back(temp);
	}

	sort(numArr.begin(), numArr.end(), func);

	for (int i = 0; i < n; i++)
		cout << numArr[i] << ' ';
	return 0;
}