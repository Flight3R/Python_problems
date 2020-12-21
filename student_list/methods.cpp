#include "classes.h"

using namespace std;

  Student::Student(string name, int indexnumber) {
    this->name = name;
    this->indexnumber = indexnumber;
  }
  
  string Student::getN() {
    return name;
  }
  
  int Student::getI() {
    return indexnumber;
  }

  
  void Student::show() {
    cout << "Name: " << name << "\tIndexNo: " << indexnumber << endl;
  }
  
  void Student::swap() {
    Student *tmp = next->next;
    prev->next = next;
    next->prev = prev;
    next->next = this;
    prev = next;
    next = tmp;
    tmp->prev = this;
  }

  void List::add(string name, int indexnumber) {
    Student *added = new Student(name, indexnumber);
    
    if (first == NULL) {
      added->next = added;
      added->prev = added;
      first = added;
    } 
    else {
      Student *tmp = first;
      while (tmp->next != first) {
        tmp = tmp->next;
      }
      first->prev = added;
      added->next = first;
      tmp->next = added;
      added->prev = tmp;
    }
  }
  
  bool List::remove(int indexnumber) {
    Student *pnt = first;
    
    while(pnt->getI() != indexnumber) {
      pnt = pnt->next;
      if (pnt == first) {
        return false;
      }
    }
    
    pnt->next->prev = pnt->prev;
    pnt->prev->next = pnt->next;
    
    delete pnt;
    return true;
  }
  
  bool List::remove(string name) {
    Student *pnt = first;
    
    while(pnt->getN() != name) {
      pnt = pnt->next;
      if (pnt == first) {
        return false;
      }
    }
    pnt->next->prev = pnt->prev;
    pnt->prev->next = pnt->next;
    
    delete pnt;
    return true;
  }

  
  int List::counter() {
    if (first == NULL) return 0;
      else if (first->next == first) return 1;
      else {
    
      int count = 2;
      Student *pnt = first->next;
      while (pnt->next != first) {
        pnt = pnt->next;
        count++;
      }
      return count;
    }
    
  }
  
  bool List::sortI() {
    int count = counter();
    
    if (count == 0 || count == 1) return false;
    
    Student *pnt = first;
    int min = 999999;
    for (int i=0;i<count;i++) {
      if (pnt->getI() < min) {
        min = pnt->getI();
        first = pnt;
      }
      pnt = pnt->next;
    }
    
//-----compare and swap------
    pnt = first;
    for (int i=0; i<count-1; i++) { 
      pnt = first;
      for (int j=0; j<count-1-i; j++) {
        if (pnt->getI() > pnt->next->getI()) {
          pnt->swap();
        }
        else pnt = pnt->next;
      }
    }   
    return true;
  }
  
  bool List::sortN() {
    int count = counter();
    
    if (count == 0 || count == 1) return false;
    
    Student *pnt = first;
    string min = "zz";
    for (int i=0;i<count;i++) {
      if (compare(min, pnt->getN(), 0)) {
        min = pnt->getN();
        first = pnt;
      }
      pnt = pnt->next;
    }
    
//-----compare and swap------
    pnt = first;
    for (int i=0; i<count-1; i++) { 
      pnt = first;
      for (int j=0; j<count-1-i; j++) {
        if (compare(pnt->getN(), pnt->next->getN(), 0)) {
          pnt->swap();
        }
        else pnt = pnt->next;
      }
    }   
    return true;
  }
  
  bool List::show() {
    if (first == NULL) return 0;
    
    Student *pnt = first;
    
    do {
      pnt->show();
      pnt = pnt->next;
    } while (pnt != first);
    
    return 1;
  }
  
  bool List::fromfile() {
    
    string line, name, vorname, number;
    int index;
    fstream file("source.txt",ios::in);
    
    if(!file.is_open()) {
      return false;
    }
    
    while (getline(file, line)) {

      std::istringstream iss(line);
      iss >> name >> vorname >> number;
      index = atoi(number.c_str());
      
      add(name + " " + vorname, index);
      cout << "NAME: " << name + " " + vorname << "\tINDEX: " << index << " added"<<endl;
      
    }
    
    file.close();
    return true;
  }
  
  bool List::tofile() {
    fstream file ("dest.txt", ios::out);
    
    if(!file.is_open()) {
      return false;
    }
    
    Student *pnt = first;
    
    do {
      file << pnt->getN() << "\t" << pnt->getI() << endl;
      pnt = pnt->next;
    } while (pnt->next != first);
    
    file.close();
    return true;
  }
     
  bool compare(string a, string b, int i) {
    if ((int)a[i] > (int)b[i]) {
      return true;
    } 
    else if ((int)a[i] < (int)b[i]) {
      return false;
    }
    else return compare(a, b, i+1);
  }
