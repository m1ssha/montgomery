import multiplication as m
import random
import openpyxl
import gmpy2
import time
import psutil


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Results"
sheet.append(["a", "b", "n", "Result", "Время выполнения программы (сек)", "Использование памяти (мБ)"])

bits = 200000
print(f"Заданное число бит = {bits}")


if __name__ == "__main__":
    for _ in range(5):
        start_time = time.time()
        a = gmpy2.mpz(random.getrandbits(bits))
        b = gmpy2.mpz(random.getrandbits(bits))
        n = gmpy2.mpz(random.getrandbits(bits))

        print(f"Количество знаков в числе:\na: {len(str(a))}\nb: {len(str(b))}\nn: {len(str(n))}\n")

        if n % 2 == 0:
            n += 1

        result = m.multiplication(a, b, n)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time}")
        memory_usage = psutil.Process().memory_info().rss / 1024**2

        sheet.append([str(a), str(b), str(n), str(result), execution_time, memory_usage])

    workbook.save(f"results{bits}.xlsx")
