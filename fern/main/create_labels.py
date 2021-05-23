from sklearn.preprocessing import LabelEncoder
import cv2                  
import numpy as np  
from keras.utils import to_categorical
import os       

X=[]
Z=[]
IMG_SIZE=150
FLOWER_ROSE_DIR= '../fern/main/flowers/rose'
FLOWER_IXORA_COCCINEA_DIR='../fern/main/flowers/ixora_c'
FLOWER_CRAPEJASMINE_DIR='../fern/main/flowers/jasmine'
FLOWER_ALLAMANDA_CATHARTICA_DIR='../fern/main/flowers/allamanda'
FLOWER_ORANGE_TRUMPET_DIR='../fern/main/flowers/orange_trumpet'
FLOWER_IXORA_DIR='../fern/main/flowers/ixora'
FLOWER_DAISY_DIR='../fern/main/flowers/daisy'
FLOWER_SUNFLOWER_DIR='../fern/main/flowers/sunflower'
FLOWER_LANTANA_DIR='../fern/main/flowers/lantana'

def assign_label(img,flower_type):
    return flower_type
    
def make_train_data(flower_type,DIR):
    for img in (os.listdir(DIR)):
        label=assign_label(img,flower_type)
        path = os.path.join(DIR,img)
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        
        X.append(np.array(img))
        Z.append(str(label))
        
        
make_train_data('rose',FLOWER_ROSE_DIR)
make_train_data('ixora coccinea',FLOWER_IXORA_COCCINEA_DIR)
make_train_data('crape jasmine',FLOWER_CRAPEJASMINE_DIR)
make_train_data('allamanda',FLOWER_ALLAMANDA_CATHARTICA_DIR)
make_train_data('orange trumpet',FLOWER_ORANGE_TRUMPET_DIR)
make_train_data('ixora',FLOWER_IXORA_DIR)
make_train_data('daisy',FLOWER_DAISY_DIR)
make_train_data('sunflower',FLOWER_SUNFLOWER_DIR)
make_train_data('lantana',FLOWER_LANTANA_DIR)
        
le=LabelEncoder()
Y=le.fit_transform(Z)
Y=to_categorical(Y,9)

def get_label(out_arg):
    return le.inverse_transform(out_arg)
