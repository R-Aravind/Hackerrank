#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    string arr[]={"even","one","two","three","four","five","six","seven","eight","nine"};
    int a,b;
    cin >>a>>b;

    for(int i=a;i<=b;i++)
        {
            if(i<10)
            {
                cout<<arr[i]<<"\n";
            }
            else if(i%2==0)
            {
                cout<<arr[0]<<"\n";
            }
            else{
                cout<<"odd"<<"\n";
            }
        }


    return 0;
}
