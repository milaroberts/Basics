select * from voters;
select * from volunteers;
select * from volunteers v inner join vanid_eid van on v.eid = van.eid inner join voters vo on vo.vanid = van.vanid;
#Volunteers who are registered to vote
#select column_names(s) from table 1 inner join table 2 on table 1.column_names = table 2.column_names;#
#biggest table should be first and the smallest table should be last# 
#select column_name
select voters.lastname from voters FULL JOIN contacts on voters.vanid = contacts.vanidofcontacted;
	#full join
select dateofcontact, result from contacts left outer join voters on contacts.vanidofcontacted = voters.vanid;
#subqueries
select eid, vanid from vanid_eid where vanid in (select vanid from voters where firstname like 'Jo%');
	#vanid of everyone named jo%
	#subquery because its a second request inside of a request
#create table newtable as 
	#select id (int), firstname(var), etc. 
create table demo1 as
	(select firstname, lastname from volunteers);
	#creates a new table
select count(distinct volunteers.lastname) from volunteers;

select min(age), vaddress from voters group by vaddress ??

select * from voters where datereg between "2008-11-08" and "2015-11-08"; 

select firstname, lastname, vanid from voters join (select count(contactid), contacts.vanidofcontacted, contacts.dateofcontact from contacts group by contacts.dateofcontact) x on voters.vanid = contacts.vanidofcontacted;
