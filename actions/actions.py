from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pages.ml_function import get_result

# def verify_data(smoking_status, if_know_avg_glucose, avg_glucose_level, height, weight, residence_type, work_type, ever_married, heart_disease, hypertension, age, gender):


class ActionHandleConversation(Action):

    def name(self) -> Text:
        return "action_handle_conversation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_data = {
            "age": None,
            "gender": None,
            "hypertension": None,
            "heart_disease": None,
            "ever_married": None,
            "work_type": None,
            "residence_type": None,
            "if_know_avg_glucose": None,
            "avg_glucose_level": None,
            "height": None,
            "weight": None,
            "smoking_status": None
        }

        user_data["age"] = tracker.get_slot('age')
        user_data["gender"] = tracker.get_slot('gender')
        user_data["hypertension"] = tracker.get_slot('hypertension')
        user_data["heart_disease"] = tracker.get_slot('heart_disease')
        user_data["ever_married"] = tracker.get_slot('ever_married')
        user_data["work_type"] = tracker.get_slot('work_type')
        user_data["residence_type"] = tracker.get_slot('Residence_type')
        user_data["if_know_avg_glucose"] = tracker.get_slot('if_know_avg_glucose')
        user_data["avg_glucose_level"] = tracker.get_slot('avg_glucose_level')
        user_data["height"] = tracker.get_slot('height')
        user_data["weight"] = tracker.get_slot('weight')
        user_data["smoking_status"] = tracker.get_slot('smoking_status')


        print(f'Age = {user_data["age"]}, Gender = {user_data["gender"]}, Hypertension = {user_data["hypertension"]}, '
              f'Heart Disease = {user_data["heart_disease"]}, Ever Married = {user_data["ever_married"]}, '
              f'Work Type = {user_data["work_type"]}, Residence Type = {user_data["residence_type"]}, '
              f'If know Glucose Level = {user_data["if_know_avg_glucose"]} ,Avg Glucose Level = {user_data["avg_glucose_level"]}, Height = {user_data["height"]}, '
              f'Weight = {user_data["weight"]}, Smoking Status = {user_data["smoking_status"]}')
        



        for key in user_data:

            if key == "avg_glucose_level" and user_data["if_know_avg_glucose"] != None:
                if user_data["if_know_avg_glucose"].lower() in ["no", "nope", "don't know", "don't have", "not sure"]:
                    user_data["avg_glucose_level"] = 106.14

            if user_data[key] is None:
                dispatcher.utter_message(response=f"utter_ask_{key}")

                print("hi from if")                
                break

            if None not in user_data.values():
                dispatcher.utter_message(response="utter_thank_you")
                print("hi from 2nd if")


                #Mapping Smoke Status

                if user_data["smoking_status"].lower() == "never smoked":
                    user_data["smoking_status"] = 2
                elif user_data["smoking_status"].lower() == "formerly smoked":
                    user_data["smoking_status"] = 1
                elif user_data["smoking_status"].lower() in ["smokes", "smoker", "smoking", "smoke"]:
                    user_data["smoking_status"] = 3
                elif user_data["smoking_status"].lower() == "unknown" or user_data["smoking_status"].lower() == "don't know":
                    user_data["smoking_status"] = 0
                else:
                    dispatcher.utter_message(response="utter_ask_smoking_status")

                # Mapping Gender

                if user_data["gender"].lower() == "female":
                    user_data["gender"] = 0
                elif user_data["gender"].lower() == "male":
                    user_data["gender"] = 1
                else:
                    dispatcher.utter_message(response="utter_ask_gender")

                # Ever Married Mapping
                ever_married = ["no", "nope", "never been", "not married"]
                if user_data["ever_married"].lower() in ever_married:
                    user_data["ever_married"] = 0
                elif user_data["ever_married"].lower() in ["yes", "yeah", "yep", "married", "have been"]:
                    user_data["ever_married"] = 1
                else:
                    dispatcher.utter_message(response="utter_ask_ever_married")

                # Work Type Mapping
                if user_data["work_type"].lower() == "govt_job" or user_data["work_type"].lower() == "government job":
                    user_data["work_type"] = 0
                elif user_data["work_type"].lower() == "never worked":
                    user_data["work_type"] = 1
                elif user_data["work_type"].lower() == "private":
                    user_data["work_type"] = 2
                elif user_data["work_type"].lower() == "self-employed" or user_data["work_type"].lower() == "self employed":
                    user_data["work_type"] = 3
                elif user_data["work_type"].lower() == "have children" or user_data["work_type"].lower() == "children":
                    user_data["work_type"] = 4
                else:
                    dispatcher.utter_message(response="utter_ask_work_type")

                # Residence Type Mapping
                if user_data["residence_type"].lower() in ["rural", "village"]:
                    user_data["residence_type"] = 0
                elif user_data["residence_type"].lower() in ["urban", "city", "suburban"]:
                    user_data["residence_type"] = 1
                else:
                    dispatcher.utter_message(response="utter_ask_residence_type")

                # Heart Disease Mapping
                if user_data["heart_disease"].lower() in ["yes", "yeah", "yep", "have"]:
                    user_data["heart_disease"] = 1
                elif user_data["heart_disease"].lower() in ["no", "nope", "don't have", "don't"]:
                    user_data["heart_disease"] = 0
                else:
                    dispatcher.utter_message(response="utter_ask_heart_disease")

                # Hypertension Mapping
                if user_data["hypertension"].lower() in ["yes", "yeah", "yep", "have"]:
                    user_data["hypertension"] = 1
                elif user_data["hypertension"].lower() in ["no", "nope", "don't have", "don't"]:
                    user_data["hypertension"] = 0
                else:
                    dispatcher.utter_message(response="utter_ask_hypertension")

                # If Know Avg Glucose Mapping

                if user_data["if_know_avg_glucose"].lower() in ["yes", "yeah", "yep", "know", "have", "sure"]:
                    user_data["if_know_avg_glucose"] = 1
                elif user_data["if_know_avg_glucose"].lower() in ["no", "nope", "don't know", "don't have", "not sure"]:
                    user_data["if_know_avg_glucose"] = 0
                else:
                    dispatcher.utter_message(response="utter_ask_if_know_avg_glucose")

                if user_data["age"]:
                    user_data["age"] = int(user_data["age"])
                else:
                    dispatcher.utter_message(response="utter_ask_age")


                if user_data["avg_glucose_level"]:
                    user_data["avg_glucose_level"] = float(user_data["avg_glucose_level"])
                else:
                    dispatcher.utter_message(response="utter_ask_avg_glucose_level")
                
                if user_data["height"]:
                    user_data["height"] = float(user_data["height"])
                else:
                    dispatcher.utter_message(response="utter_ask_height")

                if user_data["weight"]:
                    user_data["weight"] = float(user_data["weight"])
                else:
                    dispatcher.utter_message(response="utter_ask_weight")
        
                break 
                   
        # print(user_data)
        if None in user_data.values():
            return []
        else:
            bmi = user_data["weight"] / (user_data["height"] ** 2)
            result = get_result(user_data["age"], user_data["gender"], bmi, user_data["hypertension"], user_data["heart_disease"], user_data["avg_glucose_level"], user_data["work_type"], user_data["ever_married"], user_data["smoking_status"], user_data["residence_type"], False)
            result_prediction = result[0]
            result_probability = result[1]
            if result_prediction == 1:
                result_prediction = "have risk"
            else:
                result_prediction = "don't have risk"
    
            print(result)
            result_probability = f"{result_probability*100:.2f}"
            dispatcher.utter_message(text=f"Based on the information you provided, you {result_prediction} of having a stroke. The probability of you having a stroke is {result_probability}%")

        return []