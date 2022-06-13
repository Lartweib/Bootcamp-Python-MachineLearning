select avg(length), category.name from film f
join film_category cat
on f.film_id = cat.film_id
join category 
on cat.category_id = category.category_id
group by cat.category_id
order by cat.film_id;

select max(length) as "pelicula con mayor duracion", title from film;

select s.first_name, co.country, ci.city, a.address from staff s
join address a 
on a.address_id = s.address_id
join city ci
on ci.city_id = a.city_id
join country co
on co.country_id = ci.country_id;

select ci.city from country co
join city ci
on co.country_id = ci.country_id
where upper(co.country = "Spain");

select avg(length) as "media de duracion de peliculas pg" from film where upper(rating = "PG");

select f.title, cat.name from film f
join film_category fc
on f.film_id = fc.film_id
join category cat
on cat.category_id = fc.category_id;

select count(*) as "cantidad de peliculas", rating from film group by rating order by rating;

select cu.first_name, co.country, ci.city, a.address from customer cu
join address a 
on a.address_id = cu.address_id
join city ci
on ci.city_id = a.city_id
join country co
on co.country_id = ci.country_id;

select min(length) as "menor duracion", title from film;

select count(*) ;

select count(*) from film f, actor a, film_actor fa where f.film_id = fa.film_id and a.actor_id = fa.actor_id and a.first_name = "ED" and a.last_name="CHASE";

select a.first_name, a.last_name, f.title from film f
join film_actor fa
on fa.film_id = f.film_id
join actor a
on a.actor_id = fa.actor_id