#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;
vector<int> sortEvenOdd(vector<int> &nums)
{
    priority_queue<int, vector<int>, greater<int>> even;
    priority_queue<int> odd;
    for (int i = 0; i < nums.size(); i = i + 2)
    {
        even.push(nums[i]);
    }
    for (int i = 1; i < nums.size(); i = i + 2)
    {
        odd.push(nums[i]);
    }
    int count = 0;

    while ((!even.empty()) || (!odd.empty()))
    {

        if (count % 2 == 0)
        {
            nums[count] = even.top();
            even.pop();
        }
        else
        {
            nums[count] = odd.top();
            odd.pop();
        }
        count++;
    }
    return nums;
}

int main()
{

    vector<int> v1 = {4, 1, 2, 3};
    vector<int> ret = sortEvenOdd(v1);
    for (int i = 0; i < ret.size(); i++)
    {
        cout << ret[i] << endl;
    }
}