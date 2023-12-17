//  copyright 2023 hadleya
//  day 3 functions
#include<vector>
using std::vector;
#include<string>
using std::string;
//  debug
#include<iostream>
using std:: cout;
using std:: endl;
//  debug
namespace aoc2015 {
class Coords {
 public:
  explicit Coords(int x = 0, int y = 0) {
    x_ = x;
    y_ = y;
  }
  //  fuck it, do a good old fashioned java thing lol
  bool equals(Coords c) {
    if (c.x_ == x_ && c.y_ == y_)
      return true;
    return false;
  }
  //  debug
  void print() {
    cout << "coords (" << x_ << ", " << y_ << ")" << endl;
  }
  //  debug
 private:
  int x_;
  int y_;
};

class Day3 {
 public:
  explicit Day3(vector<string> lines) { lines_ = lines; }
  void setLines(vector<string> lines) { lines_ = lines; }
  //  part 1
  int run1() {
    string dirs = convert();
    vector<Coords> full = calculate(dirs);
    /* debug
    for (int i = 0; i < test.size(); ++i) {
      test[i].print();
    }
      debug
    */
    //  wildly inefficient code incoming
    vector<Coords> shrunk;
    for (int i = 0; i < full.size() ; ++i) {
      bool exists = false;
      for (int j = 0; j < shrunk.size(); ++j) {
        if (full[i].equals(shrunk[j]))
          exists = true;
      }
      if (!exists) {
        shrunk.push_back(full[i]);
      }
    }
    return shrunk.size();
  }
  int run2() {
    string totaldirs = convert();
    // split into 2 strings
    string dirs1 = "";
    string dirs2 = "";
    for (int i = 0; i < totaldirs.size(); ++i) {
      if (i % 2 == 0) {
        dirs1 += totaldirs[i];
      } else {
        dirs2 += totaldirs[i];
      }
    }
    vector<Coords> santa = calculate(dirs1);
    vector<Coords> robosanta = calculate(dirs2);
    vector<Coords> total = santa;
    total.insert(total.end(), robosanta.begin(), robosanta.end());
    vector<Coords> shrunk;
    for (int i = 0; i < total.size(); ++i) {
      bool exists = false;
      for (int j = 0; j < shrunk.size(); ++j) {
        if (total[i].equals(shrunk[j]))
          exists = true;
      }
      if (!exists) {
        shrunk.push_back(total[i]);
      }
    }
    return shrunk.size();
  }
  //  helper function because i think i know what part 2 is
  vector<Coords> calculate(string dirs) {
    //  set initial position
    int x = 0;
    int y = 0;
    vector<Coords> result;
    result.push_back(Coords(x, y));
    for (int i = 0; i < dirs.size(); ++i) {
      char in = dirs[i];
      switch (in) {
        case '^':
          y++;
          break;
        case 'v':
          y--;
          break;
        case '<':
          x--;
          break;
        case '>':
          x++;
          break;
      }
      Coords c(x, y);
      result.push_back(c);
    }
    return result;
  }
  //  my ass was WRONG
  //  helper function just to convert the lines into a string
  string convert() {
    string result = "";
    for (int i = 0; i < lines_.size(); ++i) {
      result += lines_[i];
    }
    return result;
  }

 private:
  vector<string> lines_;
};
}  //  namespace aoc2015

