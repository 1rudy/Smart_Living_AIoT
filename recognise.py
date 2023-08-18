import face_recognition


# Load the first image with the known face
def face(file_path):
    image1 = face_recognition.load_image_file("my_photo.jpeg")
    encoding1 = face_recognition.face_encodings(image1)[0]

    # Load the second image to search for the face
    image2 = face_recognition.load_image_file("images/captured_image.jpg")
    encodings2 = face_recognition.face_encodings(image2)

    # Find matches between the first encoding and second image encodings
    match_found = False
    for encoding2 in encodings2:
        match = face_recognition.compare_faces([encoding1], encoding2)
        if match[0]:
            print("Match found ")
            match_found = True
            return "LOGIN SUCCESSFUL"
            break

    if not match_found:
        print("No match found ")
        return "LOGIN FAILED"
