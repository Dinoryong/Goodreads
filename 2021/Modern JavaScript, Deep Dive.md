# 모던 자바스크립트 Deep Dive

-----

> [toc]

Chp 01 프로그래밍

1.1 프로그래밍이란 ?

1.2 프로그래밍 언어

1.3 구문과 의미



Chp 02 자바스크립트란 ?

2.1 자바스크립트의 탄생

2.2 자바스크립트의 표준화

2.3 자바스크립트 성장의 역사

​	2.3.1 Ajax

​	2.3.2 jQuery

​	2.3.3 V8 자바스크립트 엔진

​	2.3.4 Node.js

​	2.3.5 SPA 프레임워크

2.4 자바스크립트의 특징

2.5 자바스크립트의 특징

2.6 ES6 브라우저 지원 현황



Chp 03

3.1 자바스크립트 실행 환경

3.2 웹 브라우저

​	3.2.1 개발자 도구

​	3.2.2 콘솔

​	3.2.3 브라우저에서 자바스크립트 실행

​	3.2.4 디버깅

3.3 Node.js

​	3.3.1 Node.js와 npm 소개

​	3.3.2 Node.js 설치

​	3.3.3 Node.jss REPL

3.4 비주얼 스튜디오 코드

​	3.4.1 비주얼 스튜디오 코드 설치

​	3.4.2 내장 터미널

​	3.4.3 Code Runner 확장 플러그인

​	3.4.4 Live Server 확장 플러그인



Chp 04

4.1 변수란 무엇인가 ? 왜 필요한가 ?

4.2 식별자

4.3 변수 선언

4.4. 변수 선언의 실행 시점과 변수 호이스팅

4.5 값의 할당

4.6 값의 재할당

4.7 식별자 네이밍 규칙



Chp 05

5.1 값

5.2 리터럴

5.3 표현식

5.4 문

5.5 세미콜론과 세미콜론 자동 삽입 기능

5.6 표현식인 문과 표현식이 아닌 문



Chp 06

6.1 숫자 타입

6.2 문자열 타입

6.3 템플릿 리터럴

​	6.3.1 멀티라인 문자열

​	6.3.2 표현식 삽입

6.4 불리언 타입

6.5 undefined 타입

6.6 null 타입

6.7 심벌 타입

6.8 객체 타입

6.9 데이터 타입의 필요엇ㅇ

​	6.9.1 데이터 타입에 의한 메모리 공간의 확보와 참조

​	6.9.2 데이터 타입에 의한 값의 해석

6.10 동적 타이핑

​	6.10.1 동적 타입 언어와 정적 타입 언어

​	6.10.2 동적 타입 언어와 변수



Chp 07

7.1 산술 연산자

​	7.1.1 이항 산술 연산자

​	7.1.2 단항 산술 연산자

​	7.1.3 문자열 연결 연산자

7.2 할당 연산자

7.3 비교 연산자

​	7.3.1 동등/일차 비교 연산자

​	7.3.2 대소 관계 비교 연산자

7.4 삼항 조건 연산자

7.5 논리 연산자

7.6 쉼표 연산자

7.7 그룹 연산자

7.8 typeof 연산자

7.9 지수 연산자

7.10 그 외의 연산자

7.11 연산자의 부수 효과

7.12 연산자 우선순위

7.13 연산자 결합 순서



Chp 08 제어문

8.1 블록문

8.2 조건문

​	8.2.1 if...else 문

​	8.2.2 switch 문

8.3 반복문

​	8.3.1 for 문

​	8.3.2 while 문

​	8.3.3 do...while 문

8.4 break 문

8.5 continue 문



Chp 09 타입 변환과 단축 평가

9.1 타입 변환이란 ?

9.2 암묵적 타입 변환

​	9.2.1 문자열 타입으로 변환

​	9.2.2 숫자 타입으로 변환

​	9.2.3 불리언 타입으로 변환

9.3 명시적 타입 변환

​	9.3.1 문자열 타입으로 변환

​	9.3.2 숫자 타입으로 변환

​	9.3.3 불리언 타입으로 변환

9.4 단축 평가

​	9.4.1 논리 연산자를 사용한 단축 평가

​	9.4.2 옵셔널 체이닝 연산자

​	9.4.3 null 병합 연산자



Chp 10 객체 리터럴

10.1 객체란 ?

10.2 객체 리터럴에 의한 객체 생성

10.3 프로퍼티

10.4 메서드

10.5 프로퍼티 접근

10.6 프로퍼티 값 갱신

10.7 프로퍼티 동적 생성

