--Write a Query that selects big countries from the table WORLD
--a country is a big country if its area is at least 3000000km^2 or it population is at least 25000000

SELECT name, population, area FROM World
WHERE (area >= 3000000) OR (population >= 25000000)