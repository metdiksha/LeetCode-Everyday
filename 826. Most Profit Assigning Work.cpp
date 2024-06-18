#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int maxProfitAssignment(vector<int> &difficulty, vector<int> &profit, vector<int> &worker)
{
    int n = profit.size();
    int m = worker.size();
    int pro = 0;
    vector<int> max_profit(m, 0);

    vector<pair<int, int>> assigned;
    for (int i = 0; i < n; i++)
    {
        assigned.push_back(make_pair(difficulty[i], profit[i]));
    }
    sort(assigned.begin(), assigned.end());
    sort(worker.begin(), worker.end());
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (assigned[j].first <= worker[i])
            {
                max_profit[i] = max(max_profit[i], assigned[j].second);
            }
            else
            {
                break;
            }
        }
        pro += max_profit[i];
    }
    return pro;
}
int main()
{
    vector<int> difficulty = {2, 4, 6, 8, 10};
    vector<int> profit = {10, 20, 30, 40, 50};
    vector<int> worker = {4, 5, 6, 7};
    int ret = maxProfitAssignment(difficulty, profit, worker);
    cout << ret;
}