package binary_search;

import java.util.Scanner;

public class MakingTteok02 {

    public static void main(String[] args) {
        //String[] resultArr;
        Scanner sc = new Scanner(System.in);
        System.out.println("떡의 개수:");
        int cakeNumber = sc.nextInt();
        System.out.println("요청한 떡의 개수:");
        int wantingCakeNumber = sc.nextInt();
        int[] cakeLength = new int[cakeNumber];
        System.out.println("떡 길이 입력:");
        for (int i = 0; i < cakeNumber; i++) {
            cakeLength[i] = sc.nextInt();
        }

        int start= 0;
        int end = (int)1e9;

        int result = 0;
        while(start<=end){
            long total = 0;
            int mid = (start+end)/2;
            for(int i=0;i<cakeNumber;i++){
                if(cakeLength[i]>mid){
                    total = total + cakeLength[i] -mid;
                }
                if(total < wantingCakeNumber){
                    end = mid -1;
                }
                else{
                    result = mid;
                    start = mid + 1;
                }
            }
        }
        System.out.println(result);
    }

}



