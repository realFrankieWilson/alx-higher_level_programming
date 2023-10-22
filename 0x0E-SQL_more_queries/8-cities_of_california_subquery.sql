-- lists all the cities fo California that can be found in the database
--	hbtn_0d_usa.
SELECT id, name from cities
WHERE state_id = (
	SELECT id FROM states WHERE name = 'California'
);
