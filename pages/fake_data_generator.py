import random

# Reurns 1000 or 2000 fake data dataframe
def fake_data_generator(how_many):

    random_age = []
    random_hypertension = []
    random_ever_married = []
    random_work_type = []
    random_residence_type = []
    random_avg_glucose_level = []
    random_bmi = []
    random_smoking_status = []
    random_heart_disease = []
    random_gender = []
    random_stroke = []


    for i in range(how_many):
    random_age.append(random.choice(original['age']))
    random_hypertension.append(random.choice(original['hypertension']))
    random_ever_married.append(random.choice(original['ever_married']))
    random_work_type.append(random.choice(original['work_type']))
    random_residence_type.append(random.choice(original['Residence_type']))
    random_avg_glucose_level.append(random.choice(original['avg_glucose_level']))
    random_bmi.append(random.choice(original['bmi']))
    random_smoking_status.append(random.choice(original['smoking_status']))
    random_heart_disease.append(random.choice(original['heart_disease']))
    random_gender.append(random.choice(original['gender']))
    random_stroke.append(random.choice(original['stroke']))

    fake_data = {
        "age": random_age,
        "hypertension": random_hypertension,
        "ever_married": random_ever_married,
        "work_type": random_work_type,
        "Residence_type": random_residence_type,
        "avg_glucose_level": random_avg_glucose_level,
        "bmi": random_bmi,
        "smoking_status": random_smoking_status,
        "heart_disease": random_heart_disease,
        "gender": random_gender,
        "stroke": random_stroke
    }

    df_fakedata = pd.DataFrame(fake_data)
    return df_fake_data

