from flask import Blueprint, render_template

blueprint = Blueprint('public', __name__)

# Books list content
content = """
### 2019 (Age 27-28)
* Never Split the Difference (Kindle)

### 2018 (Age 26-27)
* Men Are from Mars, Women Are from Venus (Kindle)
* Advanced Sports Nutrition (Kindle)
* Principles: Life and Work (Kindle)
* Generations (Kindle)
* Love in a Time of Cholera (Kindle)
* On the Road: Original Scroll (Kindle)
* Homo Sapiens (Kindle)

### 2017 (Age 25-26)
* For Young Men Only (Kindle)
* Ready Player One (Audible)
* The Undoing Project (Audible)
* East of Eden (Audible)

### 2016 (Age 24-25)
* 48 Laws of Power (Audible)
* The Alchemist (Audible)
* Lolita (Audible)
* Picture of Dorian Gray (Audible)
* Delivering Happiness (Audible)
* The Bhagavad Gita (Audible)
* Elon Musk (Kindle)
* Anna Karenina (Audible)
* The Unbearable Lightness of Being (Audible)
* The Kite Runner (Audible)
* Man's Search for Meaning (Audible)

### 2015 (Age 23-24)
* Three Comrades (Kindle)
* Golden Compass (Kindle)
* Brave New World (Kindle)
* Perennial Philosophy (Kindle)
* Wrinkle in Time (Kindle)
* The Wind in the Willows (Kindle)
* Looking for Alaska (Kindle)
* Paper Towns (Kindle)
* Divergent Trilogy (All three) (Kindle)
* A History of the World in Six Glasses (Kindle)
* Introduction to Tornado

### 2014 (Age 22-23)
* Tao: The Watercourse Way
* Journey to the East
* Peter Camenzind
* The Game
* Pragmatic Programmer
* PeopleWare
* The Young Lions
* The Red Queen
* Zero to One
* The Hard Thing About Hard Things
* JavaScript The Good Parts
* Test-Driven Python Development

### 2013 (Age 21-22)
* The Catcher in the Rye
* Pride and Prejudice (2/3)
* The Perks of Being a Wallflower
* 1984
* Animal Farm
* Siddhartha
* Demian
* Narcissus and Goldmund (1/2)
* The Story of Philosophy
* Steppenwolf

### 2012 (Age 20-21)
* Getting Things Done
* The 7 Habits of Highly Effective People
* The  Way of Zen
* Mindless Eating
* Eat, Drink, and Be Healthy

### 2011 (Age 19-20)
* How to Win Friends and Influence People
* The New New Thing
* Ahead of the Curve
* The Dip
* Autobiography of Benjamin Franklin
* The Big Short
* When Genius Failed

### 2010 (Age 18-19)
* My Life as a Quant
* Goldman Sachs: The Culture of Success
* Den of Thieves
* Liar's Poker
* Liquidated: An Ethnography of Wall Street
* Reminiscences of a Stock Operator
* Fortune's Formula
* Working the Street
* The Millionaire Next Door
* The Richest Man in Babylon
* Rich Dad Poor Dad
* Fooled by Randomness
* Where are the Customers' Yachts
* The Investment Answer
"""

@blueprint.route('/', methods=['GET'])
def welcome():
    return render_template("public/welcome.tmpl")

@blueprint.route('/books', methods=['GET'])
def books():
    return render_template("public/books.tmpl", content=content)
