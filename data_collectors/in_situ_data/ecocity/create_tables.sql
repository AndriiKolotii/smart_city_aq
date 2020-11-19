create table ecocity_data
(
    Station_ID varchar(100),
    cityName varchar(100),
    localName varchar(100),
    latitude float not null,
    longitude float not null,
    timezone varchar (50) not null,
    pol varchar(50) not null,
    unit varchar(50) not null,
    time timestamp not null,
    value float not null,
    averaging varchar(50) not null)
;