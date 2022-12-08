SELECT Institution.name, Overall.mean, Overall.geo_rank, Overall.overall_rank, Year.year, Region.region 
FROM Institution JOIN Overall JOIN Year JOIN Region 
ON Institution.id = Overall.institution_id AND Overall.region_id = Region.id AND Overall.year_id = Year.id
