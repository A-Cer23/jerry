packages:
- fastapi 
- sqlmodel
- psycopg2
- pydantic-settings


K6 MILESTONES:
- [x] 10 concurrent users
- [] 100 concurrent users
- [] 1000 concnurrent users
- [] 10 000 concurrent users
- [] 100 000 concurrent users
- [] 1 000 000 concurrent users

TODO:
- [x] k6 to perform performance testing
- [x] create prometheus to grabs k6 results
- [x] create grafana to dashboard prometheus
- [] pass 100 cocurrent users
- [] introduce post requests in k6 testing

low priorirty:
- [] add prometheus data source for grafana without the need of creating it through ui
- [] add default dashboard to grafana without having to import it through ui
- [] prometheus receives multiple data from r6 like count,sum,min,max,avg,med,p(95),p(90),p(99) instead of just p(99)
