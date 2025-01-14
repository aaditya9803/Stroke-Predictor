def get_result(age, gender, bmi, hypertension, heart_disease, avg_gulcose, work_type, married, smokes, residence, dont_know_gulcose):
    
    # Gender column mapping
    if gender == "Female":
        gender = 0
    elif gender == "Male":
        gender = 1
    else:
        print("error - gender")

    # married column mapping
    if married == "No":
        married = 0
    elif married == "Yes":
        married = 1
    else:
        print("error - ever_married")

    # Work_type column mapping
    if work_type == "Government Job":
        work_type = 0
    elif work_type == "Never Worked":
        work_type = 1
    elif work_type == "Private":
        work_type = 2
    elif work_type == "Self-employed":
        work_type = 3
    elif work_type == "Have children":
        work_type = 4
    else:
        print("error - work_type")

    # Residence column mapping
    if residence == "Rural":
        residence = 0
    elif residence == "Urban":
        residence = 1
    else:
        print("error - Residence_type")

    # Smoking column mapping
    if smokes == "Unknown":
        smokes = 0
    elif smokes == "Formerly Smoked":
        smokes = 1
    elif smokes == "Never Smoked":
        smokes = 2
    elif smokes == "Smokes":
        smokes = 3
    else:
        print("error - smoking_status")

    # Hypertension column mapping
    if hypertension == "No":
        hypertension = 0
    elif hypertension == "Yes":
        hypertension = 1
    else:
        print("error - hypertension")
    
    # Heart_disease column mapping
    if heart_disease == "No":
        heart_disease = 0
    elif heart_disease == "Yes":
        heart_disease = 1
    else:
        print("error - heart_disease")
    
    # Don't know glucose column mapping
    if dont_know_gulcose == False:
        dont_know_gulcose = 0
    elif dont_know_gulcose == True:
        dont_know_gulcose = 1
    else:
        print("error - dont_know_gulcose")
    print("From ml_function")
    print("\n")
    print (age, gender, bmi, hypertension, heart_disease, avg_gulcose, work_type, married, smokes, residence, dont_know_gulcose)