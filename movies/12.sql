SELECT title FROM movies WHERE id IN (
SELECT movie_id from stars WHERE person_id = (SELECT id FROM people WHERE name = "Bradley Cooper")
INTERSECT
SELECT movie_id from stars WHERE person_id = (SELECT id FROM people WHERE name = "Jennifer Lawrence"));

/*SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id WHERE movies.id IN
(SELECT movie_id from stars JOIN people ON stars.person_id = people.id WHERE people.name = "Bradley Cooper" OR people.name = "Jennifer Lawrence");

/*In 12.sql, write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Bradley Cooper.
You may assume that there is only one person in the database with the name Jennifer Lawrence*/