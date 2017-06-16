from __future__ import division
import tensorflow as tf
import numpy as np
from scipy.misc import imread, imresize
import vgg16
from vgg16 import *


def get_embedding_x(img):
    '''
            Args    : Numpy Image Vector
            Returns : Embedded feature vector of length 4096
    '''
    sess = tf.Session()
    imgs = tf.placeholder(tf.float32, [None, None, None, None])
    vgg = vgg16(imgs, '/tmp/vgg16_weights.npz', sess)
    #img = imresize(img, (224, 224))
    img = np.array(img)
    emb = sess.run(vgg.emb, feed_dict={vgg.imgs: [img]})
    emb = np.reshape(emb,(emb.shape[0],emb.shape[1] * emb.shape[2] * emb.shape[3]))
    return emb


def get_embedding_X(img):
    '''
            Args 	: Numpy Images vector
            Returns : Embedded Matrix of length Samples, 4096
    '''
    img = img.reshape((img.shape[0], img.shape[1], img.shape[2], 1))
    sess = tf.Session()
    imgs = tf.placeholder(tf.float32, [None, None, None, None])
    vgg = vgg16(imgs, '/tmp/vgg16_weights.npz', sess)
    embs = []
    cnt = 0
    for img_batch in np.array_split(img, img.shape[0] / 1000):
    	emb = sess.run(vgg.emb, feed_dict={vgg.imgs: img_batch})
        embs.extend(emb)
        cnt += 1
        progress = round(100 * (cnt * 1000 / img.shape[0]),2)
        print progress
    embs = np.array(embs)
    print embs.shape
    embs = np.reshape(embs,(embs.shape[0],embs.shape[1] * embs.shape[2] * embs.shape[3]))
    return embs


