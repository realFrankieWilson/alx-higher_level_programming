-- Prints the full description of the table first_table from the database
--	Usage of DESCRIBE or EXPLAIN statement are not allowed
-- SHOW CREATE TABLE
-- hbtn_0c_0.first_table
SELECT column_name, column_type, is_nullable, column_default
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
	AND TABLE_NAME = 'first_table';
