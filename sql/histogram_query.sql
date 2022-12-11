SELECT Mean_range.mean_range AS "Mean_Range", COUNT(Mean_range.mean_range) AS "Count"
FROM Mean_Range
WHERE Mean_range.institution_id IN 
	( SELECT Overall.institution_id FROM Overall JOIN Institution 
  ON Institution.id = Overall.institution_id AND Institution.id = Mean_range.institution_id 
  GROUP BY Overall.institution_id HAVING COUNT(Overall.mean) > 1)
GROUP BY Mean_range.mean_range
ORDER BY Mean_range.mean_range
