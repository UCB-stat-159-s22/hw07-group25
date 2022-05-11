## Data analysis of NIH funding by spending category

**Binder:**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw07-group25.git/main)

**JupyterBook Link:**

Our JupyterBook can be found at the following link: https://ucb-stat-159-s22.github.io/hw07-group25/

**Note:** This repository is public so that Binder can find it. All data is based on the original [Estimates of Funding for Various Research, Condition, and Disease Categories (RCDC)](https://report.nih.gov/funding/categorical-spending#/). This repository is a class exercise that develops a complete analysis of a dataset that can be found online, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original data rests with NIH.


We started with a dataset containing information of the number of millions of dollars that was spent for different categories of health related research over the years. We aimed to explore the following questions:
1) What are the top 10 spending categories in 2019? 
2) What spending categories have increased/decreased the most during the years that data is available in 2019? 
3) What is the relationship between mortality rates and funding by category in 2019? 


Our analysis includes various components:

- The data folder contains both raw data that our team was able to extract from the original website, and data that we have cleaned to resolve many formatting issues (and set up in different formats).
- The figures folder contains png files of all the generated figures in this analysis.
- The functiontools file contains the functions we created for our analysis. The test folder refers to testing of the functions we created. The command `pytest functiontools` should run all those tests.
- The environment.yml file reflects the environment that was created by our group to successfully run the analysis. 

To use this environment in the datahub:
- create a folder in your home directory called "envs" to save the environement. 
- navigate to the directory of this homework
- create a new environment from the environment.yml file by run in the terminal: mamba env create -f environment.yml -p ~/envs/nih
- to activate the new environment, run in the terminal: conda activate nih

To then use the environment with the jupyter notebook, you need to create a new kernel (named nih) from the environment.yml file:
- run in the terminal: python -m ipykernel install --user --name nih --display-name “IPython - nih”
- select this kernel from the list in the dropdown menu of the upper righthand corner of jupyter notebook. 

The LICENSE file states which licensing conditions apply to our work and makes it easier for other people to contribute.

The main.ipynb file contains the code and associated figures of our analysis. It is split into three parts. Each part addresses one of the three questions above. It also includes a contribution statement in the end that outlines what each group member did during the project, and outlines specifics about group work and collaboration. 

The Makefile contains env and all targets. The env target should make the environment with all necessary libraries, all should run all notebooks.
