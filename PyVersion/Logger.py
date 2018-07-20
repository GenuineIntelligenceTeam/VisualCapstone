def uploadimage(imgpath): #Finds an image from a given path and returns it
    pic = io.imread(imgpath)
    return pic

def makedescriptors (pic1): #takes in an image and returns the descriptors
    try:
        detections = list(face_detect(pic1))
        shape = shape_predictor(pic1, detections[0])
        descriptor1 = np.array(face_rec_model.compute_face_descriptor(pic1,shape))
    except:
        return None
    return descriptor1
    
def LogPic(face_data, label): #Takes in a descriptors of a face and the name, then it places the name and data in a dictionary
    if not face_dict: 
        face_count[label] = 1
        face_dict[label] = face_data
    elif face_dict.get(label) is None:
        face_count[label] = 1
        face_dict[label] = face_data
    else:
        face_count[label] += 1
        face_dict[label] += face_data