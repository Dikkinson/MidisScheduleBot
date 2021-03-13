create schema db_schema;

create table Users_info
(
	user_id int null,
	user_group text null,
	subscribed bool null,
	username text null
);

create unique index Users_info_user_id_uindex
	on Users_info (user_id);

alter table Users_info
	add constraint Users_info_pk
		primary key (user_id);


create table Logs
(
	user_id int null,
	action text null,
	time datetime null,
	constraint Logs_Users_info_user_id_fk
		foreign key (user_id) references Users_info (user_id)
);