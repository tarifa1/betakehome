# How to Use This App

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

# To Do
- Foreign keys! SQLAlchemy foreign key constraints were causing issues with dropping tables (not cascading) - have to debug that
- Filter events by posting_date: update filtering to be done via body params instead of url params i.e - request.args.get('posting_date'); add filtering by sql comparison operators (<,>,=, <=, >=) 
- Read db table data using SQLAlchemy instead of pandas.read_db 
- Move SQLAlchemy classes to models.py
- Move app routes to routes.py
- Add prod docker-compose, prod db env files
- Add nginx and gunicorn support for prod