10.8 프로퍼티 삭제

10.9 ES6에서 추가된 객체 리터럴의 확장 기능

​	10.9.1 프로퍼티 축약 표현

​	10.9.2 계산된 프로퍼티 이름

​	10.9.3 메서드 축약 표현



Chp 11 원시 값과 객체의 비교

11.1 원시 값

​	11.1.1 변경 불가능한 값

​	11.1.2 문자열과 불변성

​	11.1.3 값에 의한 전달

11.2 객체

​	11.2.1 변경 가능한 값

​	11.2.2 참조에 의한 전달



Chp 12 함수

12.1 함수란 ?

12.2 함수를 사용하는 이유

12.3 함수 리터럴

12.4 함수 정의

​	12.4.1 함수 선언문

​	12.4.2 함수 표현식

​	12.4.3 함수 생성 시점과 함수 호이스팅

​	12.4.4 Function 생성자 함수

​	12.4.5 화살표 함수

12.5 함수 호출

​	12.5.1 매개변수와 인수

​	12.5.2 인수 확인

​	12.5.3 매개변수의 최대 개수

​	12.5.4 반환문

12.6 참조에 의한 전달과 외부 상태의 변경

12.7 다양한 함수의 형태

​	12.7.1 즉시 실행 함수

​	12.7.2 재귀 함수

​	12.7.3 중첩 함수

​	12.7.4 콜백 함수

​	12.7.5 순수 함수와 비순수 함수



Chp 13 스코프

13.1 스코프란 ?

13.2 스코프의 종류

​	13.2.1 전역과 전역 스코프

​	13.2.2 지역과 지역 스코프

13.3 스코프 체인

​	13.3.1 스코프 체인에 의한 변수 검색

​	13.3.2 스코프 체인에 의한 함수 검색

13.4 함수 레벨 스코프

13.5 렉시컬 스코프



Chp 14 전역 변수의 문제점

14.1 변수의 생명 주기

​	14.1.1 지역 변수의 생명 주기

​	14.1.2 전역 변수의 생명 주기

14.2 전역 변수의 문제점

14.3 전역 변수의 사용을 억제하는 방법

​	14.3.1 즉시 실행 함수

​	14.3.2 네임스페이스 객체

​	14.3.3 모듈 패턴

​	14.3.4 ES6 모듈



Chp 15 let, const 키워드와 블록 레벨 스코프

15.1 var 키워드로 선언한 변수의 문제점

​	15.1.1 변수 중복 선언 허용

​	15.1.2 함수 레벨 스코프

​	15.1.3 변수 호이스팅

15.2 let 키워드

​	15.2.1 변수 중복 선언 금지

​	15.2.2 블록 레벨 스코프

​	15.2.3 변수 호이스팅

​	15.2.4 전역 객체와 let

15.3 const 키워드

​	15.3.1 선언과 초기화

​	15.3.2 재할당 금지

​	15.3.3 상수

​	15.3.4 const 키워드와 객체

15.4 var vs. let vs. const



Chp 16. 프로퍼티 어트리뷰트

16.1 내부 슬롯과 내부 메서드

16.2 프로퍼티 어트리뷰트와 프로퍼티 디스크립터 객체

16.3 데이터 프로퍼티와 접근자 프로퍼티

​	16.3.2 데이터 프로퍼티

​	16.3.2 접근자 프로퍼티

16.4 프로퍼티 정의

16.5 객체 변경 방지

​	16.5.1 객체 확장 금지

​	16.5.2 객체 밀봉

​	16.5.3 객체 동결

​	16.5.4 불변 객체



Chp 17. 생성자 함수에 의한 객체 생성

17.1 Object 생성자 함수

17.2 생성자 함수

​	17.2.1 객체 리터럴에 의한 객체 생성 방식의 문제점

​	17.2.2 생성자 함수에 의한 객체 생성 방식의 장점

​	17.2.3 생성자 함수의 인스턴스 생성 과정

​	17.2.4 내부 메서드 [[Call]] 과 [[Construct]]

​	17.2.5 constructor 와 non-constructor 의 구분

​	17.2.6 new 연산자

​	17.2.7 new.target



Chp 18. 함수와 일급 객체

18.1 일급 객체

18.2 함수 객체의 프로퍼티

​	18.2.1 arguments 프로퍼티

​	18.2.2 caller 프로퍼티

​	18.2.3 length 프로퍼티

​	18.2.4 name 프로퍼티

​	18.2.5 `__proto__` 접근자 프로퍼티

​	18.2.6 prototype 프로퍼티



