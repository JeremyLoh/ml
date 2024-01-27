# d2l and fastai learning
For Dive Into Deep Learning - https://d2l.ai/

Practical Deep Learning Course - https://course.fast.ai/

## Setup
A new conda environment was created using steps https://d2l.ai/chapter_installation/index.html#installing-miniconda
```shell
conda create --name d2l python=3.10 -y
conda activate d2l
```

## Packages used
https://d2l.ai/chapter_installation/index.html#installing-the-deep-learning-framework-and-the-d2l-package

```shell
# Tested packages at time of writing of book
pip install torch==1.12.0 torchvision==0.13.0
# package created to encapsulate frquently used functions and classes in the book
# if this fails, check https://github.com/d2l-ai/d2l-en/issues/2443
# pip install setuptools==66
pip install d2l==1.0.0b0
```

## Downloading and running code

Download using 
```shell
curl https://d2l.ai/d2l-en.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd d2l-pytorch
```

If you do not already have unzip installed, first run sudo apt-get install unzip.
Now we can start the Jupyter Notebook server by running:
```shell
jupyter notebook
```

Navigate to http://localhost:8888
Then we can run the code for each section of the book.
Whenever you open a new command line window, you will need to execute conda activate d2l to activate the runtime environment before running the D2L notebooks, or updating your packages (either the deep learning framework or the d2l package).
To exit the environment, run conda deactivate.