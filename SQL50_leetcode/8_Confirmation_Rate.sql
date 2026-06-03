-- LeetCode SQL 50: Confirmation Rate
-- Difficulty: Medium
-- Concept: LEFT JOIN, GROUP BY, ROUND, CASE, COUNT
-- Calculate confirmation rate for each user (confirmed actions / total actions)

SELECT s.user_id,
       ROUND(
           COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END) 
           / 
           COUNT(*), 
           2
       ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;

-- Alternative Solution using SUM:
-- SELECT s.user_id,
--        ROUND(
--            SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) 
--            / 
--            COUNT(c.action),
--            2
--        ) AS confirmation_rate
-- FROM Signups s
-- LEFT JOIN Confirmations c ON s.user_id = c.user_id
-- GROUP BY s.user_id;

-- Alternative Solution with COALESCE for NULL handling:
-- SELECT s.user_id,
--        ROUND(
--            COALESCE(
--                SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) 
--                / 
--                COUNT(*),
--                0
--            ),
--            2
--        ) AS confirmation_rate
-- FROM Signups s
-- LEFT JOIN Confirmations c ON s.user_id = c.user_id
-- GROUP BY s.user_id;
