#include <iostream>

using namespace std;

int main()
{
    int quotient=0;
    int dividend = 100;
    int divisor = 10;
    while(dividend>=divisor)
    {
        dividend -=divisor;
        quotient++;
    }
    cout<<"Quotient = "<<quotient<<"\nRemainder = "<<dividend<<endl;
    return 0;
}
