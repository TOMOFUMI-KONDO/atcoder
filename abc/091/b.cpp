#include <bits/stdc++.h>
using namespace std;

#define INF 1e18
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, m = 0;
  cin >> n;
  vector<string> S(n);
  rep(i, n) cin >> S.at(i);

  cin >> m;
  vector<string> T(m);
  rep(i, m) cin >> T.at(i);

  map<string, int> counts;
  rep(i, n) {
    string s = S.at(i);
    counts[s] = counts.count(s) == 0 ? 1 : counts.at(s) + 1;
  }
  rep(i, m) {
    string t = T.at(i);
    counts[t] = counts.count(t) == 0 ? -1 : counts.at(t) - 1;
  }

  int ans = 0;
  for (auto v = counts.begin(); v != counts.end(); v++) {
    ans = max(ans, v->second);
  }

  cout << ans << endl;
}
