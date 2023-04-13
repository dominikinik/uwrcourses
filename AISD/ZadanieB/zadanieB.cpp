#include <iostream>
#include <algorithm>
using namespace std;
int a, b;
short tab[3][10000];
long long tab2[3][10000];

long long pot(short a)
{
    if (a == 0)return 1;
    if (a == 1)return 7;
    if (a == 2)return 49;
    if (a == 3)return 343;
    if (a == 4)return 2401;
    if (a == 5)return 16807;
    if (a == 6)return 117649;
    if (a == 7)return 823543;
    if (a == 8)return 5764801;
    if (a == 9)return 40353607;
    return -1;
}

void uzupelniaj1(int w)
{ // brzegowe
  //  cout<<(w+2)%3<<endl;
    tab2[(w + 2) % 3][1] = max(tab2[(w + 2) % 3][1], tab2[w % 3][0] + pot(tab[(w + 2) % 3][1]));
    tab2[(w + 2) % 3][b - 2] = max(tab2[(w + 2) % 3][b - 2], tab2[w % 3][b - 1] + pot(tab[(w + 2) % 3][b - 2]));

    for (int i = 1; i < b - 1; i++)
    {
        tab2[(w + 2) % 3][i - 1] = max(tab2[(w + 2) % 3][i - 1], tab2[w % 3][i] + pot(tab[(w + 2) % 3][i - 1]));
        tab2[(w + 2) % 3][i + 1] = max(tab2[(w + 2) % 3][i + 1], tab2[w % 3][i] + pot(tab[(w + 2) % 3][i + 1]));
    }
}

void uzupelnij2(int w)
{
    for (int i = 0; i < 2; i++)
        tab2[(w - 1) % 3][i + 2] = max(tab2[(w - 1) % 3][i + 2], tab2[w % 3][i] + pot(tab[(w - 1) % 3][i + 2]));
    for (int i = b - 2; i < b; i++)
        tab2[(w - 1) % 3][i - 2] = max(tab2[(w - 1) % 3][i - 2], tab2[w % 3][i] + pot(tab[(w - 1) % 3][i - 2]));

    for (int i = 2; i < b - 2; i++)
    {
        tab2[(w - 1) % 3][i + 2] = max(tab2[(w - 1) % 3][i + 2], tab2[w % 3][i] + pot(tab[(w - 1) % 3][i + 2]));
        tab2[(w - 1) % 3][i - 2] = max(tab2[(w - 1) % 3][i - 2], tab2[w % 3][i] + pot(tab[(w - 1) % 3][i - 2]));
    }
}

int main()
{
    cin >> a >> b;
    string pom;
    cin >> pom;
    for (int i = 0; i < b; i++)
    {
        tab[0][i] = pom[i] - '0';
        tab2[0][i] = pot(pom[i] - '0');
    }
    for (int j = 1; j < 3; j++)
    {
        cin >> pom;
        for (int i = 0; i < b; i++)
        {
            tab[j][i] = pom[i] - '0';
            tab2[j][i] = pot(pom[i] - '0');
        }
    }
    int w = 0;
    for (int i = 2; i < a - 1; i++)
    {
        uzupelniaj1(w);
        w += 2;
        uzupelnij2(w);
        w -= 1;
        cin >> pom;
        for (int i = 0; i < b; i++)
            tab[(w + 2) % 3][i] = pom[i] - '0';
    }
    uzupelniaj1(w);
    long long maks = 0;
  
    for (int i = 0; i < b; i++)
        maks = max(maks, tab2[(a - 1) % 3][i]);

    cout << maks;

    return 0;
    
}