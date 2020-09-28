#include <bits/stdc++.h>

using namespace std;



int main()
{
    string arr[]={"Greater than 9","one","two","three","four","five","six","seven","eight","nine"};
    int n;
    
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if(n>9)
    {
        cout<<arr[0];
    }
    else{
        cout<<arr[n];
    }
    return 0;
}

