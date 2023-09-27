-- Keep a log of any SQL queries you execute as you solve the mystery.
crime id 295
28/07/2021 10:15 am

Ruth -> patente salio 10:25
Eugene -> ATM in the morning
Raymong -> first fligth to fiftyville 29/07/2021

select * from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour in (9,10) order by license_plate;

select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and minute in (15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) and activity = "exit";
+---------------+
| license_plate |
+---------------+
| 5P2BI95       |
| 94KL13X       |
| 6P58WS2       |
| 4328GD8       |
| G412CB7       |
| L93JTIZ       |
| 322W7JE       |
| 0NTHK55       |
+---------------+

select name, phone_number, passport_number from people where license_plate in (select license_plate from bakery_security_logs where year = 20
21 and month = 7 and day = 28 and hour = 10 and minute in (15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) and activity = "exit");

+---------+----------------+-----------------+
|  name   |  phone_number  | passport_number |
+---------+----------------+-----------------+
| Vanessa | (725) 555-4692 | 2963008352      |
| Barry   | (301) 555-4174 | 7526138472      |
| Iman    | (829) 555-5269 | 7049073643      |
| Sofia   | (130) 555-0289 | 1695452385      |
| Luca    | (389) 555-5198 | 8496433585      |
| Diana   | (770) 555-1861 | 3592750733      |
| Kelsey  | (499) 555-9472 | 8294398571      |
| Bruce   | (367) 555-5533 | 5773159633      |
+---------+----------------+-----------------+

select phone_number from people where license_plate in (select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and minute in (15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) and activity = "exit");

select receiver from phone_calls where year = 2021 and month = 7 and day = 28 and caller IN (select phone_number from people where license_plate in (select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and minute in (15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) and activity = "exit"))

select name,passport_number from people where phone_number IN (select receiver from phone_calls where year = 2021 and month = 7 and day = 28
and caller IN (select phone_number from people where license_plate in (select license_plate from bakery_security_logs where year = 2021 and month = 7
 and day = 28 and hour = 10 and minute in (15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) and activity = "exit")));
+---------+-----------------+
|  name   | passport_number |
+---------+-----------------+
| Larry   | 2312901747      |
| Gregory | 3355598951      |
| Joan    | NULL            |
| Jack    | 9029462229      |
| Melissa | 7834357192      |
| Amanda  | 1618186613      |
| Carl    | 7771405611      |
| Philip  | 3391710505      |
| Robin   | NULL            |
| Deborah | 8714200946      |
+---------+-----------------+