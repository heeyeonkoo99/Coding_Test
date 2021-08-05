#if 0
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N; //배열의 크기
int M; //숫자가 더해지는 횟수
int K; //연속으로 최대한 더해질 수 있는 횟수

int main() {
	cin >> N >> M >> K;
	vector<int> array;
	int addNum = 0; //더한 횟수
	int result = 0; //최대값
	int flag = true;

	//배열 채우기
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		array.push_back(num);
	}

	sort(array.begin(), array.end()); //배열 오름차순으로 정리
	
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

int N; //배열의 크기
int M; //숫자가 더해지는 횟수
int K; //연속으로 최대한 더해질 수 있는 횟수

int main() {
	cin >> N >> M >> K;
	vector<int> array;
	int result = 0; 
	int count = 0;
	int first;
	int second;

	//배열 채우기
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		array.push_back(num);
	}

	sort(array.begin(), array.end()); //배열 오름차순으로 정리

	first = array.at(N - 1);
	second = array.at(N - 2);

	count = (M / (K + 1)) * K;
	count += M % (K + 1);

	result = first * count;
	result += second * (M - count);

	cout << "result:" << result << endl;
}

#endif