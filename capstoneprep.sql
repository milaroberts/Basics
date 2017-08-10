#how many supporters (1s, 2s) you have by zip code
#join, count, group by
create table votersresult as
	(select * from voters vo inner join contacts con on vo.vanid = con.vanidofcontacted);
select zip5, count(result) from votersresult where result like '1%' or result like '2%' group by zip5 order by count desc limit 20;
select vanid from public.voters where zip5 in (select x.zip5 from (select zip5, count(result) from votersresult where result like '1%' or result like '2%' group by zip5 order by count desc limit 20) x
);
