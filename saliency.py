# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:18:32 2017

@author: Mohammad Imtiaz
"""

import numpy as np

def saliency_map(img):
    
    import cv2
    
    imgM2 = img.copy()
    height = imgM2.shape[0]
    width = imgM2.shape[1]
    md = np.min([width,height])
    labImgM2 = cv2.cvtColor(imgM2, cv2.COLOR_BGR2Lab)
    l = labImgM2[:,:,0]/255.0
    a = labImgM2[:,:,0]/255.0
    b = labImgM2[:,:,0]/255.0
    
    sm = np.zeros((height,width), dtype = np.uint8)
    off1 = np.int32(md/2)
    off2 = np.int32(md/4)
    off3 = np.int32(md/8)
    
    for j in xrange(0, height):
        y11 = np.max([0, j-off1])
        y12 = np.min([j+off1, height])
        
        y21 = np.max([0, j-off2])
        y22 = np.min([j+off2, height])
        
        y31 = np.max([0, j-off3])
        y32 = np.min([j+off3, height])
        
        for k in xrange(0,width):
            x11 = np.max([0, k-off1])
            x12 = np.min([k+off1,width])
            
            x21 = np.max([0, k-off2])
            x22 = np.min([k+off2,width])
    
            x31 = np.max([0, k-off3])
            x32 = np.min([k+off3,width])      
            
    
            lm1 = np.mean(l[y11:y12, x11:x12])
            am1 = np.mean(a[y11:y12, x11:x12])
            bm1 = np.mean(b[y11:y12, x11:x12])
    
            
    
            lm2 = np.mean(l[y21:y22, x21:x22])
            am2 = np.mean(a[y21:y22, x21:x22])
            bm2 = np.mean(b[y21:y22, x21:x22])
    
    
    
            lm3 = np.mean(l[y31:y32, x31:x32])
            am3 = np.mean(a[y31:y32, x31:x32])
            bm3 = np.mean(b[y31:y32, x31:x32])  
    
            
            cv1 = (l[j,k] - lm1)**2 + (a[j,k] - am1)**2 + (b[j,k] - bm1)**2
            cv2 = (l[j,k] - lm2)**2 + (a[j,k] - am2)**2 + (b[j,k] - bm2)**2
            cv3 = (l[j,k] - lm3)**2 + (a[j,k] - am3)**2 + (b[j,k] - bm3)**2
            
            sm[j,k] = (cv1+cv2+cv3) * 255
            
    return sm