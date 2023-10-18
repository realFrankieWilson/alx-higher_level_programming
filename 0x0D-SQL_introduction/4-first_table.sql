-- CREATES a table called first_table in the current database in mysql server.
-- Description:
--	id of int.
--	name of char value.
--	If the talbe already exists, the script should not fail.
--	Select or show statement are forbidden.
CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
	);
