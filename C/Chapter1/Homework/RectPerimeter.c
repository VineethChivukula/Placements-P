#include<stdio.h>
//Perimeter of a Rectangle
int main(){
    float length,breadth;
    printf("Enter length:");
    scanf("%f",&length);
    printf("Enter breadth:");
    scanf("%f",&breadth);    
    printf("Perimeter is:%f",2*(length+breadth));
    return 0;
}