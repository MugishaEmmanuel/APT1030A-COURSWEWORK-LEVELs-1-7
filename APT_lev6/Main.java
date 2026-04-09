public class Main {
    public static void checkAccess(String role) throws Exception {
        if (!role.equals("Doctor")) {
            throw new Exception("Access Denied: Only doctors can access patient records.");
        }
        System.out.println("Access Granted");
    }

    public static void main(String[] args) {
        try {
            checkAccess("Nurse");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}