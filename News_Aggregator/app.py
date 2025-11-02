# import feedparser library
import feedparser

# import datetime module for working with dates
from datetime import datetime

# write Article class to shape a single Article
class Article:
    def __init__(self, headline: str, summary: str, published: datetime, url: str):
        self._headline = headline
        self._summary = summary
        self._published = published
        self._url = url

    # getting the headline of single article
    def get_headline(self) -> str:
        return self._headline
    
    # getting the summary of single article
    def get_summary(self) -> str:
        return self._summary
    
    # getting the published date of single article
    def get_published(self) -> datetime:
        return self._published
    
    # getting the url of single article
    def get_url(self) -> str:
        return self._url
    
# function for checking if the given word (case-insensitive) appears in the article's headline.
def headline_contains(article, word: str) -> bool:
    if not word:
        return False
    return word.lower() in article.get_headline().lower()

# function for checking if the given word (case-insensitive) appears in the article's summary
def summary_contains(article, word: str) -> bool:
    if not word:
        return False
    return word.lower() in article.get_summary().lower()

# function for checking if the article was published after the given date
def published_after(article, date_str: str) -> bool:
    """The date_str must be in the format: "DD Mon YYYY HH:MM:SS"
    Example: "30 Oct 2025 12:00:00"""
    try:
        given_date = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")
    except ValueError:
        raise ValueError("Date must be in format 'DD Mon YYYY HH:MM:SS'")

    return article.get_published() > given_date

# the main program for fetching articles and making articles
def main():
    FEED_URL = "http://news.google.com/?output=rss"
    print(f"Fetching articles from {FEED_URL} ...")
    feed = feedparser.parse(FEED_URL)

     #Convert each entry into an Article object
    articles = []
    for entry in feed.entries:
        # Use current time if published date is missing
        if hasattr(entry, "published_parsed"):
            published = datetime(*entry.published_parsed[:6])
        else:
            published = datetime.now()

        headline = entry.title
        summary = getattr(entry, "summary", "")
        url = entry.link

        article = Article(headline, summary, published, url)
        articles.append(article)

     #Ask user for keyword and date
    keyword = input("Enter keyword (e.g. 'UEA'): ").strip()
    date_str = input("Enter date (format: 'DD Mon YYYY HH:MM:SS'): ").strip()

    #Apply filters
    filtered_articles = [
        a for a in articles
        if (headline_contains(a, keyword) or summary_contains(a, keyword))
        and published_after(a, date_str)
    ]

    # print the filtered articles
    for article in filtered_articles:
        print(f"[{article.get_published().strftime('%Y-%m-%d %H:%M')}] {article.get_headline()}")
        print(article.get_url())
        print('Student ID - 100536294')

main()

# First of all, I use one external library called feedparser for parsing the articles. I install it using pip with the following command: pip install feedparser. I also use the built-in datetime module, which does not require any external installation.

# I wrote this program according to the instructions given to me, starting simply by creating a class and defining object properties with getter methods for each attribute. This is a part of the code where I can code freely without hesitation because I have the flexibility to implement it in my own way without restrictions. For example, in the beginning, I had to handle errors without using try-except, among other requirements. However, I used most of the methods and properties provided by the language. I faced no difficulties while writing the program.