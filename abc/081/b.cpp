#include <bits/stdc++.h>
using namespace std;

#define INF 1e18
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, N) cin >> A[i];

  bool fin = false;
  int ans = 0;
  while (!fin) {
    rep(i, N) {
      if (A[i] % 2 == 0) {
        A[i] = A[i] >> 1;
      } else {
        fin = true;
        break;
      }
    }

    if (fin)
      break;
    ans++;
  }

  cout << ans << endl;
}
