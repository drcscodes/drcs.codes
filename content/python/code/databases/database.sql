create table if not exists author (
  author_id integer primary key,
  first_name text,
  last_name text
);

create table if not exists publication (
  pub_id integer primary key,
  title text
  
  
);

create table if not exists venue (
  venue_id integer primary key,
  booktitle text not null,
  month text,
  year integer not null
);

