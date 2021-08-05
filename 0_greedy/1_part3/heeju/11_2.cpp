#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

bool compare(int a, int b) {
	return b < a;
}

string s;
int main() {
	cin >> s;
	int strLength = s.length();
	int result;
	vector<int> arr;

	for (int i = 0; i < strLength; i++) {
		string temp = s.substr(i, 1);
		arr.push_back(std::stoi(temp));
	}

	sort(arr.begin(), arr.end(),compare); //내림차순으로 정렬

	result = arr.front();

	for (int i = 1; i < strLength; i++) {
		if (arr[i] == 0) {
			result += arr[i];
			break;
		}
		result *= arr[i];
	}

	cout << result << endl;
}

