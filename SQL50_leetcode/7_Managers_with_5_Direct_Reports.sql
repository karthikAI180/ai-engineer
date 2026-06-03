-- LeetCode SQL 50: Managers with at Least 5 Direct Reports
-- Difficulty: Medium
-- Concept: Self-JOIN, GROUP BY, HAVING, COUNT
-- Find managers who have 5 or more direct reports

-- Solution 1: Using Subquery
SELECT e1.name
FROM Employee e1
WHERE (
    SELECT COUNT(*)
    FROM Employee e2
    WHERE e2.managerId = e1.id
) >= 5;

-- Solution 2: Using JOIN + GROUP BY (Alternative)
-- SELECT e1.name
-- FROM Employee e1
-- INNER JOIN Employee e2 ON e1.id = e2.managerId
-- GROUP BY e1.id, e1.name
-- HAVING COUNT(e2.id) >= 5;

-- Solution 3: Using Window Functions (Alternative)
-- WITH manager_counts AS (
--     SELECT managerId, COUNT(*) AS report_count
--     FROM Employee
--     WHERE managerId IS NOT NULL
--     GROUP BY managerId
-- )
-- SELECT e.name
-- FROM Employee e
-- INNER JOIN manager_counts mc ON e.id = mc.managerId
-- WHERE mc.report_count >= 5;
