#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int heightChecker(vector<int> &heights)
{
    vector<int> temp = heights;
    sort(temp.begin(), temp.end());
    int n = heights.size();
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (temp[i] != heights[i])
        {
            count++;
        }
    }
    return count;
}
int main()
{
    vector<int> arr = {1, 5, 3, 7, 8};
    int ret = heightChecker(arr);
    cout << ret;
}