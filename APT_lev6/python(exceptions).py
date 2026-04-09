def checkAccess(role):
    if role != "Doctor":
        raise Exception("Access Denied: Only doctors can access patient records.")
    else:
        return "Access Granted"

# Example usage
try:
    print(checkAccess("Nurse"))
except Exception as e:
    print(e)