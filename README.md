# d2l and fastai learning
For Dive Into Deep Learning - https://d2l.ai/

Practical Deep Learning Course - https://course.fast.ai/
- Book - https://course.fast.ai/Resources/book.html

## Setup
A new conda environment was created using steps https://d2l.ai/chapter_installation/index.html#installing-miniconda
```shell
conda create --name d2l python=3.10 -y
conda activate d2l
```

## Checking pytorch is using GPU
- Install pytorch - https://pytorch.org/get-started/locally/

https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu
```python
import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())

current_device = torch.cuda.current_device()
print(torch.cuda.device(current_device))
print(torch.cuda.get_device_name(current_device))
```

## Converting to Fastai image
https://forums.fast.ai/t/how-to-create-image-with-class-fastai-vision-core-pilimage/82191/1
```python
from fastai.vision.core import PILImage

basset_hound_image = PILImage.create("basset_hound_example.jpg")
print(type(basset_hound_image))
# basset_hound_image.show()

result = convnext_nano_learner.predict(basset_hound_image)
print(result)
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