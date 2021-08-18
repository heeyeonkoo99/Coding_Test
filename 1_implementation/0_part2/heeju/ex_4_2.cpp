#include<iostream>
#include<cstring>
using namespace std;

int n;
int main() {
	cin >> n;

	int cnt = 0;

	for (int i = 0; i <= n; i++) {
		if (i  == 3) {
			cnt += 60 * 60;
			continue;
		}
		for (int j = 0; j < 60; j++) {
			if (j == 3||j/10==3) {
				cnt += 60;
				continue;
			}
			for (int k = 0; k < 60; k++) {
				if (k==3||k/10==3)
					cnt++;
			}
		}
	}
	cout << cnt << endl;

}