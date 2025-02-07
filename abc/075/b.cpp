#include <bits/stdc++.h>
#include <string>
using namespace std;

#define INF 1e18
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  /* int N; */
  /* cin >> N; */
  /* int N, M; */
  /* cin >> N >> M; */
  /* vector<int> A(N); */
  /* rep(i, N) cin >> A[i]; */

  int H, W;
  cin >> H >> W;
  string S[50];
  rep(i, H) cin >> S[i];

  rep(i, H) {
    rep(j, W) {
      if (S[i][j] == '#')
        continue;

      int count = 0;
      if (i > 0) {
        if (S[i - 1][j] == '#')
          count++;
        if (j > 0)
          if (S[i - 1][j - 1] == '#')
            count++;
        if (j < W - 1) {
          if (S[i - 1][j + 1] == '#')
            count++;
        }
      }
      if (i < H - 1) {
        if (S[i + 1][j] == '#')
          count++;
        if (j > 0)
          if (S[i + 1][j - 1] == '#')
            count++;
        if (j < W - 1)
          if (S[i + 1][j + 1] == '#')
            count++;
      }
      if (j > 0 && S[i][j - 1] == '#')
        count++;
      if (j < W - 1 && S[i][j + 1] == '#')
        count++;

      S[i][j] = char(count + '0');
    }
  }

  rep(i, H) cout << S[i] << endl;
}
