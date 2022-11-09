import inspect
import tkinter

print(inspect.ismodule(tkinter))
print(callable(tkinter))
for method in dir(tkinter):
    print(method)
print(inspect.isclass(tkinter.mainloop))
print(callable(tkinter.mainloop))
for method in dir(tkinter.mainloop):
    print(method)
