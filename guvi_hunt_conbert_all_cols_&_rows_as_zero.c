#include <stdio.h>

int main()
{
    int N;
    scanf("%d",&N);
    int arr[N][N],brr[N][N];
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
                scanf("%d",&arr[i][j]);
                
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
                brr[i][j] = 1;
                
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(arr[i][j] == 0)
            {
                for(int k=0;k<N;k++)
                    brr[i][k] = 0;
                for(int k=0;k<N;k++)
                    brr[k][j] = 0;
                        
            }
        }
    }
    
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
                printf("%d ",brr[i][j]);
        }
        printf("\n");
    }
                
    return 0;
}
