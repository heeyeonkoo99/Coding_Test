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
	else if (list[mid] < target) //������ Ž��
		return binarySearch(list, target, mid + 1, end);
	else //���� Ž��
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
	} //�Է¹޾Ƽ� ����Ʈ �ۼ��ϱ�

	sort(stockList.begin(), stockList.end()); //��� ����Ʈ �����ϱ�

	for (int i = 0; i < m; i++) { //�ֹ� ����Ʈ�� �ֹ���ȣ�� �ϳ��� �Լ��� ������ ����Ž���� �����Ѵ�. 
		if (binarySearch(stockList, orderList[i], 0, n - 1)>0)
			cout << "yes ";
		else
			cout << "no ";

	}
}
