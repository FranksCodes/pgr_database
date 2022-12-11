SELECT Institution.name, Mean_Range.mean_range, ROUND(AVG(Overall.mean), 2) AS avg_mean, 
ROUND(mean_range.mean_range/AVG(Overall.mean)*100, 2) AS percent_fl, Region.region
FROM Institution JOIN Overall JOIN Mean_Range JOIN Region
ON Institution.id = Overall.institution_id AND Overall.region_id = Region.id 
 AND Institution.id = Mean_range.institution_id
GROUP BY Institution.name
HAVING COUNT(Overall.mean) > 1
ORDER BY Mean_Range.mean_range DESC, AVG(Overall.mean) DESC
