# === Step 1: Game setup ===
student_name = "Jalayah Ray"
current_gpa = 3.20
study_hours = 20
social_points = 50
stress_level = 35

print("=== Welcome to College Life Adventure ===")
print(f"Student: {student_name}")
print(f"Starting GPA: {current_gpa}")
print(f"Weekly Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

# === Step 2: Course planning decision ===
try:
    choice = input("Your choice (A/B/C): ").strip().upper()
except EOFError:
    choice = "B"

if choice == "A":
    if current_gpa >= 3.0:
        study_hours += 2
        stress_level -= 5
        print("Light load chosen: More free time, less stress!")
    else:
        study_hours += 1
        stress_level -= 2
        print("Light load chosen: Easier pace, slight improvement.")

elif choice == "B":
    if current_gpa >= 3.5:
        study_hours += 4
        stress_level += 8
        print("Standard load with high GPA: You handle it easily.")
    elif 2.5 <= current_gpa < 4.0:   # <= operator included
        study_hours += 3
        stress_level += 5
        print("Standard load: Manageable, but adds some stress.")
    else:
        study_hours += 2
        stress_level += 7
        print("Standard load feels a bit overwhelming.")

elif choice == "C":
    if current_gpa == 4.0:
        study_hours += 8
        stress_level += 10
        print("Heavy load with strong GPA: Challenging but possible!")
    elif current_gpa != 4.0:          # != operator included
        study_hours += 4
        stress_level += 12
        print("Heavy load without perfect GPA: Very stressful!")

else:
    print("Invalid choice. Defaulting to Standard plan effects.")
    study_hours += 2
    stress_level += 5

print("\n--- After Course Planning ---")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")

# === Step 3: Study strategy decision ===
study_options = ["Programming", "Math", "English", "History"]
print("\nPick a focus area for this week:")
for i, opt in enumerate(study_options, start=1):
    print(f"{i}) {opt}")

try:
    raw_choice = input("Type subject name or number (1=Programming, 2=Math, 3=English, 4=History): ").strip()
except EOFError:
    raw_choice = "Programming"  # default fallback for the grader

# Map numbers to subjects
num_to_subject = {"1": "Programming", "2": "Math", "3": "English", "4": "History"}

if raw_choice in num_to_subject:
    choice2 = num_to_subject[raw_choice]
else:
    choice2 = raw_choice.title()

# AI helped clarify membership operator syntax for this validation
if choice2 in study_options:

    # Programming: OR condition
    if choice2 == "Programming":
        if (study_hours >= 22) or (stress_level <= 40):
            delta_gpa = 0.05
            delta_social = -3
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("Programming grind: you focused hard on problem sets.")
        else:
            delta_gpa = 0.02
            delta_social = -2
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("Programming steady: small gains from light practice.")

    # Math: AND condition
    elif choice2 == "Math":
        if (study_hours >= 20) and (stress_level < 50):
            delta_gpa = 0.04
            delta_social = -1
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("Math momentum: consistent practice paid off.")
        else:
            delta_gpa = 0.015
            delta_social = -1
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("Math steady: drills helped a little.")

    # English: NOT condition
    elif choice2 == "English":
        if not (stress_level > 60):
            delta_gpa = 0.03
            delta_social = 2
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("English flow: reading & writing felt smooth.")
        else:
            delta_gpa = 0.02
            delta_social = 1
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("English steady: you skimmed and kept up.")

    # History: OR condition
    elif choice2 == "History":
        if (study_hours < 18) or (stress_level <= 45):
            delta_gpa = 0.02
            delta_social = 1
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("History highlights: bite-sized sessions still helped.")
        else:
            delta_gpa = 0.01
            delta_social = 0
            current_gpa = round(max(0.0, min(4.0, current_gpa + delta_gpa)), 2)
            social_points += delta_social
            print("History steady: notes review kept you on track.")

elif choice2 not in study_options:   # explicit NOT IN required by TC3
    print("[Branch] Invalid (not in list)")
    print("Invalid study choice. Please pick from the list next time.")
    social_points -= 2

print("\n--- After Study Strategy ---")
print(f"GPA: {current_gpa}")
print(f"Social Points: {social_points}")

# === Step 4: Final semester assessment ===
print("\n=== Final Semester Assessment ===")

ending = None

# Identity operator checks (required by TC4)
if type(current_gpa) is float and type(study_hours) is int and type(stress_level) is int and type(social_points) is int:
    HIGH_GPA = 3.5
    HIGH_HOURS = 25
    HIGH_STRESS = 70
    HIGH_SOCIAL = 60

    # Nested ifs (2+ levels)
    if current_gpa >= HIGH_GPA:
        if study_hours >= HIGH_HOURS:
            ending = "ENDING A: Dean's List energy—high study time with strong GPA."
        else:
            if stress_level <= 40:
                ending = "ENDING B: Quiet Excellence—great GPA with healthy balance."
            else:
                ending = "ENDING C: High Achiever, High Stress—watch your workload."
    else:
        if stress_level >= HIGH_STRESS:
            if social_points < 40:
                ending = "ENDING D: Burnout Alert—rethink your schedule and supports."
            else:
                ending = "ENDING E: Stressed but Supported—lean on your community."
        else:
            if social_points >= HIGH_SOCIAL:
                ending = "ENDING F: Campus Connector—networking boosted your semester."
            else:
                ending = "ENDING G: Steady Progress—solid growth with room to level up."
else:
    ending = "Type check failed: stats were not the expected types."

# Final stats + ending
print("\n=== Final Statistics ===")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print("\n=== Your Ending ===")
if ending is not None:  # identity operator 'is not'
    print(ending)
else:
    print("Outcome pending (no ending determined).")

# TC2: if/elif/else + comparison operators (<=, != added)

# TC3: membership (in/not in) + logical (and/or/not); unique outcomes per subject
