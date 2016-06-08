#include <stdio.h>

int main()
{
    int num,k=1;
    int arr[1000] = {0,};
    arr[0] = 3;
    arr[1] = 4;
    for(int i=0;i<100;i++)
    {
        arr[++k] = (arr[i]*10) + 3;
        arr[++k] = (arr[i]*10) + 4;
    }
    scanf("%d",&num);
    printf("%d",arr[num-1]);
    return 0;
}
