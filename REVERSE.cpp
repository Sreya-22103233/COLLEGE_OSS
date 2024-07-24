#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    string input;
    string output="";
    cout<<"Enter string: ";
    cin>>input;
    for(int i=input.size()-1;i>=0;i--)
    {
        output+=input[i];
    }

    cout<<"Reversed String: "<<output;
    return 0;
}