Chp 19 프로토타입

19.1 객체지향 프로그래밍

19.2 상속과 프로토타입

19.3 프로토타입 깨체

​	19.3.1 `__proto__` 접근자 프로퍼티

​	19.3.2 함수 객체의 prototype 프로퍼티

​	19.3.3 프로토타입의 constructor 프로퍼티와 생성자 함수

19.4 리터럴 표기법에 의해 생성된 객체의 생성자 함수와 프로토타입

19.5 프로토타입의 생성 시점

​	19.5.1 사용자 정의 생성자 함수와 프로토타입 생성 시점

​	19.5.2 빌트인 생성자 함수와 프로토타입 생성 시점

19.6 객체 생성 방식과 프로토타입의 결정

​	19.6.1 객체 리터럴에 의해 생성된 객체의 프로토타입

​	19.6.2 Object 생성자 함수에 의해 생성된 객체의 프로토타입

​	19.6.3 생성자 함수에 의해 생성된 객체의 프로토타입

19.7 프로토타입 체인

19.8 오버라이딩과 프로퍼티 섀도잉

19.9 프로토타입의 교체

​	19.9.1 생성자 함수에 의한 프로토타입의 교체

​	19.9.2 인스턴스에 의한 프로토타입의 교체

19.10 instanceof 연산자

19.11 직접 상속

​	19.11.1 Object.create 에 의한 직접 상속

​	19.11.2 객체 리터럴 내부에서 `__proto__` 에 의한 직접 상속

19.12 정적 프로퍼티/메서드

19.13 프로퍼티 존재 확인

​	19.13.1 in 연산자

​	19.13.2 Object.prototyle.hasOwnProperty 메서드

19.14 프로퍼티 열거

​	19.14.1 for...in 문

​	19.14.2 Object.keys/values/entries 메서드



Chp 20. strict mode

20.1 strict mode 란 ?

20.2 strict mode의 적용

20.3 전역에 strict mode를 적용하는 것은 피하자

20.4 함수 단위로 strict mode를 적용하는 것도 피하자

20.5 strict mode 가 발생시키는 에러

​	20.5.1 암묵적 전역

​	20.5.2 변수, 함수, 매개변수의 삭제

​	20.5.3 매개변수 이름의 중복

​	20.5.4 with 문의 사용

20.6 strict mode 적용에 의한 변화

​	20.6.1 일반 함수의 this

​	20.6.2 arguments 객체



Chp 21. 빌트인 객체

21.1 자바스크립트 객체의 분류

21.2 표준 빌트인 객체

21.3 원시값과 래퍼 객체

21.4 전역 객체

​	21.4.1 빌트인 전역 프로퍼티

​	21.4.2 빌트인 전역 함수

​	21.4.3 암묵적 전역



Chp 22. this

22.1 this 키워드

22.2 함수 호출 방식과 this 바인딩

​	22.2.1 일반 함수 호출

​	22.2.2 메서드 호출

​	22.2.3 생성자 함수 호출

​	22.2.4 Function.prototype.apply/calll/bind 메서드에 의한 간접 호출



Chp 23. 실행 컨텍스트

23.1 소스코드의 타입

23.2 소스코드의 평가와 실행

23.3 실행 컨텍스트의 역할

23.4 실행 컨텍스트 스택

23.5 렉시컬 환경

23.6 실행 컨텍스트의 생성과 식별자 검색 과정

​	23.6.1 전역 객체 생성

​	23.6.2 전역 코드 평가

​	23.6.3 전역 코드 실행

​	23.6.4 foo 함수 코드 평가

​	23.6.5 foo 함수 코드 실행

​	23.6.6 bar 함수 코드 평가

​	23.6.7 bar 함수 코드 실행

​	23.6.8 bar 함수 코드 실행 종료

​	23.6.9 foo 함수 코드 실행 종료

​	23.6.10 전역 코드 실행 종료

23.7 실행 컨텍스트와 블록 레벨 스코프



Chp 24. 클로저

24.1 렉시컬 스코프

24.2 함수 객체의 내부 슬록 [[Environment]]

24.3 클로저와 렉시컬 환경

24.4 클로저의 활용

24.5 캡슐화와 정보 은닉

24.6 자주 발생하는 실수



Chp 25. 클래스

25.1 클래스는 프로토타입의 문법적 설탕인가 ?

25.2 클래스 정의

25.3 클래스 호이스팅

25.4 인스턴스 생성

25.5 메서드

​	25.5.1 constructor

​	25.5.2 프로토타입 메서드

​	25.5.3 정적 메서드






















