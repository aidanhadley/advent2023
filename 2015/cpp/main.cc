//  Copyright 2023 hadleya
//  main file to test all days
#include"src/include.h"
#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using std::cout;
using std::endl;
using std::vector;
using std::string;
using namespace aoc2015;

//  decalre prototype
vector<string> turnFileToString(string fileName);

int main() {
  //  ! modify
  int day = 3;
  //  ! modify
  //  runs example
  string file = "day" + std::to_string(day) + "e.txt";
  cout << "Running Day " << day << " Example:" << endl;
  vector<string> lines = turnFileToString(file);
  //  ! modify
  Day3 d(lines);
  //  ! modify
  cout << "Part 1:" << d.run1() << endl;
  cout << "Part 2:" << d.run2() << endl;
  string file1 = "day" + std::to_string(day) + ".txt";
  //  real
  cout << "Running Day " << day << " Real:" << endl;
  vector<string> lines1 = turnFileToString(file1);
  d.setLines(lines1);
  cout << "Part 1:" << d.run1() << endl;
  cout << "Part 2:" << d.run2() << endl;
}

//  this turns a file in the "input" section into a vector of string
vector<string> turnFileToString(string fileName) {
  string fullPath = "input/" + fileName;
  std::ifstream inputFile(fullPath);
  vector<string> result;
  if (!inputFile.is_open()) {
    std::cerr << "Error opening file" << endl;
    return result;
  }
  string line;

  while (std::getline(inputFile, line)) {
    result.push_back(line);
  }
  inputFile.close();

  return result;
}
