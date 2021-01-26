needed_honey = float(input())
bee_name = input()

total_honey = 0

while bee_name != "Winter has come":
    collected_honey = 0
    for month in range(1, 7):
        collected_honey_per_month = float(input())

        collected_honey += collected_honey_per_month
        total_honey += collected_honey_per_month

    if collected_honey < 0:
        print(f"{bee_name} was banished for gluttony")

    if total_honey >= needed_honey:
        extra_honey = total_honey - needed_honey
        print(f"Well done! Honey surplus {extra_honey:.2f}.")
        break

    bee_name = input()

else:
    lacking_honey = needed_honey - total_honey
    print(f"Hard Winter! Honey needed {lacking_honey:.2f}.")

