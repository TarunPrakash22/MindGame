import tkinter as tk
#Convert to OOPS
class colorPallette:
    def __init__(self) -> None:
        self.dataList = []
        self.colors = ['red','orange','yellow','green','blue','indigo']

        self.root = tk.Tk()
        self.root.geometry("600x400")

    def createPallette(self):
        canvas = tk.Canvas(self.root,bg = "gray")
        canvas.pack(expand=True, fill = "both")

        frame = tk.Frame(canvas)
        frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        for i in range(2):
            for j in range(3):
                cButton = tk.Button(frame, text=self.colors[(i * 3) + j].capitalize(), fg=self.colors[(i * 3) + j], font=('Arial',25,'bold'),command = lambda x = i,y = j: self.onClick(x,y))
                cButton.place(relx=j/3, rely = i/3, relheight=1/3, relwidth=1/3)

        sButton = tk.Button(frame, text = "Submit",font=('Arial',25,'bold'), command = self.submitList)
        sButton.place(relx = 1/3, rely = 2/3, relheight = 1/3, relwidth = 1/3)

        dummyButton = tk.Button(frame, text = "Dummy",font=('Arial',25,'bold'))
        dummyButton.place(relx = 0/3, rely = 2/3, relheight = 1/3, relwidth = 1/3)

        clearButton = tk.Button(frame, text = "Clear",font=('Arial',25,'bold'), command = self.clearList)
        clearButton.place(relx = 2/3, rely = 2/3, relheight = 1/3, relwidth = 1/3)

    def onClick(self,x,y):
        self.dataList.append(self.colors[(x * 3) + y].capitalize())

    def submitList(self):
        self.root.quit()
        self.root.destroy()

    def clearList(self):
        self.dataList = []

    def mainLoop(self):
        self.root.mainloop()

