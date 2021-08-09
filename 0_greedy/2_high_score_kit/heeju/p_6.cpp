#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int solution(vector<vector<int>>routes) {
	int res = 0;
	vector<int> starts;
	vector<int>ends;
	for (size_t i = 0; i < routes.size(); i++) {
		starts.push_back(routes[i][0]);
		ends.push_back(routes[i][1]);
	}

	int minStart = starts[min_element(starts.begin(), starts.end()) - starts.begin()];
	int maxEnd = ends[min_element(ends.begin(), ends.end()) - ends.begin()];

	int rangeSize = maxEnd - minStart + 1;

	int* vertical = new int[rangeSize] {};
	for (size_t i = 0; i < routes.size(); i++) {

	}

	return res;
}

int main() {
	vector<vector<int>> routes({ {-20,15},{-14,-5},{-18,-13},{-5,-3} });
	int res = solution(routes);
	cout << res << endl;
}
