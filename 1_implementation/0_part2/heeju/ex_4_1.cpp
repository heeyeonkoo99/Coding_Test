#include<iostream>
#include<algorithm>
#include<deque>
using namespace std;

int n;
int main() {
	cin >> n;
	cin.ignore();
	deque<char> plan;
	int res[2] = { 1,1 };
	while(1){
		char temp;
		cin.get(temp);
		if (temp == 'R' || temp == 'L' || temp == 'U' || temp == 'D') {
			plan.push_back(temp);
		}
		else if (temp == '\n')
			break;
	}

	for (size_t i = 0; i < plan.size(); i++) {
		switch (plan[i]) {
		case 'L':
			if (res[1] != 1) {
				res[1]--;
			}break;
		case 'R':
			if (res[1] != n) {
				res[1]++;
			}break;
		case 'U':
			if (res[0] != 1) {
				res[0]--;
			}break;
		case 'D':
			if (res[0] != n) {
				res[0]++;
			}break;
		}
	}

	cout << res[0] << ' ' << res[1];
}