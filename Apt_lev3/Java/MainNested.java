import java.util.Scanner;

public class MainNested {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Welcome to rainfall advisory! ");
        System.out.print("Enter the rainfall amount in mm: ");
        int rainfall = scanner.nextInt();

        System.out.print("Enter temperature in degree Celsius(°C): ");
        int temperature = scanner.nextInt();

        if (rainfall < 200) {
            System.out.println("Irrigation Required");
        } else {
            if (temperature > 30) {
                System.out.println("Monitor Soil");
            } else {
                System.out.println("Normal Conditions");
            }
        }

        scanner.close();
    }
}