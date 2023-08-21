#include <iostream>
#include <set>
#include <map>
#include <string>

int main() {
    std::string myString = "aaannjitha";
    std::set<char> charSet;
    std::map<char, int> charCount;

    for (char c : myString) {
        charSet.insert(c);
    }

    for (char c : charSet) {
        int count = 0;
        for (char ch : myString) {
            if (c == ch) {
                count++;
            }
        }
        charCount[c] = count;
    }

    for (const auto& pair : charCount) {
        std::cout << pair.first << " Occurs " << pair.second << " times" << std::endl;
    }

    return 0;
}
