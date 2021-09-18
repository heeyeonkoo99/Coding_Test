#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int n;
int m;

int binarySearch(vector<int> list, int target, int start, int end){
	if (start > end)
		return -1;
	int mid = (start + end) / 2;
	if (list[mid] == target)
		return mid;
	else if (list[mid] < target) //오른쪽 탐색
		return binarySearch(list, target, mid + 1, end);
	else //왼쪽 탐색
		return binarySearch(list, target, start, mid - 1);
}
int main(){
	cin >> n;
	vector<int> stockList;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		stockList.push_back(temp);
	}

	cin >> m;
	vector<int> orderList;
	for (int i = 0; i < m; i++) {
		int temp;
		cin >> temp;
		orderList.push_back(temp);
	} //입력받아서 리스트 작성하기

	sort(stockList.begin(), stockList.end()); //재고 리스트 정렬하기

	for (int i = 0; i < m; i++) { //주문 리스트의 주문번호를 하나씩 함수로 보내서 이진탐색을 진행한다. 
		if (binarySearch(stockList, orderList[i], 0, n - 1)>0)
			cout << "yes ";
		else
			cout << "no ";

	}
}
