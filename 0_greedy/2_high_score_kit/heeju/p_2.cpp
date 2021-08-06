//���ĺ��� M���� ���̸� ���� �ø��°���
//M���� ũ�� ������ �����ϴ� ���� �� �����ϴ�
//���̽�ƽ�� �¿�� �����ϴ� ���� �ٽ�
//A�� ��ġ�� �˾ƾ� �Ѵ�.
//A�� �ƴ� ģ���鰣�� �Ÿ��� �����ؾ��ϳ�?

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int solution(string name) {
	int result = 0;
	int nameLen = name.size();

	//�ϴ� ���Ʒ��� �����̴� Ƚ�� ����ϱ�
	for (int i = 0; i < nameLen; i++) {
		if (name[i] == 'A')
			continue;
		if (name[i] <= 'M')
			result += name[i] - 'A';
		else
			result += 'Z' + 1 - name[i];
	} //����� ����

	vector<int> aOrNot(nameLen, 0);
	for (int i = 0; i < nameLen; i++) {
		if (name[i] == 'A')
			aOrNot[i] = 1;
	}

	//�¿�� �����̴� Ƚ�� ���
	//case1)������ ���ڰ� A�� ���
	//	�׳� ��� �����ϴ� ���� ���� �������
	//case2)������ ���ڰ� A�� �ƴ� ���
	// 1.ù��° A�� ���ö������� ��ΰ��ٰ� ù��° A�� ������ �ڷ� ���ư���
	// 2.�׳� ��� ����
	// ���� �ΰ��� ��� ���ؼ� ���� ���� ��
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