#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int solution(vector<int> people, int limit) { //효율성 test실패 ==> index로 범위 관리
	int res = 0;
	int startIdx = 0;
	int lastIdx = people.size() - 1;
	sort(people.begin(), people.end());
	while (lastIdx>=startIdx){
		res++;
		int maxWeight = people[lastIdx];
		int minWeight = people[startIdx];
		lastIdx--;
		if (maxWeight + minWeight <= limit)
			startIdx++;
	}
	return res;
}

int main() {
	vector<int> people;
	people.push_back(50);
	people.push_back(50);
	people.push_back(50);
	people.push_back(70);
	people.push_back(80);
	int limit = 100;
	int result = solution(people, limit);
	cout << result << endl;
}