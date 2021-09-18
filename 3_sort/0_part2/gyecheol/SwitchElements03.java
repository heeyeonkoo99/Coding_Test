import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class SwitchElements03 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.println("배열의 크기와 바꿔치기 횟수 입력:");
        String nk = sc.nextLine();
        int n = Integer.parseInt(nk.split(" ")[0]);
        int k = Integer.parseInt(nk.split(" ")[1]);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("a 배열입력:");
        String[] a = br.readLine().split(" ");
        System.out.println("b 배열입력:");
        String[] b = br.readLine().split(" ");

        Arrays.sort(a);
        Arrays.sort(b);

        for(int i=0; i<k; i++){
            String temp = a[i];
            a[i] = b[n-i-1];
            b[n-i-1]=temp;
        }

        int sum =0;
        int[] intA = Arrays.stream(a).mapToInt(Integer::parseInt).toArray();
        sum =Arrays.stream(intA).sum();

        System.out.println();
        System.out.println("합계: "+sum);
    }
}
