-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
INNER JOIN tvshows_ratings ON tv_shows.id = tvshows_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
