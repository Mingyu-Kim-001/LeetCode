import os
from os.path import join,isdir
import pandas as pd
problem_types = []
problem_difficulty = ["easy","medium","hard"]
counter = pd.DataFrame(index=problem_difficulty+["total"])
for problem_type in os.listdir():
    if isdir(problem_type) and problem_type[0]!=".":
        problem_types.append(problem_type)
        counter[problem_type] = [0,0,0,0]
        for difficulty in problem_difficulty:
            if difficulty in os.listdir(join(os.getcwd(),problem_type)):
                for problem in os.listdir(join(os.getcwd(),problem_type,difficulty)):
                    if problem[0]!=".":
                        counter[problem_type][difficulty]+=1
counter["total"] = counter.sum(axis=1)
counter.loc["total",:] = counter.sum(axis=0)
mdTable = counter.to_markdown()

with open("problem_worth_resolve.md","r") as resolve, open("README.md", "w") as readme:
    readme.write("# LeetCode\nProblems solved\n\n"+mdTable+"\n\n"+resolve.read())