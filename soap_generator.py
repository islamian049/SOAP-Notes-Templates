# SOAP Generator by Dr. Rashid Mansoor - @islamiano49
# MBBS + Senior Billing Auditor @ Ecodermedico

def generate_soap(name, age, gender, cc, hpi, vitals, exam, assessment, plan):
    return f"""
PATIENT: {name} | {age} {gender}
CC: {cc}
S: {hpi}
O: Vitals: {vitals} | Exam: {exam}
A: {assessment}
P: {plan}
Scribe: Dr. Rashid | eCW Ready | QA Checked
    """

# Example
print(generate_soap("Samina", "12 y/o", "F", "Sore throat", "2 days fever, dysphagia", "T 100.8F", "Pharynx erythematous", "Pharyngitis J02.9", "Amoxicillin"))

# For your portfolio - run this to generate new notes