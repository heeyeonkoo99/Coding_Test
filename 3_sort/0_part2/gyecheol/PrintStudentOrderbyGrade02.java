import java.util.Arrays;
import java.util.Scanner;

public class PrintStudentOrderbyGrade02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("학생수 입력:");
        int number = sc.nextInt();
        String[] students = new String[number];
        String[] temps = new String[number];
        sc.nextLine();
        for(int i=0;i<number;i++){
            System.out.println("학생이름과 성적 입력:");
            students[i] = sc.nextLine();
        }
        for(int i=0; i<number;i++){
            String front = students[i].split(" ")[0];
            String back = students[i].split(" ")[1];
            temps[i] = back+" "+front;
        }
        Arrays.sort(temps);
        for(int i=0;i<number;i++){
            System.out.println(students[i]);
        }
        for(int i=0;i<number;i++){
            System.out.print(temps[i].split(" ")[1]+" ");
        }

    }
}
