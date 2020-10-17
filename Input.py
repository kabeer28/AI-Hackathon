#Getting the user's input
patient_bio = []
patient_bio.append(input("What is your age: "))
gender = input("Please enter your biological gender (male or female)")
patient_bio.append(gender)
if gender == "Male" or "male" or "MALE":
  gender_value = 1
elif gender == "Female" or "female" or "FEMALE":
  gender_value = 0
symptom_name = input("Please enter symptoms: ")
symptom_list = symptom_name.split()
print(symptom_list)
