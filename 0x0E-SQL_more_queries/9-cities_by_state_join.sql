-- lists all cities cntained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON states.id = cities.state_id;
