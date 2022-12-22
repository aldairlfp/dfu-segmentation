import cv2
from min_cut import *
from numpy import log

def read_image(path_to_image):
    return cv2.imread(path_to_image)

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def construct_graph(img):
    graph = []
    index = 0
    
    dir_x = [0, 0, 1, 1, 1, -1, -1, -1]
    dir_y = [1, -1, 1, -1, 0, 1, -1, 0]
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            graph.append([])
            for x in range(dir_x):
                for y in range(dir_y):
                    if i + x < 0 or i + x >= img.shape[0] or j + y < 0 or j + y >= img.shape[1]:
                        continue
                    graph[index].append(weight(img[i, j] - img[i + x, j + y]))
            index += 1
    
    return graph

def weight(a, b):
    weight = abs(a - b)/255
    
    return -log(weight) if weight > 0 else 0

def save_graph(graph, path_to_file):
    with open(path_to_file, 'w') as f:
        for i in range(len(graph)):
            f.write(str(i) + '\t' + '\t'.join([str(j) for j in graph[i]]) + '\n')
    

