#include<iostream> 
#include<vector>
#include<string>
using namespace std;

string s;
int main() {
	cin >> s;
	int cCnt = 0;
	vector<bool> arr;
	int strLen = s.length();
	int result;

	for (int i = 0; i < strLen; i++) {
		arr.push_back((bool)stoi(s.substr(i, 1)));
	}

	
	bool flag = arr.front();
	for (int i = 1; i < strLen; i++) {
		if (arr[i] != flag) {
			cCnt++;
			flag = arr[i];
		}
	}

	result = (cCnt % 2 == 0) ? cCnt / 2 : (cCnt / 2) + 1;

	cout << result << endl;
}