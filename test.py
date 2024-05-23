import subprocess
import random
import openpyxl


def run_main_with_args(a, b, n):
    command = f"venv\Scripts\python.exe main.py {a} {b} {n}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    output, _ = process.communicate()
    return output.decode('utf-8')


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Results"
sheet.append(["a", "b", "n", "Result", "Execution Time", "Memory Usage"])


if __name__ == "__main__":
    for _ in range(25):
        a = random.randint(1, 10000000000000000000)
        b = random.randint(1, 10000000000000000000)
        n = random.randint(1, 99999999)

        if n % 2 != 0:
            output = run_main_with_args(a, b, n)
            lines = output.strip().split('\n')

            if len(lines) >= 3:
                result_line = lines[-3]
                time_line = lines[-2]
                memory_line = lines[-1]

                result = result_line.split(": ")[1]
                execution_time = time_line.split(": ")[1].split(" ")[0]
                memory_usage = memory_line.split(": ")[1].split(" ")[0]

                sheet.append([a, b, n, result, execution_time, memory_usage])

        workbook.save("results4.xlsx")