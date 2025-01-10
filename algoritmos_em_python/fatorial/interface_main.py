import tkinter as tk
import factorial

def Interface():
    def Calculate():
        string = factorial.Factorial(int(number_field.get()))
        Window_Result(string)
    
    def Window_Result(result_string):
        window_result = tk.Tk()
        window_result.title("Resultado")
        label_result = tk.Label(window_result, text="Resultado=>")
        label_result.grid(row=0, column=0, padx=5, pady=5)
        label_final = tk.Label(window_result, text=result_string)
        label_final.grid(row=0, column=1, padx=5, pady=5)
        window_result.mainloop()

    # Janela principal
    window = tk.Tk()
    window.geometry("200x70")
    window.title("")

    # Rótulo e campo de entrada para o número
    number_label = tk.Label(window, text="Number:")
    number_label.grid(row=0, column=0, padx=5, pady=5)
    number_field = tk.Entry(window)
    number_field.configure(background="gray76")
    number_field.grid(row=0, column=1, padx=5, pady=5)

    # Botão de cálculo
    calculate_button = tk.Button(window, text="Calcular", command=Calculate)
    calculate_button.configure(background="gray76")
    calculate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()