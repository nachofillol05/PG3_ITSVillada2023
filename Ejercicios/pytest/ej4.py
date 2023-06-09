import statistics
def calculate_statistics(numbers: list):
    desviacion = statistics.pstdev(numbers)
    total = 0
    for num in numbers:
        total += num
        
    media = total / len(numbers)
        
    
    return desviacion,media