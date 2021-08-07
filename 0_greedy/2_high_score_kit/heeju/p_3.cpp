#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;


string solution(string numStr, int k) {
	string res = "";
	int resLen = numStr.size() - k;

	for (int i = resLen; i >= 1; i--) {
		int numLen = numStr.size();
		int idx = max_element(numStr.begin(), numStr.begin() + (numLen - (i-1))) - numStr.begin();
		res += numStr[idx];
		numStr.erase(0,idx+1);
	}

	return res;
}

int main() {
	string number = "1924";
	int k = 2;
	string result = solution(number, k);
	cout << result << endl;
}

/* 
- 문제 정리 : 숫자로 이루어진 n길이의 문자열에서 k개의 수를 제거해서 가장 큰 수를 나타내는 문자열을 만들어야 한다.
  따라서 n-k길이의 가장 큰 수가 되는 정답 문자열을 찾아야 한다.

- 주의할점(간과한 부분) : 정렬을 통해서 답을 구하면 안된다. 왜냐면 기존의 문자열에서 중간 중간 숫자를 삭제하는 것이므로 숫자들의 앞뒤관계를 바꿀 수 없다.

- 아이디어 :
	항상 문자열에서 연속한 부분문자열의 첫번째 자리 숫자를 구한다는 생각으로 정답 문자열의 각 자리에 올 숫자를 구한다.
	정답이 될 문자열의 첫번째 숫자는 다음과 같이 구한다.
		정답문자열은 곧 주어진 문자열의 부분문자열이다. 
		이를 이용해서 첫번째 숫자를 탐색할 범위를 구하고 해당 범위내에서 가장 큰 숫자를 구한다.
		정답문자열의 길이가 n-k이고 주어진 문자열의 길이가 n이다. 
		따라서 첫번째 숫자는 탐색할 범위는 다음과 같다.
			[0] ~ [k] <== n-(n-k-1) 
		해당 범위에서 가장 큰 숫자가 정답 문자열의 첫번째 자리에 오는 숫자가 된다. (max_element(first_iteratir,last_iterator)를 이용해서 [first_iterator,last_iterator)에서 가장 큰 숫자를 탐색)
		이 때 해당 숫자의 앞의 인덱스는 정답 문자열에 포함될 수 없다. (erase(first_idx,last_idx)를 이용해서 [first_idx,last_idx)까지의 문자를 제거)
		또한 다음 로직을 위해서 첫번째 숫자또한 문자열에서 삭제한다.
	동일한 로직을 이용해서 정답 문자열의 두번째 자리 수를 구한다.

	예시) "1924" k=2인 경우
		일단 2자리로 이루어진 숫자에서 첫번째 자리(십의 자리)에 올 숫자를 구한다.
		문자열의 길이가 4이고 k가 2이므로 4-(2-1)=3이다.
		따라서 맨앞에서 세번째 숫자까지 해당하는 1,9,2를 탐색한다.
		세 수중 가장 큰 수는 9이다.
		이제 "1924"에서 9까지의 숫자들을 제거한다. 
		그러면 문자열은 "24"가 되고 해당 문자열에서 정답문자열의 1의 자리 수를 구한다.
		이 때는 문자열의 길이가 2이고 k=1이므로 2-(1-1)=2
		맨 앞에서 두번째 숫자까지 즉 2,4를 탐색해서 가장 큰 수를 찾는다.
		이는 4이다.
		따라서 정답은 "94"가 된다.
*/
