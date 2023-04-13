#include <iostream>
using namespace std;

long long min(long long a, long long b)
{
    if (a < b)
        return a;
    else
        return b;
}

long long max(long long a, long long b)
{
    if (a > b)
        return a;
    else
        return b;
}

long long abs(long long a)
{
    if (a < 0)
        return -1 * a;
    else
        return a;
}

bool ktorastrona(long long *houses, long long sum, long long point, long long target, long long n)
{
    if (point == n)
    {
        return true;
    }
    else
    {
        long long pom = abs(houses[point] - houses[target]);
        long long odl = min(pom, sum - pom);
        pom = abs(houses[point + 1] - houses[target]);
        long long odl1 = min(pom, sum - pom);
        ;
        return odl < odl1;
    }
}

long long bins(long long *houses, long long sum, long long l, long long r, long long target, long long n)
{
    if (l == r)
    {
        long long pom = abs(houses[l] - houses[target]);
        return min(pom, sum - pom);
    }
    else if (abs(l, r) == 1)
    {
        long long pom = abs(houses[l] - houses[target]);
        long long odl = min(pom, sum - pom);
        pom = abs(houses[r], houses[target]);
        long long odl1 = min(pom, sum - pom);
        return max(odl, odl1);
    }
    else
    {

        long long sr = (l + r) / 2;
        if (ktorastrona(houses, sum, sr, target, n))
        {
            return bins(houses, sum, sr, r, target, n);
        }
        else
        {
            return bins(houses, sum, l, sr, target, n);
        }
    }
}

long long najdl(long long *houses, long long sum, long long target, long long n)
{
    long long l = bins(houses, sum, 0, target, target, n);
    long long r = bins(houses, sum, target, n - 1, target, n);
    return max(l, r);
}
long long rozw(long long *houses, long long sum, long long n)
{
    long long maks = 0, dl;
    for (long long i = 0; i < n; i++)
    {
        dl = najdl(houses, sum, i, n);
        if (dl > maks)
        {
            maks = dl;
        }
    }
    return maks;
}
long long houses[1000000 + 7];
int main()
{
    long long n;
    cin >> n;

    long long sum = 0;
    long long pom;

    for (long long i = 0; i < n; i++)
    {

        cin >> pom;
        houses[i] = sum;
        sum += pom;
    }

    cout << rozw(houses, sum, n);
    return 0;
}