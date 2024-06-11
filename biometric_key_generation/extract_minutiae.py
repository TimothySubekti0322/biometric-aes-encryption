import fingerprint_feature_extractor

def extract_minutiae(thin_image):
    features_terminations, features_bifurcations = fingerprint_feature_extractor.extract_minutiae_features(thin_image, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True)
    minutiae_points = []
    for idx, curr_minutiae in enumerate(features_terminations):
        minutiae_points.append((curr_minutiae.locX, curr_minutiae.locY))
        # print(f"Termination {idx+1}: ({curr_minutiae.locX}, {curr_minutiae.locY})")
    
    for idx, curr_minutiae in enumerate(features_bifurcations):
        minutiae_points.append((curr_minutiae.locX, curr_minutiae.locY))
        # print(f"Bifurcation {idx+1}: ({curr_minutiae.locX}, {curr_minutiae.locY})")
    
    print(f"Minutiae points: {minutiae_points}")
    return minutiae_points