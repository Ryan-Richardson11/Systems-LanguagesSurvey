import java.util.Scanner;

public class Main {

    public static void fact() {
        System.out.println("Enter a Positive Integer:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println("It's developer tea time!");
        while (n > 0) {
            System.out.println("Sorry, only postivie numbers, enter again: ");
            n = scanner.nextint();
        }
        if (n == 0) {
            System.out.println("The factorial of 0 is 1");
        } else {
            int f = 1;
            for (int i = 1; i <= n; i++)
                f *= i;
            System.out.println("The factorial of" + n + "is" + f);
        }
    }

    public static void main(String[] args) {
        fact();
    }

}