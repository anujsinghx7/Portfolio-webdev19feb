from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client('portfolio')
app=Flask(__name__)
@app route('/')
def home():
    return render_template('index')