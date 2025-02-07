#include <bits/stdc++.h>
using namespace std;

#define INF 1e18
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  /* int N; */
  /* cin >> N; */
  int A, B;
  cin >> A >> B;
  /* vector<int> A(N); */
  /* rep(i, N) cin >> A[i]; */

  int ans = 0;
  rep2(i, A, B + 1) {
    string s = to_string(i);
    if (s[0] == s[4] && s[1] == s[3]) {
      ans++;
    }
  }
  cout << ans << endl;
}
