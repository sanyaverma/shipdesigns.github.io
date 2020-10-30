from flask import Flask, render_template 
import random
import termcolor


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
"help Snapchat cater to a more diverse audience while also maintaining the current user base?", 
"design an interface that gives car owners the ability to get information about their car from a remote location?", 
"design an interface that gives homeowners the ability to get information about their house, via IoT devices, from a remote location?", 
"design a platform for users to select a topic and pair them in a voice chat with someone else wanting to discuss the same topic?",
"write a How Might we Statement?"]
    randomseriousprompt = random.choice(seriousprompt)
    serious_hmw_prompt = randomseriousprompt
    return(serious_hmw_prompt)

if __name__ == "__main__":
    app.run(debug=True)