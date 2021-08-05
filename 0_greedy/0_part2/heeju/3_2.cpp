#if 0
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N; //�迭�� ũ��
int M; //���ڰ� �������� Ƚ��
int K; //�������� �ִ��� ������ �� �ִ� Ƚ��

int main() {
	cin >> N >> M >> K;
	vector<int> array;
	int addNum = 0; //���� Ƚ��
	int result = 0; //�ִ밪
	int flag = true;

	//�迭 ä���
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		array.push_back(num);
	}

	sort(array.begin(), array.end()); //�迭 ������������ ����
	
	while (addNum<M) {
		int data;
		if (flag){
			data = array.at(N - 1);
			cout << data << endl;
			if (addNum + K <= M) {
				result += data * K;
				addNum += K;
			}
			else {
				result += data * (M - addNum);
				addNum = M;
			}
			cout << "result:" << result << ", addNum:" << addNum << endl;
			flag = false;
		}
		else { 
			data = array.at(N - 2);
			cout << data << endl;
			result += data;
			addNum++;
			cout << "result:" << result << ", addNum:" << addNum << endl;
			flag = true;
		}
	}

	cout << "result:" << result << endl;
}
#endif

#if 1
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N; //�迭�� ũ��
int M; //���ڰ� �������� Ƚ��
int K; //�������� �ִ��� ������ �� �ִ� Ƚ��

int main() {
	cin >> N >> M >> K;
	vector<int> array;
	int result = 0; 
	int count = 0;
	int first;
	int second;

	//�迭 ä���
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		array.push_back(num);
	}

	sort(array.begin(), array.end()); //�迭 ������������ ����

	first = array.at(N - 1);
	second = array.at(N - 2);

	count = (M / (K + 1)) * K;
	count += M % (K + 1);

	result = first * count;
	result += second * (M - count);

	cout << "result:" << result << endl;
}

#endif