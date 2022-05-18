기초2. 입출력문 및 연산자

//1010 정수입력받기
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int num = scan.nextInt();
      System.out.print(num);
	}
}
//String input = scanner.nextLine(); // 입력받은 내용을 input에 저장
//int num = Integer.parseInt(input); // 입력받은 내용을 int타입의 값으로 변환


//1011 문자 입력받기
import java.util.Scanner;

public class Main{
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        char a = s.next().charAt(0);
        System.out.print(a);
    }
}
// next() : 첫번째 공백 전까지의 문자열을 입력받음


//1012 실수 입력받기
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        float a = s.nextFloat();
        System.out.printf("%f",a);
	}
}


//1013
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        System.out.printf("%d %d",a,b);
	}
}

//1014
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        char a = s.next().charAt(0);
        char b = s.next().charAt(0);
        System.out.printf("%c %c",b,a);
	}
}

//1015
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        float a = s.nextFloat();
        System.out.printf("%.2f",a);
	}
}

//1017
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        System.out.printf("%d %d %d",a,a,a);
	}
}

//1018
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        System.out.print(a);
	}
}

//1019
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
      Scanner s = new Scanner(System.in);
      String a = s.nextLine();
      String arr[] = a.split("\\.");
      int year = Integer.valueOf(arr[0]);
      int month = Integer.valueOf(arr[1]);
      int day = Integer.valueOf(arr[2]);
      System.out.printf("%04d.%02d.%02d",year,month,day);
	}
}
// valueOf를 통해 배열 인덱스의 값을 정수로 변환해서 각각 정수형 인트에 할당
// 근데 스플릿 항목이 많아서 배열이 길어지면 새로운 배열을 생성해야할듯
//int[] arr2 = new int[arr.length]; 그다음 for문으로 arr2배열 안에
//for (int i = 0; i<arr.length;i++) {
//    arr2[i] = Integer.parseInt(arr[i]);
//}
개선된 for문의 형식 - 이렇게 배열 간단하게 print가능
문자열 타입의 배열에 사용
for (String a: arr) {
  System.out.println(a);
}

//arr배열의 값을 int형으로 변환해서 넣어주고
//마지막으로 printf에서 arr[0] ~arr[마지막인덱스]출력
//어렵다.

//1020
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        String arr[] = a.split("-");
        System.out.print(arr[0],arr[1]);
	}
}

//1021 1022
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        System.out.print(a);
// 스캐너에서 next는 공백전까지 입력받고 nextLine은 그라인다받음

//1023
// 배열쓰는방법
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        String arr[] = a.split("\\.");
        System.out.print(arr[0]+"\n"+arr[1]);
//그냥 float으로 받아도될거같은데. 그래도 배열을 이용하네

//1024
이거좀 지렸다. 위에 1019번 풀이에서본 개선된 for문 이용했다
        Scanner s = new Scanner(System.in);
	      String a = s.nextLine();
	      String arr[] = a.split("");
	      for (String abc : arr) {
	    	  System.out.println("''"+abc+'\''); //이거둘다가능
	      }

다른 방법인데 이건뭐야. 문자열을 문자로 바꾸는 방법이
"3".charAt(0)  = '3' 인데 0이 아니라 다른 숫자가 들어가면 그 문자열의 인덱스를
문자로 추출해오는듯
"pie".charAt(2) = 'i'
이걸 사용해서 문자열 잘라온듯.
내가 split 공백 사용해서 온거랑 비슷한 방법인 것 같은데 알아둬야할 거 같다.
        Scanner s = new Scanner(System.in);
                String word = s.nextLine();
                int w = word.length();

                for(int i=0; i<w; i++){
                    System.out.println("'"+word.charAt(i)+"'");
                }
//12/30 23:42 끝


//1025
Scanner s = new Scanner(System.in);
String a = s.next();
char b[] = new char[a.length()];  // 뭐냐 [] 뒤에변수에 썼는데도되네. 둘다가능한 방식.
for (int i=0;i<a.length();i++) {
  b[i] = a.charAt(i);
}
System.out.println("["+b[0]+"0000"+"]");
System.out.println("["+b[1]+"000"+"]");
System.out.println("["+b[2]+"00"+"]");
System.out.println("["+b[3]+"0"+"]");
System.out.println("["+b[4]+"]");
위에 내가 푼거
일부러 나머지 이용하는 방법 안씀. 근데 좀 비슷한 노가다인듯

