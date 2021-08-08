#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int solution(vector<int> people, int limit) { //ȿ���� test����
	int res = 0;
	sort(people.begin(), people.end());
	while (people.size() > 0) { 
		int maxWeight = *(--people.end());
		people.pop_back();  //�ǵڿ� �� �������ϱ� �����
		res++;
		if (people.size() == 0) //���� ���� ������������ check�������
			break;
		int minWeight = *(people.begin());
		if (maxWeight + minWeight <= limit)
			people.erase(people.begin());
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