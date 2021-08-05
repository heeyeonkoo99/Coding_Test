#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n, m;
int main() {
	cin >> n >> m;
	vector<int> arr;
	int res = 0;

	for (int i = 0; i < n; i++) {
		int data;
		cin >> data;
		arr.push_back(data);
	}
	
	for (int i = 1; i < n; i++) {
		int stdn = arr.at(i-1);
		int cnt = count(arr.begin() + i, arr.end(), stdn) ;
		if (cnt==0){
			res += n - i;
		}
		else {
			res += n - cnt - i;
		}
	}

	cout << res << endl;
}