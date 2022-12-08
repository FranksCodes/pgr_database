SELECT Institution.name, Overall.mean, Overall.overall_rank, Mean_Range.mean_range, Year.year, Region.region 
FROM Institution JOIN Overall JOIN Year JOIN Region JOIN Mean_Range
ON Institution.id = Overall.institution_id AND Overall.region_id = Region.id 
AND Overall.year_id = Year.id AND Institution.id = Mean_range.institution_id
WHERE Mean_Range.mean_range > 0.7
ORDER BY Mean_Range.mean_range DESC, Institution.name, year DESC
