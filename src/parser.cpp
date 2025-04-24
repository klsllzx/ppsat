#include "parser.hpp"
#include <fstream>
#include <iostream>
/******************************************************************************
 *  parser
 *****************************************************************************/

const regex Parser::re_literal = regex("-?[0-9]+");
const regex Parser::re_clause ("\\([^\\(\\)]+\\)");

int Parser::parse_literal(string text) {
    std::smatch sm;
    bool found = regex_match(text, sm, re_literal);
    if (!found) throw "No matching literal found in " + text;

    return stoi(sm[0].str());
}

vector<int> Parser::parse_literals(string text) {
    vector<int> res;

    std::smatch sm;
    while (regex_search(text, sm, Parser::re_literal)) {
        for (auto x : sm) {
            res.push_back(stoi(x.str()));
        }
        text = sm.suffix().str();
    }
    return res;
}

vector<string> Parser::parse_clauses(string text) {
    vector<string> res;

    std::smatch sm;
    while (regex_search(text, sm, Parser::re_clause)) {
        for (auto x : sm) {
            res.push_back(x.str());
        }
        text = sm.suffix().str();
    }
    return res;
}
vector<string> Parser::parse_DIMACS_file(const string& filename, int* nvar, int* ncls) {
    ifstream dimacsFile(filename);
    if (!dimacsFile.is_open()) {
        std::cerr << "Error: Could not open file " << filename << endl;
        return {};
    }

    vector<string> clauses;
    string line;
    bool headerParsed = false;

    while (getline(dimacsFile, line)) {
        if (!line.empty()) {
            if (!headerParsed && line[0] == 'p') {
                // Parse the header line (p cnf nvar cls)
                istringstream iss(line);
                string temp;
                iss >> temp >> temp >> *nvar >> *ncls; // Read "p cnf nvar cls"
                headerParsed = true;
            } else if (line[0] != 'c') { // Skip comment lines
                istringstream iss(line);
                vector<string> vars;
                string word;

                while (iss >> word) {
                    vars.push_back(word);
                }

                // Construct the clause string (excluding the last "0")
                string clause = "(";
                int length = vars.size();
                for (int i = 0; i < length - 1; i++) { // Skip the trailing "0"
                    clause += vars[i];
                    if (i < length - 2) {
                        clause += " "; // Add space between literals
                    }
                }
                clause += ")";
                clauses.push_back(clause); // Add the clause to the vector
            }
        }
    }

    dimacsFile.close();
    return clauses;
}
