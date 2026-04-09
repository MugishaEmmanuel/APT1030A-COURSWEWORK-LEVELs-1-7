class Patient:
    def __init__(self, name: str, policy_number: str):
        self.name = name
        self.policy_number = policy_number

class NHIFClaim:
    CO_PAYMENT_RATE = 0.10

    def __init__(self, patient: Patient, amount: float):
        self.patient = patient
        self.amount = amount

    def calculate_claim(self):
        co_payment = self.amount * self.CO_PAYMENT_RATE
        return {"co_payment": co_payment, "nhif_covers": self.amount - co_payment}

    def process(self):
        result = self.calculate_claim()
        print("=== NHIF Claim Summary ===")
        print(f"Patient     : {self.patient.name}")
        print(f"Policy No.  : {self.patient.policy_number}")
        print(f"Total Bill  : KES {self.amount:.2f}")
        print(f"Co-payment  : KES {result['co_payment']:.2f}")
        print(f"NHIF Covers : KES {result['nhif_covers']:.2f}")
        print("===================================")

name_input = input("Enter Patient Name: ")
policy_input = input("Enter Policy Number: ")
amount_input = float(input("Enter total amount: "))
print()

patient = Patient(f"{name_input}", f"{policy_input}")
NHIFClaim(patient, amount_input).process()