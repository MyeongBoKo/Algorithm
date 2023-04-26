import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 테스트 케이스 개수
        int T = sc.nextInt();

        for (int i = 0;i < T;i++){
            int n = sc.nextInt();

            // DP값, arr 값
            int[][] DP = new int[2][n+1];
            int[][] arr = new int[2][n+1];

            for (int j = 0;j<2;j++){
                for (int k = 1;k<=n;k++){
                    arr[j][k] = sc.nextInt();
                }
            }

            DP[0][1] = arr[0][1];
            DP[1][1] = arr[1][1];

            for (int l = 2;l<=n;l++){
                DP[0][l] = Math.max(DP[1][l-1], DP[1][l-2])+arr[0][l];
                DP[1][l] = Math.max(DP[0][l-1], DP[0][l-2])+arr[1][l];
            }
            System.out.println(Math.max(DP[0][n], DP[1][n]));
        }
    }
}

/*
한 칸 대각선만 해당하는 것이 아니고 두 칸 대각선도 생각해야 한다.
세 칸 대각선 혹은 세 칸 옆은 문제의 최대값을 구해야 한다는 조건을 만족 시키지 못하기 때문에 고려하지 않아도 된다.
 */
