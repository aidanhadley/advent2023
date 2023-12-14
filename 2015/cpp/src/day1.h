//  Copyright 2023 hadleya
//  solution for day 1
#include<iostream>
#include<fstream>
#include<vector>
#include <string>
using std::vector;
using std::string;
using std::cout;
using std::endl;

#ifndef _DAY1_H_
#define _DAY1_H_

namespace aoc2023 {
class Day1 {
 public:
  explicit Day1(vector<string> lines) { lines_ = lines; }
  void setLines(vector<string> lines) { lines_ = lines; }
  int run1() {
    //  runs a check to see if it's empty
    if (lines_.empty())
      return 0;
    //  otherwise, turn the vector into a single string
    string item = "";
    for (int i = 0; i < lines_.size(); ++i) {
      item += lines_[i];
    }
    //  just to check
    // cout << "String:" << item << endl;
    //  now it's time to count up
    int result = 0;
    for (int i = 0; i < item.size(); ++i) {
      if (item[i] == '(')
        result++;
      if (item[i] == ')')
        result--;
    }
    return result;
  }
  //  part 2
  int run2() {
    //  essentially run1, but now we see when result == -1
    if (lines_.empty())
      return 0;
    //  otherwise, turn the vector into a single string
    string item = "";
    for (int i = 0; i < lines_.size(); ++i) {
      item += lines_[i];
    }
    //  just to check
    // cout << "String:" << item << endl;
    //  now it's time to count up
    int result = 0;
    for (int i = 0; i < item.size(); ++i) {
      if (item[i] == '(')
        result++;
      if (item[i] == ')')
        result--;
      if (result == -1)
        return i + 1;
    }
    return 0;
  }
 private:
  vector<string> lines_;
  int result_;
};
}   //  namespace aoc2023
#endif  //  end _DAY1_H_
