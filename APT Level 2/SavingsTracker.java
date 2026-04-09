import java.util.Scanner;

public class SavingsTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your Member ID: ");
        int memId = scanner.nextInt();

        int totalSaving = 0;

        for (int i = 1; i <= 6; i++) {
            System.out.print("Enter month " + i + " contribution: ");
            int monthlyContribution = scanner.nextInt();
            totalSaving += monthlyContribution;
        }

        System.out.println("Hello, " + name + "\nMember ID: " + memId);
        System.out.println("Total Savings last 6 months: " + totalSaving + " KES");

        scanner.close();
    }
}