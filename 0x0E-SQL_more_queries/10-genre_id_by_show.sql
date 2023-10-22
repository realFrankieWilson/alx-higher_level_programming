-- Lists all shows contained in hbtn_0d_tvshows that have at least one
--	genre linked.
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON states.id = cities.state_id;
ORDER BY cities.id;
