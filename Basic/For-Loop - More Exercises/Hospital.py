days = int(input())
num_of_medic = 7
days_count = 1
treated_patients = 0
untreated_patients = 0

# logic
for period in range(1, days + 1):
    patients = int(input())
    if days_count % 3 == 0:
        if untreated_patients > treated_patients:
            num_of_medic += 1
    days_count += 1
    if patients > num_of_medic:
        dif = patients - num_of_medic
        treated_patients += num_of_medic
        untreated_patients += dif
    elif patients <= num_of_medic:
        treated_patients += patients

# output
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
