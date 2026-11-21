COURSE_DURATION_MONTHS = 3

courses = ["Python Backend", "Frontend React", "Ma'lumotlar bazasi"]
enrollments = []
payments = []

def show_courses():
    print(f"Mavjud kurslar (davomiyligi: {COURSE_DURATION_MONTHS} oy):")
    for i, c in enumerate(courses, 1):
        print(f"{i}. {c}")

def add_course(title):
    courses.append(title)
    print(f"Yangi kurs qo'shildi: {title}")

if __name__ == "__main__":
    add_course("DevOps va Git")
    show_courses()
