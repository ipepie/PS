기초3. if ~ else
//1065 ~ 1070

//1066
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		if (a%2==0) {
			System.out.println("even");
		} else {
			System.out.println("odd");
		}
		if (b%2==0) {
			System.out.println("even");
		} else {
			System.out.println("odd");
		}
		if (c%2==0) {
			System.out.println("even");
		} else {
			System.out.println("odd");
		}
//1067
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		if (a>0) {
			System.out.println("plus");
		} else {
			System.out.println("minus");
		}
		if (a%2==0) {
			System.out.println("even");
		} else {
			System.out.println("odd");
		}
//1068
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		if (a>=90) {
			System.out.println("A");
		} else if(a>=70) {
			System.out.println("B");
		} else if(a>=40) {
			System.out.println("C");
		} else {
			System.out.println("D");
		}
//1069
    Scanner s = new Scanner(System.in);
    char a = s.next().charAt(0);
    switch(a) {
    case 'A':
      System.out.print("best!!!");
      break;
    case 'B':
      System.out.print("good!!");
      break;
    case 'C':
      System.out.print("run!");
      break;
    case 'D':
      System.out.print("slowly~");
      break;
    default:
      System.out.print("what?");
    }
스위치문의 조건은 정수값만 들어갈 수 있지만 문자도 아스키코드 정수값이라 가능하다.
//1070
    Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		switch(a) {
		case 12: case 1: case 2:
			System.out.print("winter");
			break;
		case 3: case 4: case 5:
			System.out.print("spring");
			break;
		case 6: case 7: case 8:
			System.out.print("summer");
			break;
		default:
			System.out.print("fall");
		}
