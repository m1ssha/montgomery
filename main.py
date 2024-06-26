import sys
import psutil
import multiplication as m
import time
import gmpy2


def print_usage():
    print("Используй: python main.py <a> <b> <n>")
    print("<a>: первое число")
    print("<b>: второе число")
    print("<n>: модуль")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage()
    else:
        start_time = time.time()

        a = gmpy2.mpz(sys.argv[1])
        b = gmpy2.mpz(sys.argv[2])
        n = gmpy2.mpz(sys.argv[3])

        result = m.multiplication(a, b, n)
        print(f'Результат выполнения программы: {result}')

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения программы: {execution_time:.4f} секунд")

        memory_usage = psutil.Process().memory_info().rss / 1024**2
        print(f"Затраченная оперативная память: {memory_usage} мБ")
