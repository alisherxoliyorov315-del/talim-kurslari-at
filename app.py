COURSE_DURATION_MONTHS = 3

courses = ["Python Backend", "Frontend React", "Ma'lumotlar bazasi"]
enrollments = []
payments = []

def show_courses():
    print(f"Mavjud kurslar (davomiyligi: {COURSE_DURATION_MONTHS} oy):")
    for i, c in enumerate(courses, 1):
        print(f"{i}. {c}")

if __name__ == "__main__":
    show_courses()
