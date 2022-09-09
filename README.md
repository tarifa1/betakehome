#How to Use This App

- From the top level directory, run `docker-compose up -d --build`
- To create databases, run `docker-compose exec web python manage.py create_db`
- To seed databases, run `docker-compose exec web python manage.py seed_db`

- /events route are filterable by `posting_date`, add `/YYYY-MM-DD` to the url path to filter by the posting_date
    - Examples:
        - `/events/2021-08-18`
- /waybill routes can be filtered by `waybill_id`, add `/id` to the url path to filter by waybill id
    - Examples:
        - `/waybills/7`
        - `/waybills/6/equipment`   