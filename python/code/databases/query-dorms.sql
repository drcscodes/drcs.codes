-- What are the names of all the dorms?
select name from dorm;

-- What is the total capacity (number of spaces) for all dorms?
select sum(spaces) from dorm;

-- Which students are in Armstrong?
select stud.name from dorm join stud using (dorm_id)
    where dorm.name = 'Armstrong';

-- Which student has the highest GPA?
select name from stud order by gpa desc limit 1;

-- Which dorm has the most students?
select dorm.name, count(dorm_id) as stud_count
  from dorm join stud using (dorm_id)
  group by dorm_id
  order by stud_count desc
  limit 1;

-- Which dorm’s students have the highest average GPA?
select dorm.name, sum(gpa)/count(dorm_id) as avg_gpa
  from dorm join stud using (dorm_id)
  group by dorm_id
  order by avg_gpa desc
  limit 1;
