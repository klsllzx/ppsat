//
// Created by Ning Luo on 5/18/21.
//

#include <math.h>
#include "formula.hpp"
#include <memory>
#include <chrono>
#include <exception>
#include <stdlib.h>
#include <ctime>
#include "clause.hpp"
#include "literal.hpp"
#include "model.hpp"
#include "utils.hpp"
#include "solver.hpp"
using namespace std;
using namespace emp;



int main(int argc, char** argv) {

    try {

        int port, party;
        //cout<<"finish" << endl;

        parse_party_and_port(argv, &party, &port);
        NetIO *io = new NetIO(party == ALICE ? nullptr : "127.0.0.1", port);
        setup_semi_honest(io, party);

        int number_of_steps = atoi(argv[3]);
        int nvar, ncls; // PUBLIC
        string design_filename = argv[4];
        auto phi = make_unique<Formula>(design_filename, &nvar, &ncls, PUBLIC);
        cout << "input formula: \n";
        phi->print(true);
        Solver solver(nvar, phi);
        auto start = chrono::steady_clock::now();
        auto model = solver.solve(number_of_steps, true);
        auto end = chrono::steady_clock::now();
        auto time_span = static_cast<chrono::duration<double>>(end - start);
        cout << "solve time: "<< time_span.count() <<" seconds\n";
        cout << "model\n"; 
        cout << model->toString() << endl;
        delete io;
    }

    catch (char const *msg) {
        cout << "Main catch msg: " << msg << endl;
    }
    catch (const exception &e) {
        cout << "Main cat exception: " << e.what() << endl;
    }


}

