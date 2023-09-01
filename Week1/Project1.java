import java.util.Scanner;

public class Project1 {
    // Java program to find the factorial of a number provided by the user.
    public static void fact() {
        System.out.println("Enter a Positive Integer:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        while (n < 0) {
            System.out.println("Sorry, only postivie numbers, enter again: ");
            n = scanner.nextInt();
        }
        if (n == 0) {
            System.out.println("The factorial of 0 is 1");
        } else {
            int f = 1;
            for (int i = 1; i <= n; i++)
                f *= i;
            System.out.println("The factorial of " + n + " is " + f);
        }
    }

    // main() function calls the fact() function.
    public static void main(String[] args) {
        fact();
    }

}