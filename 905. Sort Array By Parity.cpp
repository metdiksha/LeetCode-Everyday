#include <iostream>
#include <bits/stdc++.h>
using namespace std;
vector<int> sortArrayByParity(vector<int> &nums)
{
    priority_queue<int> even;
    priority_queue<int> odd;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] % 2 == 0)
        {
            even.push(nums[i]);
        }
        else
        {
            odd.push(nums[i]);
        }
    }
    int i = 0;
    while (!even.empty())
    {
        nums[i++] = even.top();
        even.pop();
    }
    while (!odd.empty())
    {
        nums[i++] = odd.top();
        odd.pop();
    }
    return nums;
}
int main()
{
    vector<int> nums = {3, 1, 2, 4};
    vector<int> ret = sortArrayByParity(nums);
    for (int i = 0; i < ret.size(); i++)
    {
        cout << ret[i] << endl;
    }
}