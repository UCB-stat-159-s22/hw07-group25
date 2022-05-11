.PHONY: env
env:
	mamba env create -f environment.yml -p ~/envs/nih
	bash -ic 'conda activate nih;python -m ipykernel install --user --name nih --display-name “IPython - nih”


.PHONY : all
all :
	jupyter execute Reproduce_Outcomes.ipynb