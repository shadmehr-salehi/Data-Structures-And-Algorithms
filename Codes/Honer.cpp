// Honer Algorhitm implementation
#include <bits/stdc++.h>
using namespace std;
// ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
int main()
{

    // 2 X^3 + 3 X^2 -4X + 1 = 1185
    
    int CoArr[1000] ; 
    int n;
    cout<<"Number of Coeffisents ? \n" ; 
    cin>>n;
    cout<<"please enter your Coeffisents \n";
    int Sum = 0 ;
    for (int i = 0; i < n ; i++)
    {
        cin>>CoArr[i];
    }
    cout<<"please enter X \n" ; 
    int x ; 
    cin>>x ; 
    Sum = CoArr[0]; 
    for (int i = 1 ; i < n ; i++)
    {
        Sum = x*Sum + CoArr[i] ; 
    }
    cout<<Sum ; 


    return 0 ;    
}
