# training-PR
PR 연습
10.23 어플 설치
10.28 수정
10/30
시험 망함 슬프다...

11/3 시험 끝 행복하다

오! 모바일로 커밋하는 방법도 있군

모바일 커밋 너무 편하다~

잔디잔디

배고픈데

따뜻한아이스돌체라떼에우유빼고물

print("20231596")
name=input("이름은?")
<%= name %>

순대보다 떡볶이보다 어묵

데이터베이스과제

use testdb;

-- [Quiz 2]  (MySQL) 실습: (고객)

-- 다음 조건을 만족하는 테이블을 생성하시오

-- 고객 테이블은 고객아이디, 고객이름, 나이, 등급, 직업, 적립금 속성으로
-- 구성되고, 고객아이디 속성이 기본키다.
-- 고객이름과 등급 속성은 값을 반드시 입력해야 하고,
-- 적립금 속성은 값을 입력하지 않으면 0이 기본으로 입력되도록 한다
-- 등급에 입력할 값은 vip, gold, silver 로 값의 범위를 설정한다

/*--------------고객 스키마 ---------------*/
drop table if exists 고객;

-- 다음을 완성하시오
create table 고객 (
    고객아이디  varchar(8)      NOT NULL,
    고객이름   char(5)         NOT NULL,
    나이      int,
    등급      varchar(10)     NOT NULL,     
    직업      varchar(10)     NOT NULL,
    적립금     int            default(0),
    primary key(고객아이디),
    CONSTRAINT ck_고객_등급 
                         CHECK (등급 IN ('vip','gold','silver'))
);

-- 고객(고객아이디,고객이름,나이,등급,직업,적립금)
insert into 고객 values('apple','정소화',20,'gold','학생',1000);
insert into 고객 values('banana','김선우',25,'vip','간호사',2500);
insert into 고객 values('carrot','고명석',28,'gold','교사',4500);
insert into 고객 values('orange','김용축',22,'silver','학생',NULL);
insert into 고객 values('melon','성원용',35,'gold','회사원',5000);
insert into 고객 values('peach','오형준',NULL,'silver','의사',300);
insert into 고객 values('pear','채광주',31,'silver','회사원',500);

select * from 고객;
-- [Quiz 2]  (MySQL) 실습: (고객)

-- 1) 직업이 학생, 간호사, 교사인 고객의 이름, 직업, 등급을 검색
select 고객이름, 직업, 등급
from 고객
where 직업='학생' or 직업='간호사' or 직업='교사';

-- 2) 적립금이 300 이상인 고객 중에서 
-- 나이를 알 수 없는 고객아이디, 나이, 적립금을 검색하라
select 고객아이디, 나이, 적립금
from 고객
where 적립금>=300 and 나이 is null;

-- 3) 등급이 gold인 고객 중에서 고객아이디, 등급, 적립금을 검색하라. 
-- 단, 등급을 오름차순 정렬하고 등급이 같으면 적립금의 내림차순 정렬하라
select 고객아이디, 등급, 적립금
from 고객
where 등급='gold'
order by 등급 asc, 적립금 desc;

-- 4) 등급별 적립급 평균을 검색하라, 
-- (단, 적립금 평균이 1000원 이상인 등급에 대해 검색)
select 등급, avg(적립금)
from 고객
group by 등급
having avg(적립금) >= 1000;
