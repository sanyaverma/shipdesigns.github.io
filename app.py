from flask import Flask, render_template 
from termcolor import colored
import random


app = Flask(__name__)

@app.route("/")
def Prompt():
    return render_template('Prompt.html')

@app.route("/serious", methods=["GET"])
def seriousprompt():
    seriousprompt= ["redesign the contraceptive buying experience for teenage girls to make it less stigmatizing?", "empower individuals to remain hopeful for a better future and promote well-being during COVID-19",
"improve the bill splitting process for college students to ensure no one is paying too much or too little?", 
"strengthen a college campus community by connecting mentors and mentees to help new students adjust to campus life?",
"increase accessibility to technology products and services and areas with poor internet access?",
"promote recycle reduce, and reuse habits to preschoolers to help build a sustainable future?", 
"help working adults prioritize healthy living habits including fitness and diet to reduce their risk of disease?", 
"help Snapchat cater to a more diverse audience while also maintaining the current user base?", "design a product that makes our users feel confident and secure during their online financial transactions?",
"design an interface that gives car owners the ability to get information about their car from a remote location?", 
"design an interface that gives homeowners the ability to get information about their house, via IoT devices, from a remote location?", 
"design a platform for users to select a topic and pair them in a voice chat with someone else wanting to discuss the same topic?",
"write a How Might we Statement?","design a product that helps users deposit their paycheques in three easy steps by using a guided workflow?", 
"get families in the community sharing babysitting resources?", "design the checkout flow for a liquor store's website?", "design a website for a company that makes websites?",
"build a product to make lottery games more accessible to players?", "create a platform for individuals to showcase and share their talents?", 
"redesign the ice-cream buying experience for kids so that it can be more portable and less messy?", "build a platform for students so that voter turnout increases at the next election?", "make group trip planning more collaborative"]
    randomseriousprompt = random.choice(seriousprompt)
    serious_hmw_prompt = randomseriousprompt
    return(serious_hmw_prompt)

@app.route("/fun", methods=["GET"])
def funprompt():
    actions = ["design ", "build ", "create ", "invent ", "make ", "modernize "]
    objects = ["a bed", "a printer", "shoes", "music player", "an ecosystem", "a new planet", "a coffee shop", "a tea flavor", "a bottle of wine", "a brand", "a marketing flyer", "keychain", "bag", "bicycle", "pillows", "watercolors", "stickers"]
    subjects = ["dragons", "a tent", "humans", "the elderly", "our society", "babies", "grandmothers", "a hotel in Spain", "plants", "your neighbor", "a play", "theatres around the world"]
    impact = ["solve world hunger", "turn dirt into clean water", "destroy earth", "start a tornado", "bring happiness", "fuck shit up", "you fuck it ship it"]
    fortext = [" for "] 
    to = [" to "]
    randomactions = random.choice(actions)
    randomobjects = random.choice(objects)
    randomsubjects = random.choice(subjects)
    randomimpact = random.choice(impact)
    randomfor = random.choice(fortext)
    randomto = random.choice(to)
    fun_hmw_prompt = randomactions + randomobjects + randomfor + randomsubjects + randomto + randomimpact + "?"
    return(fun_hmw_prompt)

if __name__ == "__main__":
    app.run(debug=True)