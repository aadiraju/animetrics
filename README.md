[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=311731&assignment_repo_type=GroupAssignmentRepo)
# Group 100 - A WorldWide Canvas

- Your title can change over time.

## Milestones

Details for Milestone are available on Canvas (left sidebar, Course Project) or [here](https://firas.moosvi.com/courses/data301/project/milestone01.html).

## Describe your topic/interest in about 150-200 words

After playing **"Quick, Draw!"** a few times, it became clear to me that it was a Data Scientist's _Pot of Gold at the end of the rainbow_. I can't help but be excited to see exactly the kind of insights I can gain into the collective perception of the masses. _Do Americans draw circles clockwise, or anti-clockwise? Which country draws the best representation of the Mona Lisa?_ These are the types of questions I wish to tackle with my analysis. However, I must also acknowledge that this study will have to be limited to a select few of the wide array of categories in the dataset, as doing more than that will be nothing short of excruciatingly difficult.  

## Describe your dataset in about 150-200 words

The **"Quick, Draw!"** dataset contains *millions of user-submitted drawings across over 300 categories*. These drawings were collected through the Google game, **"Quick, Draw!"** where a player is given a word to draw and has a limited amount of time to draw it and see how fast the Nueral Network can recognize their drawing. The drawings are stored in the dataset as vectors made up of a collection of end points. Each record in the dataset has the following fields:
* A unique ID (**key_id**)
* The prompt the user was given (**word**) 
* Whether their drawing was recognized by the system (**recognized**)
* A timestamp of when the drawing was made (**timestamp**) 
* The country of the user who drew the doodle (**countrycode**)
* The actual vector they drew (**drawing**).

In this project, I will be using the Binary files (`.bin`), located in `data/raw`([here](data/raw)) for my analysis, which are of the format `full_binary_CATEGORY_NAME.bin`, where `CATEGORY_NAME` is replaced with the prompt the user was provided for the drawing.

## Team Members

- Abhineeth: 3rd year CS major very interested in practical applications of Data Science

## References
[Quick, Draw! Dataset provided by Google](https://github.com/googlecreativelab/quickdraw-dataset)

