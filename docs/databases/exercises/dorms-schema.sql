drop database if exists dorms;
create database dorms;
use dorms;

drop table if exists dorm;
create table dorm (
    dorm_id integer primary key auto_increment,
    name text,
    spaces integer
);

drop table if exists stud;
create table stud (
    stud_id integer primary key auto_increment,
    name text,
    gpa float,
    dorm_id integer references dorm(dorm_id)
);
