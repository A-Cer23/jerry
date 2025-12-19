packages:
- fastapi 
- sqlmodel
- psycopg2
- pydantic-settings


TODO:
- introduce testing for high loads
    - [x] k6 to perform performance testing
    - [x] prometheus grabs results
    - grafana to dashboard prometheus