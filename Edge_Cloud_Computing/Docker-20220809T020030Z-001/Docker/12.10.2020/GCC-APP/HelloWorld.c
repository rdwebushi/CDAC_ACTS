#include <stdio.h>
#include <unistd.h>  //Header file for sleep function
void displayMessage()
{
    printf("C Program Running inside a container\n");
}
int main()
{
    for(int i=0; i<100; i++)
    {
        displayMessage();
        sleep(1);
    }
    return 0;
}
