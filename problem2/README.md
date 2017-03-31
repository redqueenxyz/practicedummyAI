## tutorialAI
### Problem 2

[Anaconda](https://www.google.ca/search?q=anaconda&oq=anaconda&aqs=chrome..69i57j0l5.2044j0j1&sourceid=chrome&ie=UTF-8) is a data science Python distribution with excellent support and virtual environment services. Also comes in a convenient [Miniconda](https://conda.io/miniconda.html) to save storage if necessary.

`conda` is the primary package manager for this distribution, and is available exclusively through the command line. Here is a quick refresher on CLI for [Windows](https://www.lynda.com/-tutorials/Windows-command-line-basics/497312/513424-4.html) and [Linux systems](https://www.udacity.com/course/linux-command-line-basics--ud595).  


1) [Download and install Anaconda](https://www.continuum.io/downloads) (Graphical or Command Line):

    `bash <(curl -O https://repo.continuum.io/archive/Anaconda3-4.3.0-MacOSX-x86_64.sh)`

2)  Create a new environment:

    `conda create -n test_environment python=3`

3) Activate that environment

    `source activate test_environment`

4) List installed packages

    `conda list`

5) Install some new packages depending on what you need:

    `conda install numpy pandas matplotlib`

6) Install Jupyter:

    `conda install jupyter notebook`

7) Export the current environment:

    `conda env export > test_environment.yaml`

8) Destroy the environment you just made:

    `conda env remove -n test_environment`

9) Rebuild that environment:

    `conda env create -f environment.yaml`

8) Submit a PR to this repo with your own `environment.yaml` in the `/problem2/ folder. 


Recommended packages:
* Numpy: For numeric manipulation.
* Pandas: For dataframes.
* Matplotlib: For visualizations. 
* Jupyter: For notebook and REPL.