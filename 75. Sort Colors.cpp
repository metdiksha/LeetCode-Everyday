#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

void sortColors(vector<int> &nums)
{
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < nums.size(); i++)
    {
        pq.push(nums[i]);
    }
    for (int i = 0; i < nums.size(); i++)
    {
        nums[i] = pq.top();
        pq.pop();
    }
}
int main()
{
    vector<int> arr = {2, 0, 2, 0, 1, 1, 0, 0};
    sortColors(arr);
    for (int i = 0; i < arr.size(); i++)
    {
        cout << (arr[i]);
    }
}