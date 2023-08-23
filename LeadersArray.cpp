#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> leaders(int a[], int n) {
        vector<int> k;
        int r = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (a[i] >= r) {
                r = a[i];
                k.insert(k.begin(), a[i]);
            }
        }
        k.push_back(a[n - 1]);
        return k;
    }
};

int main() {
    int n;
    cout << "Please enter the length of the array: ";
    cin >> n;

    int a[n];
    cout << "Please enter the elements of the array:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    vector<int> result = solution.leaders(a, n);
    cout << "The Leaders of array are contains:";
    for (int i = 0; i < result.size(); i++) {
        cout << " " << result[i];
    }    
 
    // for (int num : result) {
    //     cout << num << " ";
    // }

    return 0;
}
