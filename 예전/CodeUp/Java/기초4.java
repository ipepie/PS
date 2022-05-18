기초 4-1 단순 반복문 ~ 4-2 중첩 반복문
//1071 ~ 1077 반복실행구조
// 1071
import java.util.Scanner;
public class Main {
	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		while(true) {
			int a = s.nextInt();
			if(a != 0) {
				System.out.println(a);
			}else {
				break;
			}
		}
	}
}
//1072
    Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		for(int i = 0; i<n; i++) {
			int a = s.nextInt();
			System.out.println(a);
		}
		s.close();
//1074
    Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		while(n!=0) {  // = for(int i=a;i>0;i--)
			System.out.println(n);
			n--;
		}
//1075
    Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		while(n!=0) {
			n--;
			System.out.println(n);

		}
//1076 와 이거 어케 풀긴 풀었는데 쉽게 푸는 방법이 있을거같은데. 배운거가지고는 이렇게밖에 못풀겠다
    Scanner s = new Scanner(System.in);
		char n = s.next().charAt(0);
		char[] arr = new char[n-'a'+1];
		for(int i = n-'a'; i>=0;i--) {
			arr[i] = n;
			n--;
		}
		for(int j = 0; j<arr.length;j++) {
			System.out.print(arr[j]+" ");
		}
char ch = s.nextLine().charAt(0);
char first = 'a';
do {
  System.out.print(first +" ");
  first++
} while(first <= ch);
이거처럼 처음 'a'부터 시작해서 같아지면 종료하는게 훨씬 쉽네
   Scanner s = new Scanner(System.in);
   char a = s.next().charAt(0);
   int b = (int)a;

   for(int i=97;i<=b;i++){
       System.out.print((char)i+" ");
   }
마찬가지로 a가 97이니까 입력이랑 같아질때까지 돌리기.

//1077
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		for(int i = 0;i<=a;i++) {
			System.out.println(i);
    }
//1078 ~ 1092 기초-종합
//1078
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int sum = 0;
		for(int i = 0;i<=a;i++) {
			if(i%2==0) {
				sum += i;
			}
		}
		System.out.println(sum);
//1079
    Scanner s = new Scanner(System.in);
		while(true) {
			char a = s.next().charAt(0);
			System.out.println(a);
			if(a =='q') {
				break;
			}
		}
//1080
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int sum = 0, i = 0;
		while(sum<a) {
			i++;
			sum += i;
		}
		System.out.print(i);

//for문하다가 두번째 조건 애매해서 break써도되나 고민하다 안했는데
    for(int i=1,sum=0; ; i++) {
			sum+=i;
			if(sum>=n) {
				System.out.println(i);
				break;
			}
		}
이렇게도 가능
//여기부턴 띄엄띄엄있네 문제번호가
//1083
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		for(int i=1;i<=a;i++) {
			if(i%3 == 0) {
				System.out.print("X ");
			} else {
				System.out.print(i+" ");
			}
		}
//1087
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int sum = 0;
		for(int i=1;;i++) {
			sum += i;
			if(sum >= a) {
				System.out.print(sum);
				break;
			}
		}
//1088
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		for(int i=1;i<=a;i++) {
			if(i % 3 == 0) {
				System.out.print("");
			} else {
				System.out.print(i + " ");
			}
		}
continue써서 넘기는방법
    for(int i=1; i<=n; i++) {
			if(i%3==0) continue;
			System.out.print(i);
			if(i!=n) System.out.print(" ");
		}


//1089
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int d = s.nextInt();
		int n = s.nextInt();
		System.out.print(a+(n-1)*d);
//1090
    int a = s.nextInt();
		int r = s.nextInt();
		int n = s.nextInt();
		int ans = a;
		for(int i = 1;i<n;i++) {
			ans *= r;
		}
		System.out.print(ans);
문제 그지같네 이거. 숫자 커지면 타입때문에 틀리는거 같은데
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int r = s.nextInt();
		int n = s.nextInt();
		long ans = (long)Math.pow(r,n-1);
		System.out.print(a*ans);
이렇게 하니까 됨. pow는 기본 타입이 double라 신경써줘야하는듯
//1091
    Scanner s = new Scanner(System.in);
		long a = s.nextLong();
		int m = s.nextInt();
		int d = s.nextInt();
		int n = s.nextInt();
		for(int i = 1; i<n;i++) {
			 a = a*m+d;
		}
		System.out.println(a);
//1092
    Scanner s = new Scanner(System.in);
		long a = s.nextLong();
		int b = s.nextInt();
		int c = s.nextInt();
		int day = 1;
		while(day%a!=0||day%b!=0||day%c!=0) {
			day++;
		}
		System.out.println(day);

//4-2 중첩반복문
//1081
    Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int m = s.nextInt();
		for(int i = 1;i<=n;i++) {
			for(int j = 1;j<=m;j++) {
				System.out.println(i+" "+j);
			}
		}
//1082
    Scanner s = new Scanner(System.in);
		int n = s.nextInt(16);
		for(int i = 1;i<16;i++) {
			System.out.printf("%X*%X=%X %n",n,i,n*i);
		}
//1084
    Scanner s = new Scanner(System.in);
		int r = s.nextInt();
		int g = s.nextInt();
		int b = s.nextInt();
		for(int i = 0;i<r;i++) {
			for(int j=0;j<g;j++) {
				for(int k=0;k<b;k++) {
					System.out.printf("%d %d %d %n",i,j,k);
				}
			}
		}
		System.out.println(r*g*b);
맞는데 삼중포문에 print가 시간이 오래걸린답니다.
파이썬에서 sys.stdin.readline() 쓰는거랑 비슷한듯.
그래서 버퍼 리더와 라이터 사용해야한다는데 안배웠는데 일단보면
import해야하는게 많다

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;
public class Test{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt();
		int g = sc.nextInt();
		int b = sc.nextInt();
		int count =0;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for(int i=0; i<r; i++){
			for(int j=0; j<g; j++){
				for(int k=0; k<b; k++){
					count++;
					bw.write(i+" "+j+" "+k+"\n");

				}
			}
		}
		bw.write(String.valueOf(count));
		bw.flush();
		bw.close();
	}
}
아직 어떻게 쓰는지 모르는 아이지만 문제해결 시간비교해보면
위에가 4000 아래가 375로 처리속도가 월등히 빠르다.    
