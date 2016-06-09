#include <stdio.h>

int main()
{
    int num;
    scanf("%d",&num);
    
    int arr[num];
    
    for(int i=0;i<num;i++)
    scanf("%d",&arr[i]);
    
    printf("The respective elements are:\n\n");
    for(int i=0;i<num;i++)
        for(int j=0;j<num;j++)
            for(int k=0;k<num;k++)
                if(arr[i] + arr[j] == arr[k])
                    {
                        printf("%d  %d  %d\n",arr[i],arr[j],arr[k]);
                        break;
                    }
    return 0;
}
