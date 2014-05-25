#include <iostream>
#include "Linklist_Vector_temp.h"

using std::cout;
using std::endl;

int main( )
{
    int a = 5;
     Vector<int> my_vector;
    my_vector.push_back( 5 );
    cout<<my_vector.back( )<<endl;
    return 0;
}
