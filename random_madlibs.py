from sample_madlibs import code, hp, hungergames, zombie 
import random

if __name__ == "__main__":
    m = random.choice([hp, hungergames, zombie, code])
    m.madlib()