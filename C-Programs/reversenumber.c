#include<stdio.h>
int main()
{
  int n,rev=0,rem;
  printf("\n enter the no: ");
  scanf("%d",&n);
  while(n!=0)
    {
      rem=n%10;
      rev=rev*10+rem;
      n=n/10;
    }
  printf("\n reversed no:%d",rev);
  return 0;
}
