SELECT COUNT(*) FROM birds;

SELECT COUNT(DISTINCT Scientific_Name)
FROM birds;

SELECT Common_Name,
COUNT(*)
FROM birds
GROUP BY Common_Name
ORDER BY COUNT(*) DESC
LIMIT 10;


SELECT COUNT(*) AS Total_Observations
FROM birds;

SELECT COUNT(DISTINCT Scientific_Name) AS Total_Species
FROM birds;

SELECT Common_Name,
COUNT(*) AS Observation_Count
FROM birds
GROUP BY Common_Name
ORDER BY Observation_Count DESC
LIMIT 10;

SELECT Common_Name,
COUNT(*) AS Observation_Count
FROM birds
GROUP BY Common_Name
ORDER BY Observation_Count DESC
LIMIT 10;

SELECT Habitat,
COUNT(DISTINCT Scientific_Name) AS Species_Count
FROM birds
GROUP BY Habitat;

SELECT Season,
COUNT(*) AS Observations
FROM birds
GROUP BY Season
ORDER BY Observations DESC;

SELECT Admin_Unit_Code,
COUNT(DISTINCT Scientific_Name) AS Species_Diversity
FROM birds
GROUP BY Admin_Unit_Code
ORDER BY Species_Diversity DESC;

SELECT COUNT(DISTINCT Scientific_Name) AS Watchlist_Species
FROM birds
WHERE PIF_Watchlist_Status = 1;

SELECT COUNT(DISTINCT Scientific_Name) AS Stewardship_Species
FROM birds
WHERE Regional_Stewardship_Status = 1;

SELECT Habitat,
AVG(Temperature) AS Avg_Temperature
FROM birds
GROUP BY Habitat;

SELECT Observer,
COUNT(*) AS Observation_Count
FROM birds
GROUP BY Observer
ORDER BY Observation_Count DESC
LIMIT 10;