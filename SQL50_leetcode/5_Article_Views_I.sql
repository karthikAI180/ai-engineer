-- LeetCode SQL 50: Article Views I
-- Difficulty: Easy
-- Concept: SELECT, WHERE, DISTINCT, ORDER BY
-- Find authors who viewed their own articles, ordered by ID ascending

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;

-- Alternative Solution using GROUP BY:
-- SELECT author_id FROM Views WHERE author_id = viewer_id GROUP BY author_id ORDER BY author_id;
