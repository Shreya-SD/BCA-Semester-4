#include<stdio.h>
int main()
{
  int l,b,a,p;
  printf("/n enter length and breadth:");
  scanf("%d%d",&l,&b);
  a=l*b;
  p=2*(l+b);
  printf("/n perimeter is:%d",p);
  printf("/n area is:%d",a);
  return 0;
}
