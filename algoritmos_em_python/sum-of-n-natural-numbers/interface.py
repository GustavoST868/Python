import tkinter as tk
import number_sum

def Result():
    result = number_field.get()
    return result

def Interface_Result():
    window_result = tk.Tk()
    window_result.title("")
    window_result.configure(bg="gray76")
    label_result = tk.Label(window_result, text="Resultado:")
    label_result.grid(row=0, column=0, padx=5, pady=5)
    result_value = Result()  # Call the Result function to get the result
    label_result_value = tk.Label(window_result, text=number_sum.Sum(int(result_value)))
    label_result_value.grid(row=0, column=1, padx=5, pady=5)
    window_result.mainloop()

def Interface():
    window = tk.Tk()
    window.title("")
    window.configure(bg="gray76")
    window.geometry("200x70")
    number_label = tk.Label(window, text="Número:")
    number_label.grid(row=0, column=0, padx=5, pady=5)
    global number_field  # Make number_field a global variable
    number_field = tk.Entry(window)
    number_field.grid(row=0, column=1, padx=5, pady=5)
    button_calculate = tk.Button(window, text="Calculate", command=Interface_Result)  # Specify the command
    button_calculate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)  # Span two columns for the button
    window.mainloop()


