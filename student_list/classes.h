#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

class Student {
private:
  string name;
  int indexnumber;
public:
  Student *next = NULL; 
  Student *prev = NULL;
  
  Student(string, int);
  
  string getN();
  
  int getI();
  
  void show();
  
  void swap();
};

class List { 
public:
  Student *first = NULL;
  
  void add(string, int);
  
  bool remove(int);
  
  bool remove(string);
  
  int counter();
  
  bool sortI();
  
  bool sortN();
  
  bool show();
  
  bool fromfile();
  
  bool tofile();
};

bool compare(string, string, int);
