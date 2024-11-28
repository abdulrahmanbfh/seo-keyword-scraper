# SEO Keyword Scraper

This project scrapes SEO keywords from Google search results and serves them via a Django web server.
It will extract a csv file with the following info:
Keyword	Position	Title	Text	Date	Domain	URL	Intent


## How to Run

1. Clone the repository:
   git clone https://github.com/abdulrahmanbfh/seo-keyword-scraper/ cd seo-keyword-scraper

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Django server:
   python manage.py runserver

4. Access the endpoint:
   For example: http://127.0.0.1:8000/get_results/?query=python+web+scraping (Default max results: 100)
                 http://127.0.0.1:8000/get_results/?query=python+web+scraping&max_results=50


## For training the model:
  1. Modify the file: `env/keyword_intent_dataset.csv` with your phrases and its intent.
  2. Create the trained file: `python train_classifier.py`, it will create a file with name: `keyword_intent_model.pkl`

## Project Structure

- `scraper/`: Contains the web scraping logic.
- `webserver/`: Django project files.
- `app/`: Django app containing the web server logic.
- `env/`: Environment files

