#include <iostream>
#include <iomanip>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <vector>
#include <utility>
#include <algorithm>
#include <numeric>
#include <string>
#include <cmath>
#include <random>
#include <sstream>
#include <string.h>
#include <assert.h>
#include <limits.h>
using namespace std;

#define fi first
#define se second
#define int long long

typedef pair<int,int> ii;

mt19937 rng;

map<string,vector<pair<string,int>>> adj;
map<string,int> gender;
map<vector<int>,int> tot;

void initGender() {
  // 0 (Wanita), 1 (Pria)
  gender["Ani"] = 0;
  gender["Budi"] = 1;
  gender["Cici"] = 0;
  gender["David"] = 1;
  gender["Eva"] = 0;
  gender["Farhan"] = 1;
  gender["Gunawan"] = 1;
  gender["Hendra"] = 1;
  gender["Joko"] = 1;
  gender["Kate"] = 0;
  gender["Lisa"] = 0;
}

void addEdge(string a, string b, int w) {
  // cout << a << ' ' << b << ' ' << w << endl;
  adj[a].push_back({b,w});
  adj[b].push_back({a,w});
}

void calculateGraph() {
  map<vector<int>,int> cnt;

  for (auto i : gender) {
    string u = i.fi;
    for (auto j : adj[u]) {
      string v = j.fi;
      int w = j.se;
      if (gender[u] > gender[v]) {
        cnt[{gender[v], w, gender[u]}]++;
      }
      else {
        cnt[{gender[u], w, gender[v]}]++;
      }
    }
  }
  for (auto i : cnt) {
    i.se /= 2;
    // for (int j : i.fi) cout << j << " ";
    // cout << "-> " << i.se << '\n';
    tot[i.fi] += i.se;
  }

  for (int p : {0,1}) {
    for (int a : {1,2}) {
      for (int q : {0,1}) {
        for (int b : {1,2}) {
          for (int r : {0,1}) {
            if (a > b || p > r) continue;
            int all = 0;
            for (auto i : gender) {
              string u = i.fi;
              if (gender[u] != q) continue;
              int cntP = 0, cntR = 0;
              for (auto j : adj[u]) {
                string v = j.fi;
                int w = j.se;
                cntP += (gender[v] == p && w == a);
                cntR += (gender[v] == r && w == b);
              }
              if (p == 1 && a == 1 && q == 0 && b == 2 && r == 1) {
                cout << u << " -> " << cntP << " " << cntR << endl;
              }
              if (p == r && a == b) {
                all += cntP * (cntR-1) / 2;
                if (cntP * (cntR-1) / 2 > 0) {
                  cout << u << q << ' ' << p << a << ' ' << q << b << " -> " << cntP*(cntR-1)/2 << '\n';
                }
              }
              else {
                all += cntP * cntR;
                if (cntP *cntR > 0) {
                  cout << u << q << ' ' << p << a << ' ' << q << b << " -> " << cntP*cntR << '\n';
                }
              }
            }
            assert(all >= 0);
            if (p == 1 && a == 1 && q == 0 && b == 2 && r == 1) cout << all << '\n';
            tot[{p,a,q,b,r}] += all;
          }
        }
      }
    }
  }
  cout << '\n';
}

bool cmp(pair<int,vector<int>> a, pair<int,vector<int>> b) {
  return a.fi > b.fi;
}

signed main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  
  initGender();
  
  // Graph 1
  adj.clear();
  addEdge("Ani", "Budi", 2);
  addEdge("Ani", "Cici", 2);
  addEdge("Budi", "Cici", 1);
  addEdge("Budi", "David", 1);
  addEdge("Cici", "Eva", 2);
  addEdge("David", "Joko", 2);
  addEdge("David", "Lisa", 2);
  addEdge("Eva", "Lisa", 2);
  addEdge("Eva", "Farhan", 1);
  addEdge("Gunawan", "Farhan", 2);
  addEdge("Gunawan", "Hendra", 1);
  calculateGraph();
  
  // Graph 2
  adj.clear();
  addEdge("Budi", "Joko", 1);
  addEdge("Budi", "Ani", 1);
  addEdge("Joko", "Ani", 2);
  addEdge("Hendra", "Ani", 2);
  addEdge("Hendra", "Eva", 1);
  addEdge("Hendra", "Cici", 1);
  addEdge("Hendra", "Gunawan", 1);
  addEdge("Hendra", "David", 2);
  addEdge("Cici", "Gunawan", 1);
  addEdge("David", "Gunawan", 2);
  addEdge("David", "Farhan", 1);
  calculateGraph();
  
  // Graph 3
  adj.clear();
  addEdge("Ani", "Joko", 2);
  addEdge("Ani", "Kate", 1);
  addEdge("Budi", "Joko", 1);
  addEdge("Budi", "Kate", 2);
  addEdge("Farhan", "Kate", 1);
  addEdge("Eva", "Kate", 2);
  addEdge("Gunawan", "Kate", 2);
  addEdge("David", "Kate", 1);
  addEdge("Gunawan", "Eva", 2);
  addEdge("Gunawan", "Lisa", 1);
  addEdge("David", "Lisa", 2);
  addEdge("Hendra", "Lisa", 2);
  addEdge("Hendra", "Cici", 1);
  calculateGraph();

  vector<pair<int,vector<int>>> ans;
  for (auto i : tot) {
    ans.push_back({i.se,i.fi});
  }
  
  sort(ans.begin(),ans.end(),cmp);
  for (auto i : ans) {
    for (int j : i.se) cout << j << " ";
    cout << "-> " << i.fi << '\n';
  }
  
  return 0;
}