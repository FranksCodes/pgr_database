SELECT Institution.name, Overall.mean, Spread.spread, Year.year, Region.region 
FROM Institution JOIN Overall JOIN Year JOIN Region JOIN Spread
ON Institution.id = Overall.institution_id AND Overall.region_id = Region.id 
AND Overall.year_id = Year.id AND Institution.id = Spread.institution_id
WHERE Spread.spread > 0.6
ORDER BY Spread.spread DESC, Institution.name, year DESC
