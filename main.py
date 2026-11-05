from db import run_query_select, run_update_query

ecomm = run_query_select("SELECT * FROM ecomm")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT avg(age) FROM ecomm")
for e in ecomm:
    print(e)

ecomm = run_query_select(" SELECT Gender, count(*) FROM ecomm GROUP by Gender")
for e in ecomm:
    print(e)

ecomm = run_query_select(" SELECT Gender, avg([Items Purchased]) FROM ecomm GROUP by Gender")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT count(*) FROM(SELECT [Membership Type] FROM ecomm GROUP by [Membership Type]) as T ")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT [Membership Type], count(*) FROM ecomm GROUP by [Membership Type]")
for e in ecomm:
    print(e)
    
ecomm = run_query_select("SELECT City, count(*) as number_customer FROM ecomm GROUP by City HAVING City like 'new york'")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT City, count(*) as number_customer FROM ecomm GROUP by City ORDER by number_customer DESC")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT Gender, sum([Total Spend]) FROM ecomm GROUP by Gender")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT [Customer ID], [Items Purchased] FROM ecomm ORDER by [Items Purchased] DESeLIMIT 1;")
for e in ecomm:
    print(e)

ecomm = run_query_select("SELECT [Customer ID], [Items Purchased] FROM ecomm ORDER by [Items Purchased]  LIMIT 1;")
for e in ecomm:
    print(e)




