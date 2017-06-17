# Deep Vision for Dummies

* To install from Github do, 

`pip install git+git://github.com/ajayrfhp/dvd/`

* To install from PIP do, 

`pip install dvd`

Installation involves downloading of vgg model into /tmp/. This is a huge file, this takes about 20 minutes if you have good internet speed. Please wait.

# Usage : 

* Check examples folder for a demo notebook. 
  - Included transfer learning for MNIST, achieve 99.2% accuracy with logistic regression using transfer learnt representation as features
* Features as of now
  - Transfer Learning
  	- Takes input an image and returns a trasnfer learnt representation of the image. 
  	- The returned vector can be used as features of image to build classification algorithms using simple ML models like logistic regression, SVM. 
  	- Get transfer learnt embeddings from Vgg Net. Given an image obtain a dense vector representation. 
  - Object Detector
	- Simple object detector
	- More Coming
  - Image to text
	- Coming up
  - Text to image 
	- Coming up



This work is possible because of [Awesome place to get Vgg Net, by Professor Davi frosard](https://www.cs.toronto.edu/~frossard/post/vgg16/).

The Vgg model code and data used are from Professor Davi Frosard's website. 
