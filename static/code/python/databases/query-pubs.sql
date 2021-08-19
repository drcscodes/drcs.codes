-- Simple selects
select * from author;

-- Simple joins
select * from pub cross join venue;
-- equivalent to:
-- select * from publication join venue;
-- select * from publication, venue;

-- Join ... on
select * from pub join venue on pub.venue_id = venue.venue_id;

-- Join ... using, natural join
select * from pub join venue using (venue_id);
select * from pub natural join venue;

-- Select headers
select title, year from pub join venue using (venue_id);

-- Joining multiple tables
select * from author join author_pub using (author_id) join pub using (pub_id);

-- Where clauses
select first_name, last_name, title
  from author join author_pub using (author_id) join pub using (pub_id)
  where last_name = 'Turing';

-- Like
select booktitle from venue where booktitle like 'Communications%';

-- Aggregate functions
-- Pub count by author
select author_id, last_name, count(author_id)
    from author join author_pub using (author_id) join pub using (pub_id)
    group by author_id;

-- Aliasing
-- Author with most pubs
select author_id, last_name, count(author_id) as pub_count
    from author join author_pub using (author_id) join pub using (pub_id)
    group by author_id
    order by pub_count desc
    limit 1;

-- All authors tied for most pubs
select last_name, pub_count
    from (select author_id, last_name, count(author_id) as pub_count
         from author join author_pub using (author_id) join pub using (pub_id)
         group by author_id
         order by pub_count desc);
