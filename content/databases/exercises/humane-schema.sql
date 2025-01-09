drop database if exists humane;
create database humane;
use humane;

-- All workers, including employees and volunteers
create table worker (
  worker_id int primary key auto_increment,
  name varchar(10) not null
);

-- A worker who is an employee (not a volunteer) will be in this table.
create table emp (
  emp_id int primary key,
  salary int not null,

  foreign key (emp_id) references worker(worker_id)
);

create table shelter (
  shelter_id int primary key,
  name varchar(16) not null,
  manager_id int,

  foreign key (manager_id) references emp(emp_id)
);

-- A worker can work at many shelters, a shleter can have many workers.
create table shelter_worker (
  shelter_id int,
  worker_id int,

  primary key (shelter_id, worker_id),
  foreign key (shelter_id) references shelter(shelter_id),
  foreign key (worker_id) references worker(worker_id)
);

create table work_days (
  shelter_id int,
  worker_id int,
  week_day enum('M', 'T', 'W', 'R', 'F', 'S', 'U'),
  start_time time,
  end_time time,

  primary key (shelter_id, worker_id, week_day, start_time, end_time),
  foreign key (shelter_id) references shelter(shelter_id),
  foreign key (worker_id) references worker(worker_id)
);

create table pet (
  shelter_id int not null,
  pet_id int not null,
  name varchar(10) not null,
  breed varchar(10) not null,

  primary key (shelter_id, pet_id),
  foreign key (shelter_id) references shelter(shelter_id)
);
