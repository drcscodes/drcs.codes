CREATE TABLE house (
  house_name text primary key,
  sigil text not null,
  words text not null
);

CREATE TABLE character (
  character_name text not null,
  house_name text not null references house(house_name),
  primary key (character_name, house_name)
);
