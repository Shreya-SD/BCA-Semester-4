#include<stdio.h>
int main()
{
  int n,i,fact=1;
  printf("/n enter the number:");
  scanf("%d",&n);
  if(n<0)
  {
    printf("/n error");
  }
  else
  {
    for(i=1;i<=n;i++)
      {
        fact=fact*i;
      }
    printf("/n factorial of %d=%d",n,fact);
  }
  return 0;
}
