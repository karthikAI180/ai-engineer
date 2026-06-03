-- LeetCode SQL 50: Find Customer Referee
-- Difficulty: Easy
-- Concept: WHERE, IS NULL, OR
-- Find customers who have NO referee OR whose referee is NOT customer 2

-- IMPORTANT: NULL != 2 returns NULL (not TRUE), so IS NULL is necessary!

SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;

-- Alternative Solution using COALESCE:
-- SELECT name FROM Customer WHERE COALESCE(referee_id, 0) != 2;

-- WRONG SOLUTION (DO NOT USE):
-- SELECT name FROM Customer WHERE referee_id != 2; 
-- This misses customers with referee_id = NULL!
