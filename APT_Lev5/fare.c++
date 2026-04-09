#include <iostream>
using namespace std;

const int BASE_FARE = 200;
const int COST_PER_KM = 50;

int compute_fare(int distance_km) {
    return BASE_FARE + (COST_PER_KM * distance_km);
}

int main() {
    int distance;
    cout << "Enter distance (km): ";
    cin >> distance;
    cout << "Total fare: KES " << compute_fare(distance) << endl;
    return 0;
}