Scanner s = new Scanner(System.in);
String num = s.nextLine();
char[] array = num.toCharArray();

System.out.println("["+array[0]+"0000]");
System.out.println("["+array[1]+"000]");
System.out.println("["+array[2]+"00]");
System.out.println("["+array[3]+"0]");
System.out.println("["+array[4]+"]");
toCharArray : 문자열 데이터를 char배열에 한글자씩 삽입하는 메소드
입력 하나씩 자를 때 유용할듯

//1031~ 1035
입력받은 정수를 8진수로 출력 printf("%o",a)
입력받은 정수를 16진수 소문자로 출력 printf("%x",a)
입력받은 정수를 16진수 대문자로 출력 printf("%X",a)
정수 입력받기
int a = s.nextInt();   default값 10진수로 입력받음
int a = s.nextInt(8);  8진수로 입력받음
int a = s.nextInt(16); 16진수로 입력받음
//1034 8진수를 받고 10진수로 출력
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt(8);
        System.out.printf("%d",a);
    }
}

//1036 문자 하나 입력받아 10진수로 출력
    Scanner s = new Scanner(System.in);
		char a = s.next().charAt(0);
		System.out.print((int)a);
		s.close();

//1037 정수 입력받아 아스키문자로 출력 1036거꾸로
    Scanner s = new Scanner(System.in);
    char a = s.nextInt();
    System.out.print((char)a);
    s.close();

//1038 == 1039  int 범위 항상생각 그냥 불안하면 long타입선언

//1040
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		System.out.printf("%d",-a);  //-a 하면 부호 반대 print(a*(-1))도 가능하네
		s.close();

//1041
    Scanner s = new Scanner(System.in);
		char a = s.next().charAt(0);
		System.out.print((char)(a+1));

    Scanner s = new Scanner(System.in);
		char a = s.next().charAt(0);
		a += 1;
		System.out.print(a);
두가지방법가능
//1042
    Scanner s = new Scanner(System.in);
    int a = s.nextInt();
    int b = s.nextInt();
    System.out.print(a/b);
//1043
    Scanner s = new Scanner(System.in);
    int a = s.nextInt();
    int b = s.nextInt();
    System.out.print(a%b);
//1045
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		System.out.println((long)(a+b));
		System.out.println(a-b);
		System.out.println((long)(a*b));
		System.out.println(a/b);
		System.out.println(a%b);
		System.out.printf("%.2f",(float)a/b);
//1046
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		System.out.println((long)a+b+c);
		System.out.printf("%.1f",(float)(a+b+c)/3); // (a+b+c)/3.0

//1047 1048
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		System.out.printf("%d",a<<b); // 2**b 배
비트시프트 연산. <<1 하면 2배  >>1 하면 0.5 배

//1049 ~ 1052 비교연산
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		if (a>b) {
			System.out.println("1");
		} else {
			System.out.println("0");
		}

//1053 ~ 1058 논리연산
    Scanner s = new Scanner(System.in);
    int a = s.nextInt();
    int b = s.nextInt();
    if (a == 0 && b==0) {
    System.out.println("1");
    } else {
    System.out.println("0");
    }

//1059 ~ 1062 비트단위 논리연산. 안배워서 패스

//1063 ~ 1064 삼항연산
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		System.out.print(a>b?a:b);

    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		System.out.print((a>b?b:a)>c?c:(a>b?b:a)); //정수 3개중 제일 작은 수 출력

//1085 ~ 1086 기초-종합
    Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int s = sc.nextInt();
		System.out.printf("%.1f MB",(float)h*b*c*s/1024/1024/8);

    Scanner s = new Scanner(System.in);
  	int w = s.nextInt();
  	int h = s.nextInt();
		int b = s.nextInt();
  	System.out.printf("%.2f MB",(float)w*h*b/1024/1024/8);
