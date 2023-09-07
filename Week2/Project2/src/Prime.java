import java.util.Scanner;

public class Prime {

    // This code take an integer as and intput parameter and returns whether or not it is a prime number.
    public static boolean isPrime(int n) {
        if (n <= 1) {return false;}
        if (n <= 3) {return true;}
        if (n % 2 == 0 || n % 3 == 0) {return false;}
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i +2) == 0) {return false;}
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number;
        while (true){
            System.out.println("Enter a positve number (0 or negative to exit)");
            number = input.nextInt();
            if (number <= 0) {
                break;
            }
            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number");
            }
        }
        input.close();
    }
}
