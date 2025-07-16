//Maria Angel Palacios 
//CS 280

#include <iostream>
using namespace std;

//main function
int main(){

    //declare a variable called name stores the 1st input from the user
    string name;
    cout << "Please enter your first name >>" << endl;
    cin >> name;
    

    //declare a variable called lastName to store the last name input 
    string lastName;
    cout << "Please enter your last name >>" << endl;
    cin >> lastName;
    
    
    //declare a variable named secNum to store the value of the Section Numbr input
    int secNum;
    cout << "Please enter your CS 280 section number >>" << endl;
    cin >> secNum;
    

    //print final sentence--> Welcome message 

    cout << "Welcome " << name << " to CS 280 section " << secNum << "." << endl; 
    
    //return int value of 0
    return 0;


}
