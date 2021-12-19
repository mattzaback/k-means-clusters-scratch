# -*- coding: utf-8 -*-
#*********************************************************************
#File name: IA5.py
#Author: Matthew Zaback
#Date: 11/11/2021
#Class: DSCI 440 ML
#Assignment: IA 5
#Purpose: Demonstrate k-means algorithm
#**********************************************************************

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt


#Load test data
file = open("Desktop\Data.txt", "r")
my_data = genfromtxt('Desktop\Data.txt', dtype = (float, float))

rows = len(my_data)
columns = 2

points = list ()

r=0
while r < rows:
    point = (my_data[r][0], my_data[r][1])
    points.append(point)
    r += 1

        
plt.scatter(my_data[:, 0], my_data[:, 1])

def list_avg(theList):
    xSum = 0
    ySum = 0
    i = 0
    while i < len(theList):
        xSum += theList[i][0]
        ySum += theList[i][1]
        i += 1
        
    xCoord = xSum / len(theList)
    yCoord = ySum / len(theList)
    
    orderedPair = (xCoord, yCoord)
    return orderedPair

def find_centroids(seeds, data, assignments):
    centroids = list ()
    
    i = 0
    while i < len(seeds): #k clusters 
        tempList = list ()
        j = 0
        while j < len(assignments): 
            if assignments[j] == i:
                tempList.append(my_data[j])
            j += 1
            
        center = list_avg(tempList)
        centroids.append (center)
        i += 1
    
    return centroids


def euclidean_distance(v1, v2):    
    distance = np.linalg.norm(v1 - v2)
    return distance

def assign_points(centroids, points):
    clusters = np.zeros(points.shape[0])
    
    i = 0
    while i < len(points):
        j = 0
        min_dist = float('inf')
        while j < len(centroids):
            dist = euclidean_distance(centroids[j], points[i])
            dist = dist**2  # 2Norm squared
            
            if dist < min_dist:
                min_dist = dist
                clusters[i] = j
                
            j += 1
        
        i += 1
    
    return clusters #400 length vector that holds the index of the centroid
        
def compute_sse(centroids, data, assignments):
    sseList = list ()
    i = 0
    while i < len(centroids):
        tempList = list ()
        j = 0
        while j < len(assignments):
            if assignments[j] == i:
                tempList.append(data[j])
            j += 1
          
        summation = 0
        m = 0
        while m < len(tempList):
            dist = euclidean_distance(centroids[i], tempList[m])
            dist = dist**2
            summation += dist
            m += 1
        
        sseList.append(summation)
        
        i += 1
        
    summation = 0
    i = 0
    while i < len(sseList):
        summation += sseList[i]
        i += 1
        
    return summation
        



k = 6 #input("Select a k from 1-9: ")
while k < 10:
    
    randomPicks = 0
    while randomPicks < 10: #10 random seedings
        
        randSeeds = list()
        i = 0
        while i < k: #determine random seeds and put them in a list
            randSeed = np.random.randint(0, len(my_data) - 1)
            randSeeds.append(my_data[randSeed])
            i += 1
        
        #find which points belong to which random seed
        clusters = assign_points(randSeeds, my_data) 
        
        #find the centroids of these clusters
        new_centroids = find_centroids (randSeeds, my_data, clusters)
        
        difference = 1
    
        while difference:
        
            old_centroids = new_centroids
            clusters = assign_points(old_centroids, my_data)
            new_centroids = find_centroids(old_centroids, my_data, clusters)
        
            #until convergence
            if new_centroids == old_centroids:
                difference = 0
            
        sse = compute_sse(new_centroids, my_data, clusters)
        
        
        randomPicks += 1
    k += 1
    





    

    
