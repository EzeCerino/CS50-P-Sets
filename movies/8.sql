SELECT name FROM people JOIN stars ON people.id = stars.person_id WHERE movie_id = (SELECT id FROM movies where title LIKE "Toy Story%");

/*In 8.sql, write a SQL query to list the names of all people who starred in Toy Story.
Your query should output a table with a single column for the name of each person.*/