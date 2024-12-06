#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
 
#define int long long int
#define fast_io()                \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);            \
    cout.tie(nullptr);
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define si set<int>
#define sti stack<int>
#define pop st.pop();
#define top st.top();
#define push(a) st.push(a);
#define given                   \
    int n;                      \
    cin >> n;
#define take(a, n)              \
    for (int j = 0; j < n; j++) \
        cin >> a[j];
#define show(a, n)              \
    for (int j = 0; j < n; j++) \
        cout << a[j] << ' ';    \
    cout << '\n';
#define all(x) x.begin(), x.end()
#define yes cout << "YES" << '\n';
#define no cout << "NO" << '\n';
#define nl '\n'
#define MOD1 998244353
#define PI 3.141592653589793238462

string decToBinary(int n)
{
    string s = "";
    for (int i = 31; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
              s+="1";
        else s+="0";
    }
    return s;
}

signed main() {

    fast_io()
    
    given
    string s = "";
    while (n > 0) {
        s = char((n % 2) + '0') + s;
        n /= 2;
    }
    // cout << s << nl;
    int j;
    for(j = 0; j<s.length(); j++){
        if(s[j] =='1'){
            break;
        }
    }
    int gap = 0;
    int prev = -1;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '1') {
            if (prev != -1) {
                gap = max(gap, i - prev);
            }
            prev = i;
        }
    }
    cout << gap;
    return 0;
}