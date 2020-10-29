import random

#Fun How Might We statements 

actions = ["design ", "build ", "create ", "invent ", "make "]
objects = ["a bed", "an ice cream cone", "shoes", "music player", "an ecosystem", "a new planet", "a coffee shop", "a new tea flavor", "a bottle of wine", "the Shift house"]
subjects = ["dragons", "a tent", "humans", "Ria Bazaz", "our society", "babies", "my grandmother"]
impact = ["solve world hunger", "turn dirt into clean water", 
"destroy earth", "cause a tornado", "bring you happiness", "make your dog wine", "to reduce the mess it makes", "help Ria get drunk", "fuck it ship it"]

randomactions = random.choice(actions)
randomobjects = random.choice(objects)
randomsubjects = random.choice(subjects)
randomimpact = random.choice(impact)

fun_hmw_prompt = "How might we " + randomactions + randomobjects + " for " + randomsubjects + " to " + randomimpact + "?"

print(fun_hmw_prompt)

#Serious How Might We statements 
seriousprompt= ["redesign the contraceptive buying experience for teenage girls to make it less stigmatizing?", "empower individuals to remain hopeful and build better online communities that promote well-being, provide people with daily structure, and give them hope for a better future?",
"improve the bill splitting process for college students to ensure no one is paying too much or too little?", 
"strengthen a college campus community by connecting mentors and mentees to help new students adjust to campus life?",
"increase accessibility to technology products and services and areas with poor internet access?",
"promote recycle reduce, and reuse habits to preschoolers to help build a sustainable future?", 
"help working adults prioritize healthy living habits including fitness and diet to reduce their risk of disease?", 
"help Snapchat cater to a more diverse audience while also maintaining the current user base?", 
"design an interface that gives car owners the ability to get information about their car from a remote location?", 
"design an interface that gives homeowners the ability to get information about their house, via IoT devices, from a remote location?", 
"design a platform for users to select a topic and pair them in a voice chat with someone else wanting to discuss the same topic?"
"write a How Might we Statement?"]

randomseriousprompt = random.choice(seriousprompt)
serious_hmw_prompt = "How might we " + randomseriousprompt
print(serious_hmw_prompt)