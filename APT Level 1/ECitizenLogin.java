import java.util.Scanner;

public class ECitizenLogin {
    public static void main(String[] args) {
        System.out.println("Welcome to eCitizen Login Validation System");

        String username = "adminKE";
        String password = "254Secure";

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your Username: ");
        String usernameInput = scanner.nextLine();

        System.out.print("Enter your password: ");
        String passwordInput = scanner.nextLine();

        if (usernameInput.equals(username)) {
            System.out.println("Access Granted");
        } else {
            System.out.println("Invalid Credentials");
        }

        scanner.close();
    }
}