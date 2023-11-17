#imports:

import tkinter as tk

#setting up custom fonts:
digits_custom = ("Arial", 10, "bold")
total_label_custom = ("Arial", 14, "bold")
label_custom = ("Arial", 25, "bold")


class CalculatorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator") #setting up a name for the window
        self.root.resizable(False, False) #not allowing the window to be resized
        self.total_result = "" #the total expression that appears in a smaller font
        self.current_result = "" #the current expression we are working on, in a bigger font
        # creating the labels for the total_result and current_result so they appear on screen
        self.total_label, self.label = self.create_labels()
        self.create_labels()
        self.create_digit_buttons()
        self.create_operands_buttons()

    def create_labels(self):
        """
        This function creates the 2 labels that will appear on screen,corresponding to the total and current results.
        We created the buttons with a standard width of 10 and height of 3 used for all the buttons and the appropiate
           font declared at the beginning.
        :return: the 2 labels that we will use later on
        """
        self.total_label = tk.Label(self.root, text=self.total_result, width=10, height=3, bg="slategray",
                                    font=total_label_custom)
        self.total_label.grid(row=0, column=0, columnspan=5, sticky="nsew")
        self.label = tk.Label(self.root, text=self.current_result, width=10, height=3, bg="lightslategray",
                              font=label_custom)
        self.label.grid(row=1, column=0, rowspan=2, columnspan=5, sticky="nsew")
        return self.total_label, self.label

    def update_total_label(self):
        """
        This function updates the text of the total_label.
        """
        self.total_label.config(text=self.total_result)

    def update_label(self):
        """
        This function updates the text of the label corresponding to the current result
        """
        self.label.config(text=self.current_result)

    def create_digit_buttons(self):
        """
        This function creates the buttons for the digits and also for the "." for float numbers.
        Every button calls the self.add_to_expression(c) function, where c is the digit or "." in a string format.
        self.root.bind(str(i), lambda event, c=i: self.add_to_expression(str(c))) allows the keys corresponding to the
            digits to also call for the self.add_to_expression(c). For the "." button I also added "," as a key that
            calls the self.add_to_expression(".") function, as people are also used to referring to float numbers with 
            ",", not only with ".".
        """
        digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 1)
        }
        for i in digits:
            r, c = digits[i]
            button = tk.Button(self.root, text=str(i), width=10, height=3, bg="lightsteelblue", font=digits_custom,
                               command=lambda c=str(i): self.add_to_expression(c))
            self.root.bind(str(i), lambda event, c=i: self.add_to_expression(str(c)))
            if i == ".":
                button = tk.Button(self.root, text=str(i), width=10, height=3, bg="lightslategray", font=digits_custom,
                                   command=lambda c=str(i): self.add_to_expression(c))
                self.root.bind(",", lambda event, c=".": self.add_to_expression(str(c)))

            button.grid(row=r+2, column=c)

    def create_operands_buttons(self):
        """
        This function creates the buttons for the operands:+,-,*,/.
        Every button calls the self.add_operation(c) function, where c is the operand in a string format.
        self.root.bind(str(i), lambda event, c=i: self.add_to_expression(str(c))) allows the keys corresponding 
           to the operands to also call for the self.add_operation(c). 
        This function also calls for the functions that create the sqrt, equal, square and clear buttons.
        """
        operands = {
            "+": (1, 4),
            "-": (2, 4),
            "*": (3, 4),
            "/": (4, 4)
        }
        for i in operands:
            r, c = operands[i]
            button = tk.Button(self.root, text=str(i), width=10, height=3, bg="lightslategray", font=digits_custom,
                               command=lambda c=str(i): self.add_operation(c))
            button.grid(row=r+2, column=c)
            self.root.bind(str(i), lambda event, c=i: self.add_to_expression(str(c)))
        self.create_sqrt()
        self.create_equal()
        self.create_square()
        self.create_clear()

    def create_equal(self):
        """
        This function creates the equal button that calls for the self.result_operation() function.
        self.root.bind() allows the keys "=" and "Enter" to also call for the self.result_operation() function, as 
           "Enter"(<Return>) is also used by people to get the result of an operation.
        """
        button_equal = tk.Button(self.root, text="=", width=10, height=3, bg="lightslategray", font=digits_custom,
                                 command=lambda: self.result_operation())
        button_equal.grid(row=6, column=3)
        self.root.bind("=", lambda event: self.result_operation())
        self.root.bind("<Return>", lambda event: self.result_operation())

    def create_sqrt(self):
        """
        This function creates the sqrt button that calls for the self.add_operation() function but also the 
           self.result_operation() function, as according to the order of operations in mathematics the sqrt & square
           operations are the highest in order therefore they are always executed instantly.
        """
        button_sqrt = tk.Button(self.root, text="sqrt", font=digits_custom, width=10, height=3, bg="lightslategray",
                                command=lambda c="**0.5": [self.add_operation(c), self.result_operation()])
        button_sqrt.grid(row=7, column=1)

    def create_square(self):
        """
        This function creates the square button that calls for the self.add_operation() function but also the 
           self.result_operation() function, as according to the order of operations in mathematics the sqrt & square
           operations are the highest in order therefore they are always executed instantly.
        """
        button_square = tk.Button(self.root, text="^2", width=10, height=3, bg="lightslategray", font=digits_custom,
                                  command=lambda c="**2": [self.add_operation(c), self.result_operation()])
        button_square.grid(row=7, column=2)

    def create_clear(self):
        """
        This function creates the clear button that calls for the self.clear() function, that clears the previous 
           operations, reinitialising the expressions, the total and the current expressions.
        """
        button_clear = tk.Button(self.root, text="Clear", width=20, height=3, font=digits_custom, bg="darkgray",
                                 command=lambda : self.clear())
        button_clear.grid(row=7, column=3, columnspan=2, sticky="nsew")
        self.root.bind("c", lambda event: self.clear())
        self.root.bind("<BackSpace>", lambda event: self.clear())

    def add_to_expression(self, button):
        """
        This function adds characters to the current expression and calls for an update in the current label.
        :param button: this parameter receives the character corresponding to the digit/"." that has just been typed in.
        """
        self.current_result += str(button)
        self.update_label()

    def add_operation(self, operator):
        """
        This function adds characters to the current expression which is then added to the total expression and the 
           current expression is reinitialised(as an empty string). This function calls for the self.update_label()
           and the self.update_total_label() function as the text corresponding to the 2 labels has been modified.
        :param operator: this parameter receives the symbol of the operand that has just been typed in.
        """
        self.current_result += operator
        self.total_result += self.current_result
        self.current_result = ""
        self.update_label()
        self.update_total_label()

    def clear(self):
        """
        This function clears the 2 expressions, the total and the current one and calls for the functions 
           self.update_label() and self.update_total_label() as the text corresponding to the 2 labels has been 
           modified.
        """
        self.current_result = ""
        self.total_result = ""
        self.update_label()
        self.update_total_label()

    def result_operation(self):
        """
        This function is the core of the whole project. This function computes the result of the total expression by 
           adding the current expression to the total one. This updates the label to the result of the operation that 
           was typed in and it throws an error in case the operation is not possible(ex: a division by 0).This function
           calls for the self.total_update_label() and also for the self.update_label() as the text corresponding to 
           these 2 labels have been modified.
        """
        self.total_result += self.current_result
        self.update_total_label()
        try:
            self.current_result = str(eval(self.total_result))
            self.total_result = ""
        except Exception:
            self.current_result = "Error"
        finally:
            self.update_label()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
