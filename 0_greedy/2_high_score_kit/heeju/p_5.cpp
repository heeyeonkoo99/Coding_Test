#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<deque>
using namespace std;

bool isFullyConnected(vector<vector<int>> group,int n,int&totalCost) {
	int** connectionGraph = (int**)calloc(n, sizeof(int*));
	int size = group.size();
	for (int i = 0; i < n; i++) {
		connectionGraph[i] = (int*)calloc(n, sizeof(int));
	}

	for (int i = 0; i <size; i++) {
		int idx1 = group[i][0];
		int idx2 = group[i][1];
		int cost = group[i][2];
		connectionGraph[idx1][idx2] = 1;
		connectionGraph[idx2][idx1] = 1;
		totalCost += cost;
	} //그래프 구성

	//연결성을 check해야함
	deque<int> connected;
	deque<int> unConnected;
	int stdIdx = group[0][0];
	connected.push_back(stdIdx);
	for (int i = stdIdx + 1; i < n; i++) {
		unConnected.push_back(i);
	}
	while (unConnected.size()!=0){
		int unConnectedSize = unConnected.size();
		for(int i=0;i<unConnectedSize;i++){
			int idx = unConnected.front();
			if (connectionGraph[stdIdx][idx] != 0) { //연결되어 있다면
				unConnected.pop_front();
				connected.push_front(idx);
			}
		}
		stdIdx = connected.front();
		connected.pop_front();
		if (connected.size() == 0)
			break;
	}

	cout << unConnected.size() << endl;
	return unConnected.size() == 0;
}

int solution(int n, vector<vector<int>> costs) {
	int minBridgeNum = n - 1;
	int size = costs.size();

	vector<vector<int>> copy(costs);
	sort(costs.begin(), costs.end(), [](vector<int> a, vector<int> b) {
		return a[2] < b[2];
	}); //오름차순 정렬

	deque<int> results;
	int tempRes;
	for (int i = 0; i < size - 1; i++) {
		costs.erase(costs.begin()+i);
		if (isFullyConnected(costs, n, tempRes) == true)
			results.push_back(tempRes);
	}

	if (isFullyConnected(copy, n, tempRes) == true)
		results.push_back(tempRes);

	return results[max_element(results.begin(), results.end()) - results.begin()];
}

int main() {
	vector<vector<int>> costs({ {0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8} });
	int n = 4;
	//int temp = 0;
	//bool isit=isFullyConnected(costs, n, temp);
	//cout << temp << endl << isit << endl;
	int res = solution(n, costs);
	cout << res << endl;
}
