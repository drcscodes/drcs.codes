use humane;

insert into worker values (1, "Tom");
insert into worker values (2, "Jie");
insert into worker values (3, "Ravi");
insert into worker values (4, "Alice");
insert into worker values (5, "Aparna");
insert into worker values (6, "Bob");
insert into worker values (7, "Xaoxi");
insert into worker values (8, "Rohan");

insert into emp values (1, 500000);
insert into emp values (2, 30000);
insert into emp values (3, 20000);
insert into emp values (5, 1000000);
insert into emp values (6, 40000);
insert into emp values (7, 50000);

insert into shelter values (1, "Howell Mill", 1);
insert into shelter values (2, "Mansell", 5);

insert into shelter_worker values (1, 1);
insert into shelter_worker values (1, 2);
insert into shelter_worker values (1, 3);
insert into shelter_worker values (1, 4);
insert into shelter_worker values (2, 5);
insert into shelter_worker values (2, 6);
insert into shelter_worker values (2, 7);
insert into shelter_worker values (2, 8);

insert into work_days values (1, 1, 'M', '08:00', '12:00');
insert into work_days values (1, 1, 'M', '13:00', '17:00');
insert into work_days values (1, 1, 'T', '08:00', '12:00');
insert into work_days values (1, 1, 'T', '13:00', '17:00');
insert into work_days values (1, 1, 'W', '08:00', '12:00');
insert into work_days values (1, 1, 'W', '13:00', '17:00');
insert into work_days values (1, 1, 'R', '08:00', '12:00');
insert into work_days values (1, 1, 'R', '13:00', '17:00');
insert into work_days values (1, 1, 'F', '08:00', '12:00');
insert into work_days values (1, 1, 'F', '13:00', '17:00');
insert into work_days values (1, 2, 'M', '08:00', '12:00');
insert into work_days values (1, 2, 'W', '08:00', '12:00');
insert into work_days values (1, 2, 'F', '08:00', '12:00');
insert into work_days values (1, 3, 'M', '13:00', '17:00');
insert into work_days values (1, 3, 'W', '13:00', '17:00');
insert into work_days values (1, 3, 'F', '13:00', '17:00');
insert into work_days values (1, 4, 'T', '08:00', '17:00');
insert into work_days values (1, 4, 'R', '08:00', '17:00');
insert into work_days values (2, 5, 'M', '08:00', '17:00');
insert into work_days values (2, 5, 'T', '08:00', '17:00');
insert into work_days values (2, 5, 'W', '08:00', '17:00');
insert into work_days values (2, 5, 'R', '08:00', '17:00');
insert into work_days values (2, 5, 'F', '08:00', '17:00');
insert into work_days values (2, 5, 'S', '08:00', '17:00');
insert into work_days values (2, 6, 'S', '08:00', '17:00');
insert into work_days values (2, 6, 'U', '08:00', '17:00');
insert into work_days values (2, 7, 'S', '08:00', '17:00');
insert into work_days values (2, 8, 'U', '08:00', '17:00');

insert into pet values (1, 1, "Chloe", "Mix");
insert into pet values (1, 2, "Dante", "GSD");
insert into pet values (1, 3, "Heidi", "Dachshund");
insert into pet values (2, 1, "Bailey", "Mix");
insert into pet values (2, 2, "Sophie", "Lab");
insert into pet values (2, 3, "Heidi", "Dachshund");
