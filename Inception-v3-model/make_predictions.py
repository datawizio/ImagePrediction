from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import pandas as pd
import argparse
import sys,os
import tensorflow as tf
from PIL import Image
from tqdm import tqdm
import numpy as np


def load_image(file_name, input_height=299, input_width=299, input_mean=0, input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader")
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader"))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
    else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)
    return result

def load_labels(filename):
    #Read in labels, one label per line."""
    return [line.rstrip() for line in tf.gfile.GFile(filename)]

def load_graph(filename):
    #Unpersists graph from file as default graph."""
    with tf.gfile.FastGFile(filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

data_root = 'dataset/'

src= data_root + 'test/from-internet/'

labels = 'tmp/output_labels.txt'
graph = 'tmp/output_graph.pb'

input_layer = 'Mul:0'
output_layer ='final_result:0'

load_graph(graph)

labels = load_labels(labels)
num_top_predictions = 1


with tf.Session() as sess:
    for f in os.listdir(src):
        if (f == '.DS_Store'): continue
        image_data = load_image(src + f)
        softmax_tensor = sess.graph.get_tensor_by_name(output_layer)
        predictions, = sess.run(softmax_tensor, {input_layer: image_data})
        top_k = predictions.argsort()[-num_top_predictions:][::-1]
        f = f.split('-')
        for node_id in top_k:
            predicted_label = labels[node_id]
            score = predictions[node_id]
            print(str('-'.join(f)), predicted_label, score)
            if f[0] in predicted_label:
                res = 1
            else:
                res = 0
        print("\n")
