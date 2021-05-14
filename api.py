from flask import Flask, flash, request, redirect, url_for, render_template

app = Flask(__name__)
app.config["Debug"] = True

@app.route('/')
def homepage():
   return "Hi"

if __name__ == "__main__":
	app.run()
