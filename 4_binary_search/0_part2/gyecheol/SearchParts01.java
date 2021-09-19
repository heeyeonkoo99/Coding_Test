package binary_search;
import java.util.Scanner;

public class SearchParts01 {
    public static int binarySearch(int target, int arr[]){
        int mid;
        int left=0;
        int right = arr.length -1;

        while(right>=left){
            mid = (right+left)/2;

            if(target==arr[mid]){
                return mid; //찾을 경우 0리턴
            }
            else if(target < arr[mid]){
                right = mid -1;
            }
            else{
                left = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] resultArr;
        Scanner sc = new Scanner(System.in);
        System.out.println("전체 부품개수:");
        int havingPartsNumber = sc.nextInt();
        System.out.println("전체 부품입력:");
        int[] havingParts = new int[havingPartsNumber];
        for(int i=0;i<havingPartsNumber;i++){
            havingParts[i] = sc.nextInt();
        }
        System.out.println("찾는 부품개수:");
        int findingPartsNumber = sc.nextInt();
        resultArr = new String[findingPartsNumber];
        System.out.println("찾는 부품입력:");
        int[] findingParts = new int[findingPartsNumber];
        for(int i=0;i<findingPartsNumber;i++){
            findingParts[i]= sc.nextInt();
        }

        for(int i=0;i<findingPartsNumber;i++)
        {
            int result = binarySearch(i,havingParts);
            if(result==-1){
                resultArr[i] = "no";
            }
            else{
                resultArr[i]= "yes";
            }
        }
        for(int i=0;i<findingPartsNumber;i++){
            System.out.println(resultArr[i]);
        }
    }
}
