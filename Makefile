.PHONY: env
env:
	mamba env create -f environment.yml -p ~/envs/nih
	bash -ic 'conda activate nih;python -m ipykernel install --user --name nih --display-name “IPython - nih”

.PHONY: remove-env
remove-env:
	mamba env remove -n nih

.PHONY : all
all:
	jupyter execute main.ipynb


.PHONY : html
html:
	jupyter-book build .
 
 
.PHONY : html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server
  
  
.PHONY : clean
clean :
	rm -f figures/*
