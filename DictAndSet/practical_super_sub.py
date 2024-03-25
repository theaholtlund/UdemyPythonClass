# Looking at a practical case for subsets and supersets
# First defining a list of skills required for a job posting
required_skills = ['python', 'github', 'linux']

# Define a dictionary with set values listing the potential candidates
candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

# Iterate over each candidate to see if they have all the required skills at a minimum
interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills): # This code just checks for a set
    if skills > set(required_skills): # This code checks for a proper superset, better if there are many candidates
        interviewees.add(candidate)

print(interviewees)
