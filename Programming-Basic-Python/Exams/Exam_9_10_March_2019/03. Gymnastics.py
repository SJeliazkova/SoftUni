country = input()
device_type = input()

difficulty_points = 0
performance_points = 0

if country == "Russia" and device_type == "ribbon":
    difficulty_points = 9.1
    performance_points = 9.4
elif country == "Russia" and device_type == "hoop":
    difficulty_points = 9.3
    performance_points = 9.8
elif country == "Russia" and device_type == "rope":
    difficulty_points = 9.6
    performance_points = 9.0
elif country == "Bulgaria" and device_type == "ribbon":
    difficulty_points = 9.6
    performance_points = 9.4
elif country == "Bulgaria" and device_type == "hoop":
    difficulty_points = 9.55
    performance_points = 9.75
elif country == "Bulgaria" and device_type == "rope":
    difficulty_points = 9.5
    performance_points = 9.4
elif country == "Italy" and device_type == "ribbon":
    difficulty_points = 9.2
    performance_points = 9.5
elif country == "Italy" and device_type == "hoop":
    difficulty_points = 9.45
    performance_points = 9.35
elif country == "Italy" and device_type == "rope":
    difficulty_points = 9.7
    performance_points = 9.15

total_points = difficulty_points + performance_points
diff = 20 - total_points
needed_points_percent = diff / 20 * 100

print(f"The team of {country} get {total_points:.3f} on {device_type}.")
print(f"{needed_points_percent:.2f}%")