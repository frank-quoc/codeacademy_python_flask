-- This is the first query:

SELECT DISTINCT year from population_years;

-- Add your additional queries below:

-- 4: 1.54526 million
SELECT population
FROM population_years
WHERE country = 'Gabon'
ORDER BY population DESC
LIMIT 1;


-- 5: 
SELECT country
FROM population_years
WHERE year = 2005
ORDER BY population ASC
LIMIT 10;

-- 6: 
SELECT DISTINCT country
FROM population_years
WHERE population > 100
  AND year = 2010;

-- 7:
SELECT DISTINCT country
FROM population_years
WHERE country LIKE '%Islands%';

-- 8: 240.27152 - 214.67661 = 25.59491
SELECT year, population
FROM population_years
WHERE country = 'Indonesia'
  AND year = 2000
OR country = 'Indonesia'
  AND year = 2010;
