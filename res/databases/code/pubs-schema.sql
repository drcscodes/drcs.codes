drop database if exists pubs;
create database pubs;
use pubs;

create table if not exists author (
  author_id integer primary key auto_increment,
  first_name text not null check(first_name != ''),
  last_name text not null check(last_name != '')
);

create table if not exists book (
  book_id integer primary key auto_increment,
  title text not null not null check(title != ''),
  month text not null check(month != ''),
  year integer not null,
  editor integer references author(author_id)
);

create table if not exists pub (
  pub_id integer primary key auto_increment,
  title text not null check(title != ''),
  book_id integer not null references book(book_id)
);

create table if not exists author_pub (
  author_id integer not null references author(author_id),
  pub_id integer not null references pub(pub_id),
  author_position integer not null, -- first author, second, etc?

  primary key (author_id, pub_id)
);
