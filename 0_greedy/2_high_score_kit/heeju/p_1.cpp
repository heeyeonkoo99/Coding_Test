//테스트 케이스 5번에서 계속 막힘ㅠㅠ
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int solution(int n, vector<int>lost, vector<int> reserve) {
	int result;
	vector<int> std(n, 0);

	sort(reserve.begin(), reserve.end());
	for (int i = 0; i < reserve.size(); i++) {
		int standard = reserve[i];

		vector<int>::iterator self = find(lost.begin(), lost.end(), standard);
		if (self != lost.end()) { //내체육복 없음
			lost.erase(self);
			continue;
		}

		vector<int>::iterator front = find(lost.begin(), lost.end(), standard-1);
		if (front != lost.end()) { //앞에 친구 체육복 없음.
			lost.erase(front); //앞친구한테 빌려줌
			continue;
		}

		vector<int>::iterator back = find(lost.begin(), lost.end(), standard + 1);
		if (back != lost.end()){
				lost.erase(back);
		}
	}

	result = n - lost.size();
	return result;
}

int main() {
	int n = 5;
	int aLost[] = {2,4};
	int aReserve[] = { 1,3,5 };
	int result;
	vector<int>lost(aLost, aLost + sizeof(aLost) / sizeof(aLost[0]));
	vector<int> reserve(aReserve, aReserve + sizeof(aReserve) / sizeof(aReserve[0]));
	result = solution(n, lost, reserve);
	cout << result << endl;
}