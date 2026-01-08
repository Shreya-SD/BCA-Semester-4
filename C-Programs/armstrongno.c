#include<stdio.h>
int main()
{
  int n,c,d,s=0,num;
  printf("\n enter a three digit no:");
  scanf("%d",&n);
  num=n;
  do
    {
      d=n%10;
      c=d*d*d;
      s=s+c;
      n=n/10;
    }
    while(n!=0);
  if(s==num)
  {
    printf("\n %d is an armstrong no",num);
  }
  else
  {
    printf("\n %d is not an armstrong no",num);
  }
  return 0;
}
