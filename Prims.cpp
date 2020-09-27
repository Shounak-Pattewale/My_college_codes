#include<iostream>
using namespace std;

struct Edge {
 

    int wt;
	char u,v;
     
    };
int Cycle(Edge e,int*);    

int main()
{
int n,m,i,j,min;
cout<<"\nEnter the number of vertices:";
cin>>n;
cout<<"\nEnter the number of edges:";
cin>>m;
struct Edge e[25];
int path[25+1];
struct Edge temp;
 for (i=0; i<m; i++) 
 {
    cout << "\nEnter 2 vertices and weight of edge " << i+1 << endl;
    cout << "\nFirst vertex: ";
    cin >> e[i].u;
    cout << "Second vertex: ";
    cin >> e[i].v;
    cout << "\nWeight: ";
    cin >> e[i].wt;

    }
    /* for (i=0; i<=m-1; i++)          //for sorting
     {
 

    for (j=0; j<m-i-1; j++) 
    {

    if (e[j].wt > e[j+1].wt) 
    {
    t = e[j];
    e[j] = e[j+1];
    e[j+1] = t;
    }
    }
    }*/
	
    for (i=1; i<=n; i++) {

    path[i] = 0;

    }

    i = 0;

    j = 0;
 

    min = 0;

    cout << endl;

    while ((i!=n-1) && (j!=m)) {

    cout << "Edge ("

    << e[j].u << ", " << e[j].v << ") "

    << "with weight " << e[j].wt << " ";

    if (Cycle(e[j], path)) {

    min= min + e[j].wt;

    i++;

    cout << "is selected";

    } else {

    cout << "is discarded";

    }

    cout << endl;

    j++;

    }
    cout << "Minimum spanning tree is"<<min;

    if (i!=n-1) {

    cout << "Minimum spanning tree cannot be formed ";

    }



    return 0;

    }

    int Cycle (Edge e, int* path) {

    char u = e.u, v = e.v;

    while (path[u] > 0)

    u = path[u];

    while (path[v] > 0)

    v = path[v];

    if (u != v) {

    path[u] = v;

    return 1;

    }

    return 0;

    }

