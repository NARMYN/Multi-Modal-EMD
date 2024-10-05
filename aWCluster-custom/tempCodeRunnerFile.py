# End timing
end_time = time.time()

print(f"Elapsed time: {end_time - start_time} seconds")

# Optionally save the distance matrix to a .csv file
mydf = pd.DataFrame(distanceM)
path = Path(f'{subtype}/Distance_Matrix')
path.mkdir(parents=True, exist_ok=True)
mydf.to_csv(f'{subtype}/Distance_Matrix/trial1.csv', header=False)
