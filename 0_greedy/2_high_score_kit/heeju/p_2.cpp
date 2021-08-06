//알파벳이 M보다 앞이면 위로 올리는것이
//M보다 크면 밑으로 조작하는 것이 더 유리하다
//조이스틱을 좌우로 조작하는 것이 핵심
//A의 위치를 알아야 한다.
//A가 아닌 친구들간의 거리를 측정해야하나?

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int solution(string name) {
	int result = 0;
	int nameLen = name.size();

	//일단 위아래로 움직이는 횟수 계산하기
	for (int i = 0; i < nameLen; i++) {
		if (name[i] == 'A')
			continue;
		if (name[i] <= 'M')
			result += name[i] - 'A';
		else
			result += 'Z' + 1 - name[i];
	} //제대로 동작

	vector<int> aOrNot(nameLen, 0);
	for (int i = 0; i < nameLen; i++) {
		if (name[i] == 'A')
			aOrNot[i] = 1;
	}

	//좌우로 움직이는 횟수 계산
	//case1)마지막 문자가 A인 경우
	//	그냥 우로 전진하는 것이 제일 빠른경로
	//case2)마지막 문자가 A가 아닌 경우
	// 1.첫번째 A가 나올때까지는 우로가다가 첫번째 A를 만나면 뒤로 돌아가기
	// 2.그냥 우로 전진
	// 위의 두가지 경우 비교해서 작은 수가 답
	if (name[nameLen - 1] == 'A')
		result += find_end(aOrNot.begin(), aOrNot.end(), ((vector<int>)0).begin(), ((vector<int>)0).end()) - aOrNot.begin() ;
	else {
		int res1;
		int firstAidx = find(name.begin(), name.end(), 'A') - name.begin();
		int backDis = nameLen - (find(aOrNot.begin() + firstAidx, aOrNot.end(), 0) - aOrNot.begin());
		res1 = (firstAidx-1) * 2 + backDis;
		result += min(res1, nameLen - 1);
	}
	return result;
}

int main() {
	int result = solution("JEROEN");
	cout << result << endl;
}