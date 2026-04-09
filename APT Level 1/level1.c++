#include <iostream>
#include <string>

int main() {
    std::cout << "Welcome to eCitizen Login Validation System" << std::endl;

    std::string username = "adminKE";
    std::string password = "254Secure";

    std::string usernameInput, passwordInput;

    std::cout << "Enter your Username: ";
    std::getline(std::cin, usernameInput);

    std::cout << "Enter your password: ";
    std::getline(std::cin, passwordInput);

    if (usernameInput == username) {
        std::cout << "Access Granted" << std::endl;
    } else {
        std::cout << "Invalid Credentials" << std::endl;
    }

    return 0;
}