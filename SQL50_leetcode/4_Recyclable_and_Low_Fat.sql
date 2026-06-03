-- LeetCode SQL 50: Recyclable & Low Fat
-- Difficulty: Easy
-- Concept: SELECT, WHERE, AND
-- Find product IDs that are both low fat AND recyclable

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Alternative Solution:
-- SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y' ORDER BY product_id;
