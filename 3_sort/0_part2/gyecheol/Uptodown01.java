import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Uptodown01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("수열의 개수 입력:");
        int len = sc.nextInt();
        Integer[] numbers = new Integer[len];
        for(int i =0; i<len; i++){
            System.out.println("숫자 입력:");
            numbers[i] = sc.nextInt();
        }
        Arrays.sort(numbers, Collections.reverseOrder());
        for(int i=0; i<len; i++){
            System.out.println(numbers[i]);
        }

    }
}
