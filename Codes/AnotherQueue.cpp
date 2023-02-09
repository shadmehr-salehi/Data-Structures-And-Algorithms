/* implement a queue struct with these functions 
  getmin(): find the minimum integer in the queue with O(1)
 reverse(): reverse the order of integers in the queue with O(n)
*/ 
#include <bits/stdc++.h>
using namespace std;
// ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
// oredr push & pop = O(n)

class TestQueue 
{
public:


void push(int n)
{
    q.push(n) ;
    calcmin() ;
}
void pop()
{
    q.pop() ;
    calcmin();
}

int calcmin()
{
    int temp = q.front(); 
    queue<int> q2 ; 
    while (q.size() !=0)
    {
        q2.push(q.front()) ; 
        temp = min(temp , q.front()) ; 
        q.pop() ; 
    }

    mn = temp ;
    while (q2.size() !=0)
    {
        q.push(q2.front()) ; 
        q2.pop() ; 
    } 
}
int getmin()
{
    return mn ;
}
void reverse()
{
    stack<int> temp ; 
    while(q.size() != 0)
    {
        temp.push(q.front()) ;
        q.pop() ; 
    }
    while(temp.size() != 0)
    {
        q.push(temp.top());
        temp.pop() ;
    }

}
private:
    queue<int> q ; 
    int mn ;

};




int main()
{
    TestQueue q ; 
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);
    q.push(6);
    cout<<q.getmin() ; 
     


    return 0 ;    
}
