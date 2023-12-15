//  copyright 2023 hadleya
//  day2 lul
#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
using std::vector;
using std::string;
using std::atoi;

#ifndef _DAY2_H_
#define _DAY2_H_

namespace aoc2015 {
class Day2 {
 public:
  explicit Day2(vector<string> lines) { lines_ = lines; }
  void setLines(vector<string> lines) { lines_ = lines; }
  //  part 1
  int run1() {
    //  check if it's empty
    if (lines_.empty())
      return 0;
    //  alright, go crazy go stupid asf
    int result = 0;
    for (int i = 0; i < lines_.size(); ++i) {
      vector<string> dims = splitLine(lines_[i]);
      //  l,w,h
      //  convert them to ints
      int l = atoi(dims[0].c_str());
      int w = atoi(dims[1].c_str());
      int h = atoi(dims[2].c_str());
      result += ((2 * l * w) + (2 * w * h) + (2 * h * l));
      // now find the smallest sides
      vector<int> sorted = numSort(l, w, h);
      result += sorted[0] * sorted[1];
    }
    return result;
  }
  int run2() {
    int result = 0;
    for (int i = 0; i < lines_.size(); ++i) {
      //  first, find the present amount (2 smallest * 2)
      vector<string> dims = splitLine(lines_[i]);
      //  sort em
      int l = atoi(dims[0].c_str());
      int w = atoi(dims[1].c_str());
      int h = atoi(dims[2].c_str());
      vector<int> sorted = numSort(l, w, h);
      result += 2 * (sorted[0] + sorted[1]);
      //  now find the bow amount (l * w * h)
      result += (l * w * h);
    }
    return result;
  }

 private:
  vector<string> lines_;
  //  helper function to split string
  vector<string> splitLine(string s) {
    //  make a stream of strings
    std::stringstream ss(s);
    string token;                       //  used to add to the result
    vector<string> result;
    while (getline(ss, token, 'x')) {   //  grabs the item in the string and
                                        //  puts it in "token"
      result.push_back(token);          //  add to result
    }
    return result;
  }
  vector<int> numSort(int l = 0, int w = 0, int h = 0) {
    vector<int> result = {l, w, h};
    std::sort(result.begin(), result.end());
    return result;
  }
};
}  //  namespace aoc2015

#endif  //  _DAY2_H_
