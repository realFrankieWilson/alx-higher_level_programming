-- lists all genres of the show not linked to the sow Dexter using 
--	the hbtn_0d_tvsows database.
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.id NOT IN(
	SELECT tv_genres.id
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
)
ORDER BY tv_genres.name;
