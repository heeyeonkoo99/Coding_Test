#include<iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;

    int size = food_times.size();
    for (int i = 0; i <= k ; i++) {
        int idx = i % size;
        int cnt = 0;
        while(food_times[idx]==0){
            if (cnt == 3)
                return -1;
            idx = (++idx) % size;
            cnt++;
        }
        food_times[idx]--;
        if (i == k)
            answer = idx;
    }

    return answer;
}

int main() {
    int ia[] = { 1,1,0 };
    vector<int> arr(ia, ia + sizeof(ia) / sizeof(ia[0]));
    int k = 5;
    int result = solution(arr, k);
    cout << result << endl;
}