# BookClub_2021_11

-----

## 11.15 

### 1. [JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript)  : [Modern JavaScript Deep Dive](https://github.com/Dinoryong/Goodreads/blob/main/2021/Modern%20JavaScript%2C%20Deep%20Dive.md)

>  Chp 01, 02, 03, 04

- [How do you clear memory in Javascript?](https://stackoverflow.com/questions/7248122/how-do-you-clear-memory-in-javascript)

  <details><summary>answer</summary>
    G.C 가 내장되어 있기 때문에 정기적으로 검사하면서 자동으로 관리해준다
  </details>

  

- [dangling point](https://ko.wikipedia.org/wiki/%ED%97%88%EC%83%81_%ED%8F%AC%EC%9D%B8%ED%84%B0) : 다시 가리킬 가능성이 전혀 없는 메모리 변수

- [메세지 큐](https://sugerent.tistory.com/644) ( [aws 설명](https://aws.amazon.com/ko/message-queue/#:~:text=A%20message%20queue%20is%20a,once%2C%20by%20a%20single%20consumer.) ) : 비동기식 서비스 대 서비스 통신 형태, [RabbitMQ](https://www.rabbitmq.com/) ([설명](https://blog.dudaji.com/general/2020/05/25/rabbitmq.html))



### 2. Kafka

> 개념, 목적, 활용 분야

- [LINE에서 Kafka를 사용하는 방법](https://engineering.linecorp.com/ko/blog/how-to-use-kafka-in-line-1/)
- [Auto scale out](https://bcho.tistory.com/1114)
- [DB 파티셔닝](https://soye0n.tistory.com/267)
- [Data Lake](https://www.samsungsds.com/kr/insights/big_data_lake.html) 
- [Data Pipeline](https://maily.so/grabnews/posts/ecaebe)
- [카프카란?](https://freedeveloper.tistory.com/396) : 카프카는 디스크 기반인데 어떻게 성능이
- Autoscaling
- 스케일 인 , 스케일 아웃
- 스케일 업
- 팬인 vs 팬아웃
- 캐싱, 캐시 메모리, 페이지 캐시
- 디스크 I/O
- [구글 SPDY](https://ko.wikipedia.org/wiki/SPDY)
- HPA : Horizontal Pod Autoscaler
- HA : High Availability
- 레플리카 -> 개념 확실하게 다시
- Load Balancing
- 트래픽 라우팅



--------

## 11.16

### 1. [JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript)  : [Modern JavaScript Deep Dive](https://github.com/Dinoryong/Goodreads/blob/main/2021/Modern%20JavaScript%2C%20Deep%20Dive.md)

> Chp 04 05 06 

- Expression vs Statement in JavaScript : [ref](https://2ssue.github.io/common_questions_for_Web_Developer/docs/Javascript/expression_statement.html)



### 2. Kafka

> 카프카의 역사

- SPOF (Single Point of Failure) : [ref](https://datalibrary.tistory.com/207)
- Data Lake : [definition](https://aws.amazon.com/ko/big-data/datalakes-and-analytics/what-is-a-data-lake/)
- [4 big data architectures, Data Streaming, Lambda architecture, Kappa architecture, and Unifield architecture](https://medium.com/dataprophet/4-big-data-architectures-data-streaming-lambda-architecture-kappa-architecture-and-unifield-d9bcbf711eb9#:~:text=The%20Kappa%20architecture%20is%20optimized,at%20the%20data%20lake%20level.)
- [From Lambda to Kappa: evolution of Big Data architectures](https://en.paradigmadigital.com/dev/from-lambda-to-kappa-evolution-of-big-data-architectures/)
- [KSQLDB](https://www.confluent.io/product/ksql/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka_mt.xct_rgn.apac_lng.eng_dv.all_con.kafka-ksql&utm_term=ksql&creative=&device=c&placement=&gclid=Cj0KCQiAys2MBhDOARIsAFf1D1fg25vlrJGri0uUFja92by_3QI-FifT34yMoGfY-LB8EIqsekZZrs0aAvDqEALw_wcB) : kafka 스트림즈를 추상화 한 DB
- [Kafka stream과 KSQL 소개 및 설명, 차이점](https://blog.voidmainvoid.net/266) : 클라이언트가 speed layer를 바로바로 사용할 수 있게 실시간으로
- [빅데이터 처리와 저장의 핵심 기술, 하둡과 NoSQL](https://flipdata.tistory.com/74)
- [Kafka Summit 2020: Event Streaming Everywhere was hosted virtually](https://www.kafka-summit.org/2020)





