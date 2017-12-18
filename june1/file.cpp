#include <iostream>

using namespace std;

extern "C"
void hello(){
cout << "Hello World" << endl;

}
extern "C"
int add (int x, int y){
return x + y;
}