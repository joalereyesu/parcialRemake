from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

def reverseString (x):
    return x[:: -1]

def vowelsORconsonant (x, vORc):
  numberVowels = 0
  vowels = "aAeEiIoOuU"
  consonants = 0
  for elements in vowels:
      for letters in x:
          if (elements == letters):
              numberVowels = numberVowels + 1

  if (vORc):
      return numberVowels
  else: 
      consonants = len(x) - numberVowels
      return consonants

def UpDown (x):
    newWord = ' '
    for index in range(len(x)):
        if ((index % 2) == 0):
            newWord += (x[index].upper())
        else:
            newWord += (x[index].lower())
    return newWord

def naive (x):
    str_list = list(x)
    for index in range(len(str_list)):
        if ("a" == x[index].lower()):
            str_list[index] = "@"
        elif ("e" == x[index].lower()):
            str_list[index] = "3"
        elif ("i" == x[index].lower()):
            str_list[index] = "!"
        elif ("o" == x[index].lower()):
            str_list[index] = "0"
        elif ("u" == x[index].lower()):
            str_list[index] = ")"
    newStr = "".join(str_list)
    return newStr

def dic (word: str)-> Dict:
    dic = {}
    if word == "":
        return dic
    dic['String'] = word
    dic['Reversed'] = reverseString(word)
    dic['Length'] = len(word)
    dic['Number of vowels'] = vowelsORconsonant(word, True)
    dic['Number of consonants'] = vowelsORconsonant(word, False)
    dic['Upper'] = word.upper()
    dic['Lower'] = word.lower()
    dic['UpDown'] = UpDown(word)
    dic['Naive'] = naive(word)
    return dic

#@app.route("/")
#def home():
    #return render_template("string.html")

@app.route("/", methods=["GET", "POST"])
def crear():
    _string = request.args.get("texto", "")
    modified = dic(_string)
    return render_template("string.html", modified = modified)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)