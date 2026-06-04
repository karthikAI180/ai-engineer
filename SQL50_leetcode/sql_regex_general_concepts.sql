-- ============================================================================
-- SQL REGULAR EXPRESSIONS (REGEX) - General Concepts
-- ============================================================================

-- Regular Expressions are patterns used to match strings
-- Much more powerful than LIKE operator!

-- ============================================================================
-- 1. BASIC REGEX SYNTAX
-- ============================================================================

/*
CHARACTER CLASSES:
. = any single character (except newline)
[abc] = any character in set (a OR b OR c)
[a-z] = any character in range (lowercase letters)
[0-9] = any digit
[^abc] = any character NOT in set

QUANTIFIERS (how many times):
* = 0 or more times
+ = 1 or more times
? = 0 or 1 time (optional)
{n} = exactly n times
{n,} = n or more times
{n,m} = between n and m times

ANCHORS (position):
^ = start of string
$ = end of string
\b = word boundary

SPECIAL:
| = OR (alternation)
() = grouping
\ = escape special characters
*/

-- ============================================================================
-- 2. COMMON REGEX PATTERNS
-- ============================================================================

/*
EMAIL PATTERN:
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

PHONE PATTERN:
^\d{3}-\d{3}-\d{4}$

URL PATTERN:
^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

DATE PATTERN (YYYY-MM-DD):
^\d{4}-\d{2}-\d{2}$

NUMBERS ONLY:
^\d+$

LETTERS ONLY:
^[a-zA-Z]+$

ALPHANUMERIC ONLY:
^[a-zA-Z0-9]+$
*/

-- ============================================================================
-- 3. SQL REGEX FUNCTIONS (varies by database)
-- ============================================================================

/*
MySQL:
- REGEXP or RLIKE



-- ============================================================================
-- 4. PRACTICAL EXAMPLES IN MYSQL
-- ============================================================================

-- Example 1: Match emails
-- Find all emails in format: something@domain.com
SELECT email
FROM users
WHERE email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';

-- Example 2: Match phone numbers
-- Find phone in format: 123-456-7890
SELECT phone
FROM contacts
WHERE phone REGEXP '^\d{3}-\d{3}-\d{4}$';

-- Example 3: Match digit-only values
-- Find IDs that contain only numbers
SELECT id
FROM records
WHERE id REGEXP '^[0-9]+$';

-- Example 4: Match dates (YYYY-MM-DD)
SELECT date_col
FROM logs
WHERE date_col REGEXP '^\d{4}-\d{2}-\d{2}$';

-- Example 5: NOT regex (^)
-- Find names that do NOT start with vowels
SELECT name
FROM users
WHERE name NOT REGEXP '^[aeiou]';

-- Example 6: OR logic (|)
-- Find entries that are either 'active' or 'pending'
SELECT status
FROM orders
WHERE status REGEXP '^(active|pending)$';

-- ============================================================================
-- 5. REGEX vs LIKE - COMPARISON
-- ============================================================================

/*
LIKE:
- Simple wildcards: % (any chars), _ (single char)
- Case-insensitive (usually)
- Faster but less powerful
- No complex patterns

REGEX:
- Full pattern matching power
- Can specify exact formats
- Slightly slower
- More complex syntax

EXAMPLES:

LIKE:
  WHERE email LIKE '%@gmail.com'
  → matches: user@gmail.com, test123@gmail.com, etc.

REGEX:
  WHERE email REGEXP '^[a-z0-9]+@gmail\.com$'
  → matches ONLY specific format (stricter)
*/

-- ============================================================================
-- 6. COMMON CHARACTER CLASSES (SHORTCUTS)
-- ============================================================================

/*
\d = [0-9] (digit)
\D = [^0-9] (NOT digit)
\w = [a-zA-Z0-9_] (word character)
\W = [^a-zA-Z0-9_] (NOT word character)
\s = space, tab, newline
\S = NOT whitespace
. = any character
*/

-- Example: Find strings with digits
SELECT text
FROM content
WHERE text REGEXP '\d';
-- Matches any string containing at least one digit

