-- Delete Duplicate Emails
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) as id
        FROM Person
        GROUP BY email
    ) AS temp
);