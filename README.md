# ECO375-Project-Phase2
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16043289)
![This Github repository is based on v2.0.2 of the data-analytics-module-2 repository.](https://img.shields.io/badge/data--analytics--module--2-v2.0.2-brightgreen)

> **ECO375** Applied Econometrics, *University of Toronto*
> 
> Prof. Courtney Ward

# Introduction to Reproducible Research

The life of an empirical researcher involves many hours spent coding: writing code, running code, and cursing our code for its failure to produce the results we expected. Sometimes that failure is inevitable—the data does not always agree with our expectations. But too often our code fails to reproduce the results we had previously generated. Or, worse...the code fails to reproduce the results that have already been published.

One of the objectives of this course is to teach you how to create reproducible research from day one of your project. These skills might seem like a burden when working alone on projects that will last only days or a few weeks. But they are essential skills for collaborating on teams and producing accurate work. They are also highly valuable on the job market—whether you plan to work in the private sector, in academic research, in nonprofits or in government.

# 🐣 Getting Started

▶️ You can [watch a video tutorial](https://www.loom.com/share/8728bbb1245a465887176cd658179b65?sid=696fe97a-ce53-4f67-a297-fe0f0444d35f) that walks through how to use Github and submit your assignment. Use the video chapters to jump straight to a specific section.

Alternatively, follow these written step-by-step instructions with screenshots:

1. **Configure your Stata license in Github** by following the [instructions in this guide](https://github.com/UofT-Econ-DataAnalytics/files/wiki/Stata-License).

    - ⚠️ You must have [purchased a Stata license](https://www.stata.com/order/new/edu/profplus/student-pricing/). The lowest cost option is a 6-month student license, which costs US$48.

2. **Launch a Github Codespace and open Stata in your browser** by following the [instructions in this guide](https://github.com/UofT-Econ-DataAnalytics/files/wiki/Launch-Codespace:-Stata).

    - Working online using Github Codespaces means you can write and run your code on any computer—either in your browser, or using the Visual Studio Code application. No matter what computer you're using, Codespaces provides a computing environment where all the software you need is already set up and configured. And since it's configured identically for all students, it is much easier to troubleshoot issues you encounter with your classmates, with your TAs, or with your professor.

    - ⚠️ If you're using Firefox or Safari as your browser, [see these notes](https://github.com/UofT-Econ-DataAnalytics/files/wiki/%E2%98%81%EF%B8%8F-Online:-Stata#github-codespaces-is-buggy-in-your-browser).

3. **Commit your code and check your results** by following the [instructions in this guide](https://github.com/UofT-Econ-DataAnalytics/files/wiki/Submissions).

    - ℹ️ You can find out immediately whether your code ran successfully and whether your answers are correct.

### 🛠️ Advice and Troubleshooting

- We recommend writing your code as a Stata **script** (a file that ends in `.do`). A script is a plain text file containing your code and comments.

    - If you are already comfortable with **Jupyter notebooks** (a file that ends in `.ipynb`), you can write your Stata code in a notebook if you prefer. You can modify the code and execute your code in the VS Code window in your browser, and see the results displayed in the same notebook.

- For more detailed guidance and troubleshooting advice for common issues, check the [troubleshooting guide](https://github.com/UofT-Econ-DataAnalytics/files/wiki/%E2%98%81%EF%B8%8F-Online:-Stata). *This guide will be updated throughout the semester in response to questions and feedback from students.*

### 🔎 Example Code

There is example code saved in this repository, which completes a task very similar to the tasks you will be doing in this assignment. These examples could guide you if there are steps you're not sure how to do (ex: outputting your results as a YAML file).

- See [example_script_Stata.do](example_script_Stata.do) for an example script.

- See [example_notebook_Stata.ipynb](example_notebook_Stata.ipynb) for an example Jupyter notebook.

# ➡️ Submitting your work

* **You must save your code in Github, in a file named `submission.do`** located in the root directory of the repository (not in a subfolder).
    - If you're submitting a Jupyter Notebook instead of a script, you will save **`submission.ipynb`** instead.

* Your code must output its estimates in a YAML file named `results/module2.yaml`.
    - **This YAML file will not be committed to the Github repository.** You will NOT see it in the Github website within the [`results`](/results) folder.
        - The YAML file will be visible in your Github Codespace.
    - When you submit your *code* by committing it to Github, your *results* will be automatically recalculated by running your code.
        - You can [check your results](https://github.com/UofT-Econ-DataAnalytics/files/wiki/Submissions) to see if your code ran successfully and if you got the right answers.
    - Each time a question asks you to output a number, it is marked with (&#8288;🔢&#8288;→&#8288;`name_of_estimate`&#8288;)
    - The YAML file will look like this, but with the right numbers. The order doesn't matter.
        ```yaml
        avg_test_score: 123
        avg_student_teacher_ratio: 456
        gap_test_score: 7.89
        gap_student_teacher_ratio: 5.67
        ols_slope: 0.123
        ols_constant: 0.456
        ```

# 🧑‍💻 Tasks to Complete

1. Load the data from the California Test Score Dataset (named `caschool`).

    - This data is automatically available in your Github Codespace in `data/raw`. This folder contains the data in three formats: `.csv`, `.xlsx`, `.dta`. Data files that have been saved in Stata format carry the extension `.dta`. The Week 1 Stata Tutorial shows you how to import data in all three versions. To simply things here, we recommend loading the `caschool.dta` in Stata format directly using the `use` command as we did on the Week 1 Lecture Slides.

    - A description of the data is given in the pdf document included in the folder: `CaliforniaTestScores.pdf`
    
    - Throughout this assignment, we will ask you to work with two variables: `testscr` and `str`.

2. Calculate the average test score in this sample of districts (&#8288;🔢&#8288;→&#8288;`avg_test_score`&#8288;). Calculate the average students per teacher in this sample (&#8288;🔢&#8288;→&#8288;`avg_student_teacher_ratio`&#8288;).

3. How many points higher is the test score in the 90th percentile relative to districts in the 10th percentile (&#8288;🔢&#8288;→&#8288;`gap_test_score`&#8288;)? What about the student teacher ratio 90th percentile, relative to districts in the 10th percentile? (&#8288;🔢&#8288;→&#8288;`gap_student_teacher_ratio`&#8288;)?

4. Using an OLS linear regression, estimate the increase in test score associated with one more student-per-teacher (&#8288;🔢&#8288;→&#8288;`ols_slope`&#8288;). What is the estimated constant in the model? (&#8288;🔢&#8288;→&#8288;`ols_constant`&#8288;).