-- Example: Find words (only letters and underscores)
SELECT username
FROM users
WHERE username REGEXP '^\w+$';
-- Matches: user123, user_name, etc.

-- ============================================================================
-- 7. BRACKET EXPRESSIONS
-- ============================================================================

/*
[abc] = matches a, b, or c
[a-z] = matches any lowercase letter
[A-Z] = matches any uppercase letter
[0-9] = matches any digit
[a-zA-Z0-9] = matches alphanumeric
[^abc] = matches anything EXCEPT a, b, c
*/

-- Example: Find names starting with vowels
SELECT name
FROM users
WHERE name REGEXP '^[aeiou]';

-- Example: Find passwords with mixed case
SELECT password
FROM accounts
WHERE password REGEXP '[a-z]' AND password REGEXP '[A-Z]';

-- Example: Find values that DON'T contain numbers
SELECT text
FROM content
WHERE text REGEXP '^[^0-9]+$';
-- Matches only if NO digits present

-- ============================================================================
-- 8. QUANTIFIERS EXAMPLES
-- ============================================================================

/*
* = 0 or more times
+ = 1 or more times (at least 1)
? = 0 or 1 time (optional)
{n} = exactly n times
{n,} = n or more times
{n,m} = between n and m times
*/

-- Example: Exactly 10 digits (like zip code)
SELECT zip
FROM addresses
WHERE zip REGEXP '^\d{10}$';

-- Example: 2-4 letters followed by numbers
SELECT code
FROM products
WHERE code REGEXP '^[a-z]{2,4}[0-9]+$';
-- Matches: ab123, abc456, abcd999, etc.

-- Example: Optional dash in phone number
SELECT phone
FROM contacts
WHERE phone REGEXP '^\d{3}-?\d{3}-?\d{4}$';
-- Matches: 1234567890 or 123-456-7890

-- Example: Repeating pattern
SELECT text
FROM logs
WHERE text REGEXP '(ab){3}';
-- Matches: ababab (ab repeated 3 times)

-- ============================================================================
-- 9. ANCHORS
-- ============================================================================

/*
^ = start of string (must be first)
$ = end of string (must be last)
\b = word boundary
*/

-- Example: Exact match for status
SELECT status
FROM orders
WHERE status REGEXP '^PENDING$';
-- Matches ONLY "PENDING", not "PENDING_REVIEW"

-- Example: Starts with "user"
SELECT username
FROM accounts
WHERE username REGEXP '^user';
-- Matches: user123, username, user_admin, etc.

-- Example: Ends with ".com"
SELECT domain
FROM websites
WHERE domain REGEXP '\.com$';
-- Matches: google.com, github.com, etc.

-- ============================================================================
-- 10. ESCAPE SPECIAL CHARACTERS
-- ============================================================================

/*
Special characters need to be escaped with backslash (\)
. * + ? [ ] ( ) { } ^ $ | \

Examples:
\. = literal dot (not "any character")
\$ = literal dollar sign
\[ = literal bracket
*/

-- Example: Find strings with dots (literal dots, not wildcards)
SELECT filename
FROM files
WHERE filename REGEXP '\.txt$';
-- Matches: document.txt, file.txt (ends with literal .txt)

-- Example: Find price format ($100.00)
SELECT price
FROM products
WHERE price REGEXP '^\$[0-9]+\.[0-9]{2}$';
-- Matches: $100.00, $99.99, etc.

-- ============================================================================
-- 11. ALTERNATION (OR)
-- ============================================================================

/*
| = OR operator
(pattern1|pattern2|pattern3)
*/

-- Example: Find status that is one of several values
SELECT status
FROM orders
WHERE status REGEXP '^(pending|approved|rejected)$';
-- Matches ONLY one of these three

-- Example: Find colors
SELECT color
FROM products
WHERE color REGEXP '^(red|blue|green)$';

-- Example: Find file types
SELECT filename
FROM uploads
WHERE filename REGEXP '\.(jpg|png|gif)$';
-- Matches files ending with .jpg, .png, or .gif

