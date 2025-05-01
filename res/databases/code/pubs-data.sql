use pubs;

insert into author values (1, "John", "McCarthy");
insert into author values (2, "Dennis", "Ritchie");
insert into author values (3, "Ken", "Thompson");
insert into author values (4, "Claude", "Shannon");
insert into author values (5, "Alan", "Turing");
insert into author values (6, "Alonzo", "Church");
insert into author values (7, "Perry", "White");
insert into author values (8, "Moshe", "Vardi");
insert into author values (9, "Roy", "Batty");


insert into book values(1, "Communications of the ACM", "April", 1960, 8);
insert into book values(2, "Communications of the ACM", "July", 1974, 8);
insert into book values(3, "Bell System Technical Journal", "July", 1948, 2);
insert into book values(4, "Proceedigns of the London Mathematical Society", "November", 1936, 7);
insert into book values(5, "Mind", "October", 1950, NULL);
insert into book values(6, "Annals of Mathematical Studies", "Month", 1941, NULL);
insert into book values(7, "AAAI", "July", 2012, 9);
insert into book values(8, "NIPS", "July", 2012, 9);

insert into pub values(1, "Recursive Functions of Symbolic Expressions and Their Computation by Machine",1);
insert into pub values(2, "The Unix Time-sharing System",2);
insert into pub values(3, "A Mathematical Theory of Communication", 3);
insert into pub values(4, "On computable numbers, with an application to the Entscheidungsproblem", 4);
insert into pub values(5, "Computing machinery and intelligence", 5);
insert into pub values(6, "The calculi of lambda-conversion", 6);

insert into author_pub values(1, 1, 1);
insert into author_pub values(2, 2, 1);
insert into author_pub values(3, 2, 2);
insert into author_pub values(4, 3, 1);
insert into author_pub values(5, 4, 1);
insert into author_pub values(5, 5, 1);
insert into author_pub values(6, 6, 1);
