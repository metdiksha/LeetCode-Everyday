#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
{
    nums1.insert(nums1.begin(), nums2.begin(), nums2.end());
    double median = 0.00;
    priority_queue<int> pq;
    int n = nums1.size();
    for (int i = 0; i < n; i++)
    {
        pq.push(nums1[i]);
    }

    int mid = n / 2;
    int last = 0;
    if (n % 2 == 0)
    {
        while (mid > 0)
        {
            last = pq.top();
            pq.pop();
            mid--;
        }

        median = (pq.top() + last) / 2.0;
        return median;
    }
    else
    {
        while (mid >= 0)
        {
            median = pq.top();
            pq.pop();
            mid--;
        }
        return median;
    }
    return median;
}

int main()
{
    vector<int> v1 = {1};
    vector<int> v2 = {2, 3, 4};
    double ret = findMedianSortedArrays(v1, v2);
    cout << ret;
}