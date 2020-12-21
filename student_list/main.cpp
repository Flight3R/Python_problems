#include "classes.h"
#include <ctime>

using namespace std;


int main() {
  
  
  srand(time(NULL));
  
  List list;
  
  list.add("michal zie", rand()%299999 + 200000);
  list.add("marek cura", rand()%299999 + 200000);
  list.add("monika izr", rand()%299999 + 200000);
  list.add("agata kres", rand()%299999 + 200000);
  list.add("zenon affd", rand()%299999 + 200000);
  list.add("rafal gils", rand()%299999 + 200000);
  list.add("anteg gerf", rand()%299999 + 200000);
  list.add("marek aruy", rand()%299999 + 200000);
  list.add("michal lin", rand()%299999 + 200000);
  list.add("greg hfeai", rand()%299999 + 200000);
  
  cout << "1. Show list"      << endl
       << "2. Sort by indexNo"<< endl
       << "3. Sort by name"   << endl
       << "4. Add student"    << endl
       << "5. Remove b/n"     << endl
       << "6. Remove b/i"     << endl
       << "7. From file"      << endl
       << "8. To file"        << endl
       << "9. Clear"          << endl
       << "0. Exit"           << endl;

  while(true) {
    
    int choice;
    cin >> choice;
    
    switch(choice) {
      case 1: {
        list.show();
      } break;
      case 2: {
        if(list.sortI())
          cout << "done" << endl;
        else
          cout << "nothing to do" << endl;
      } break;
      case 3: {
        if(list.sortN())
          cout << "done" << endl;
        else
          cout << "nothing to do" << endl;
      } break;
      case 4: { 
        string name; 
        int number;
        cin.ignore();
        cout << "type name: "; getline(cin, name);
        cout << "type indexNo: "; cin >> number;
        list.add(name, number);
      } break;
      case 5: {
        string name;
        cin.ignore();
        cout << "type name to remove:"; getline(cin, name);
        if(list.remove(name)) 
          cout << name << " deleted" << endl;
        else 
          cout << "no such a student" << endl;
      } break;
      case 6: {
        int index;
        cout << "type indexNo to remove:"; cin >> index;
        if(list.remove(index)) 
          cout << index << " deleted" << endl;
        else 
          cout << "no such a student" << endl;
      } break;
      case 7: {
        if(list.fromfile())
          cout << "done" << endl;
        else
          cout << "file error" << endl;
      } break;
      case 8: {
        if(list.tofile())
          cout << "done" << endl;
        else
          cout << "file error" << endl;
      } break;
      case 9: {
        system("clear"); 
        cout << "1. Show list"      << endl
             << "2. Sort by indexNo"<< endl
             << "3. Sort by name"   << endl
             << "4. Add student"    << endl
             << "5. Remove b/n"     << endl
             << "6. Remove b/i"     << endl
             << "7. From file"      << endl
             << "8. To file"        << endl
             << "9. Clear"          << endl
             << "0. Exit"           << endl;
      } break;
      case 0: {
        return 0; 
      } break;
    }
  }


  return 0;
}
