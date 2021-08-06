#include<iostream>
#include <string>
#include <vector>
#include<algorithm>

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    int size = food_times.size();
    int foodNum = 0;

    for (int i = 0; i < k; i++) {
        foodNum = (i + 1) % size; 
        int cnt = 0;
        while (1) {
            if (food_times[foodNum - 1] != 0) {
                food_times[foodNum - 1]--;
                break;
            }
            else { //해당 번호 음식이 남아있지 않다면 -->다음번호로 넘어가야함
                foodNum++;
                cnt++;
                if (foodNum > size )
                    foodNum = 1;
                if (cnt == size)
                    return -1;
            }
        }
    }
    answer = (foodNum + 1) % size;
    return answer;
}

int main() {
    int ia[] = { 1,1,0 };
    vector<int> arr(ia, ia + sizeof(ia) / sizeof(ia[0]));
    int k = 5;
    int result = solution(arr, k);
    cout << result << endl;
}