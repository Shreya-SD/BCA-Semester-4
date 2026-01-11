#include<stdio.h>
float area(float r);
int main()
{
  float a,r;
  printf("\n enter radius:");
  scanf("%f",&r);
  a=area(r);
  printf("\n area=%.2f",a);
  return 0;
}
float area(float r1)
{
  return(3.14*r1*r1);
}
