#if 0 
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N; //나누어지는 수
int K; //나누는 수

int main() {
	cin >> N >> K;
	int cnt = 0;

	while (N >= K) {
		while (N % K != 0) {
			N--;
			cnt++;
		}
		N /= K;
		cnt++;
	}

	while (N > 1) {
		N--;
		cnt++;
	}

	cout << cnt << endl;

}
#endif

#if 1
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N; //나누어지는 수
int K; //나누는 수

int main() {
	cin >> N >> K;
	int cnt = 0;

	while (1){
		int target = (N / K) * K;
		cnt += N - target;
		N = target;
		if (N < K)
			break;
		N /= K;
	}

	cnt += (N - 1);

	cout << cnt << endl;

}
#endif
