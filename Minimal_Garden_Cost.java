import java.util.Scanner;

public class Minimal_Garden_Cost {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            long n = sc.nextLong();
            if(n==1){
                System.out.println(0);
                continue;
            }
            long curr = (long)Math.sqrt(n);
            while(n<curr*curr){
                curr+=1;
            }
            System.out.println(curr);
        }
    }
}