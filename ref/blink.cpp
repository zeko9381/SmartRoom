#include <wiringPi.h>
#include <iostream>
int main (void)
{
  wiringPiSetup () ;
  pinMode (8, OUTPUT) ;
  for (;;)
  {
    digitalWrite (8, HIGH) ; delay (500) ;
    digitalWrite (8,  LOW) ; delay (500) ;
  }
  return 0;
}
