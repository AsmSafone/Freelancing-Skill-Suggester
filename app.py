# ------------------------------------------ #
#
# Title: Freelancing Skill Suggester
# Description: A simple Python program that suggests freelancing skills based on user's passion.
# Author: A.S.M Arsad Ahamed Safone (AsmSafone)
# License: GNU General Public License v3.0
#
# ------------------------------------------ #


import random

# Define a dictionary of freelancing skills categorized by passion
passions = {
    "tech": ["Web Development", "Mobile App Development", "Data Science", "Cybersecurity"],
    "creative": ["Graphic Design", "Digital Marketing", "Content Writing", "UI/UX Design"],
    "business": ["Management Consulting", "Financial Analysis", "Human Resources", "Operations Management"],
    "health": ["Medical Writing", "Health Coaching", "Nutrition Consulting", "Wellness Coaching"],
    "education": ["Online Tutoring", "Course Creation", "Education Consulting", "Academic Writing"],
    "cognitive": ["Memory Improvement", "Attention Enhancement", "Logical Thinking", "Speed of Thought"],
    "behavioral": ["Communication Skills", "Team Management", "Time Management", "Adaptability"],
    "technical": ["Programming Languages", "Software Development", "Data Analysis", "IT Project Management"],
    "sector": ["Financial Services", "Healthcare", "Education", "Technology"]
}

def main():
    '''Receive input from user to suggest freelancing skills'''
    while True:
        print("Welcome to the freelancing skill suggester!")
        passion = input("What is your passion? (tech, creative, business, health, education, cognitive, behavioral, technical, sector): ")
        if passion not in passions:
            print("Invalid passion. Please try again!")
            continue
        num_skills = int(input("How many skills would you like to suggest? (1, 2, or 3): "))
        if num_skills < 1 or num_skills > 3:
            print("Number must be from 1 to 3. Please try again!")
            continue
        suggest_skills(passion, num_skills)
        print("")

def suggest_skills(passion, num_skills):
    '''Suggest freelancing skills based on user passion'''
    skills = passions[passion]
    random_skills = random.sample(skills, num_skills)
    print("Based on your passion for " + passion + ", here are " + str(num_skills) + " freelancing skills you might enjoy:")
    for skill in random_skills:
        print(skill)

if __name__ == '__main__':
    main()
