#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int n;

typedef struct {
	string name;
	int score;
}Student;

bool func(Student a, Student b) { return (a.score < b.score); }
int main() {
	cin >> n;
	vector<Student> stdArr;
	for (int i = 0; i < n; i++) {
		Student tStd;
		cin >> tStd.name >> tStd.score;
		stdArr.push_back(tStd);
	}
	sort(stdArr.begin(), stdArr.end(), func);
	for (int i = 0; i < n; i++) {
		cout << stdArr[i].name << ' ';
	}
	return 0;
}