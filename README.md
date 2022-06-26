# marketplace_scraper
 - This is a scraper for the trendyol marketplace. You can get product details from the product page.

## Using Tools
 - Django
 - Virtualenv

## Dependencies used in the project
 - Python 3.7.2  
 - Virtualenv you can follow the instructions [here](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

## Clone the project
```
$ git clone https://github.com/eibrahimarisoy/marketplace_scraper.git
$ virtualenv venv
$ source venv/bin/activate
$ cd marketplace_scraper
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run the project
```
$ python manage.py runserver
```

## Usage
 - open the project in the browser and go to http://localhost:8000/admin/product/scraper/add/
 - paste the url of the product you want to get details from and click on the button "Save"
 - you will see the product details in the product details section(http://localhost:8000/admin/product/product/)

## Contact

If you want to contact me you can reach me at <eibrahimarisoy@gmail.com>.