-- ============================================================================
-- 12. GROUPING
-- ============================================================================

/*
() = group patterns together
- Apply quantifiers to groups
- Capture/organize patterns
*/

-- Example: Phone numbers with optional formatting
SELECT phone
FROM contacts
WHERE phone REGEXP '^(1-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$';
-- Matches: 1-123-456-7890 or 123-456-7890

-- Example: Repeating units
SELECT text
FROM logs
WHERE text REGEXP '^(ha){3,}$';
-- Matches: hahaha, hahahaha, hahahahahaha (3+ times)

-- ============================================================================
-- 13. PRACTICAL REAL-WORLD EXAMPLES
-- ============================================================================

-- Example 1: Validate email format
SELECT email
FROM users
WHERE email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  AND LENGTH(email) <= 255;

-- Example 2: Find strong passwords (uppercase, lowercase, digit, special char)
SELECT user_id
FROM accounts
WHERE password REGEXP '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])';

-- Example 3: Find URLs
SELECT url
FROM links
WHERE url REGEXP '^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$';

-- Example 4: Find credit card format (4 groups of 4 digits)
SELECT card_number
FROM payments
WHERE card_number REGEXP '^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
   OR card_number REGEXP '^[0-9]{16}$';

-- Example 5: Find IP addresses
SELECT ip_address
FROM logs
WHERE ip_address REGEXP '^([0-9]{1,3}\.){3}[0-9]{1,3}$';

-- ============================================================================
-- 14. DATABASE-SPECIFIC SYNTAX
-- ============================================================================

-- MYSQL:
-- WHERE column REGEXP 'pattern'
-- WHERE column RLIKE 'pattern'

-- POSTGRESQL:
-- WHERE column ~ 'pattern'          (case-sensitive)
-- WHERE column ~* 'pattern'         (case-insensitive)
-- WHERE column !~ 'pattern'         (NOT match)

-- ORACLE:
-- WHERE REGEXP_LIKE(column, 'pattern')

-- SQL SERVER:
-- No native regex (use LIKE or CLR functions)

-- ============================================================================
-- 15. TIPS FOR WRITING REGEX
-- ============================================================================

/*
1. Start simple, build complexity
   ✓ ^\d+$ (only digits)
   ✓ ^[0-9]+$ (only digits - same thing)
   ✓ ^[0-9]{5}$ (exactly 5 digits)

2. Use anchors for exact matching
   ✓ ^pattern$ (matches only this pattern)
   ✗ pattern (might match in middle of string)

3. Test incrementally
   - Test on small dataset first
   - Use LIMIT to see sample results

4. Escape special characters
   ✓ \. (literal dot)
   ✗ . (any character)

5. Use character classes
   ✓ [a-z] (any lowercase)
   ✗ [abcdefghijklmnopqrstuvwxyz]

6. Group when needed
   ✓ (abc){3} (abc repeated 3 times)
   ✗ abc{3} (only c repeated 3 times)
*/

-- ============================================================================
-- QUICK REFERENCE TABLE
-- ============================================================================

/*
Symbol   | Meaning                | Example
---------|------------------------|------------------
.        | Any character          | a.c matches abc, adc
*        | 0 or more             | ab*c matches ac, abc, abbc
+        | 1 or more             | ab+c matches abc, abbc (not ac)
?        | 0 or 1                | ab?c matches ac, abc (not abbc)
{n}      | Exactly n             | a{3} matches aaa
{n,m}    | Between n and m       | a{2,4} matches aa, aaa, aaaa
[abc]    | Any of a, b, c        | [abc]d matches ad, bd, cd
[^abc]   | Not a, b, or c        | [^abc]d matches ed, fd
[a-z]    | Range a to z          | [0-9] matches any digit
^        | Start of string       | ^abc matches abc at start
$        | End of string         | abc$ matches abc at end
|        | OR                     | ab|cd matches ab or cd
()       | Group                  | (ab)+ matches ab, abab
\d       | Any digit             | \d{5} matches 12345
\w       | Word character        | \w+ matches word123
\s       | Whitespace            | \s+ matches spaces
*/
