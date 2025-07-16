#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string fileName;
    ifstream inputFile;



   

    // Prompt user for file name
    cout << "Enter the name of the file to read from:" << endl;
    cin >> fileName;


    // Open the file
    inputFile.open(fileName);

    if (!inputFile.is_open()) {
        cout << "File cannot be opened " << fileName << endl;
    }

    int lineCount = 0;
    int commentCount = 0;
    int paragraphCount = 0;
    int wordCount = 0;
    int boldCount = 0;
    int italicCount = 0;
    int underlineCount = 0;

    string line;
    bool inParagraph = false;

    while (getline(inputFile, line)) {
        lineCount++;

        // Skip empty lines or comment lines
        if (line=="" || line[0] == '#') {
            commentCount++;
            continue;
        }

        if (line[0] == '%') {
            // Command line
            string command = line.substr(1); // Remove %
            if (command == "begin") {
                if (inParagraph) {
                    cout << "Error %begin command"<<endl;
                }
                inParagraph = true;
            } else if (command == "end") {
                if (inParagraph) {
                    inParagraph = false;
                    paragraphCount++;
                } else {
                    cout << "Error %end command at line " << endl;
                }
            } else if (command == "bold") {
                boldCount++;
            } else if (command == "italic") {
                italicCount++;
            } else if (command == "underline") {
                underlineCount++;
            } else {
                cout << "Incorrect command name at line: " << lineCount << endl;
            }
        } else {
            // Linea de texto
            bool inWord = false;
            for (char c : line) {
                if (isspace(c)) {
                    if (inWord) {
                        wordCount++;
                        inWord = false;
                    }
                } else {
                    inWord = true;
                }
            }
            if (inWord) {
                wordCount++;
            }
        }
    }

    
    cout << "Total lines: " << lineCount << endl;
    cout << "Commented lines: " << commentCount << endl;
    cout << "Number of paragraphs: " << paragraphCount << endl;
    cout << "Total number of words: " << wordCount << endl;
    cout << "Bold commands: " << boldCount << endl;
    cout << "Italic commands: " << italicCount << endl;
    cout << "Underline commands: " << underlineCount << endl;

    inputFile.close();
    */
    return 0;
}
