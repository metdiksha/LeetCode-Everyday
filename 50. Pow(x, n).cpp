#include <iostream>
using namespace std;
double myPow(double x, int n)
{
    if (n < 0)
    {
        x = 1 / x;
        n = abs(n);
    }
    if (n == 0)
    {
        return 1;
    }
    if (n % 2 == 0)
        return myPow(x * x, n / 2);
    return x * myPow(x * x, (n - 1) / 2);
}

int main()
{
    cout << myPow(2.000, 5);
}