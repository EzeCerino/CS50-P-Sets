/*SELECT count(sqcol) from (
(SELECT name AS sqcol FROM people JOIN directors ON people.id = directors.person_id  WHERE directors.movie_id IN
(SELECT movie_id FROM ratings WHERE rating >= 9) GROUP BY name ORDER BY name));*/

SELECT name FROM people JOIN directors ON people.id = directors.person_id WHERE directors.movie_id IN
(SELECT movie_id FROM ratings WHERE rating >= 9.0) GROUP BY name ORDER BY name;

/*In 10.sql, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
Your query should output a table with a single column for the name of each person.
If a person directed more than one movie that received a rating of at least 9.0, they should only appear in your results once.*/