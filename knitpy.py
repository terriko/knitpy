#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk

class KnitPyApp(tk.Frame):
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.pack()
      self.createWidgets()

   def createWidgets(self):
      self.knit = tk.Button(self)
      self.knit["text"] = "Knit"
      self.knit["command"] = self.add_knit_stitch
      self.knit.pack(side="right")

      self.purl = tk.Button(self)
      self.purl["text"] = "Purl"
      self.purl["command"] = self.add_purl_stitch
      self.purl.pack(side="right")

      self.chart = tk.Canvas(self, width=400, height=300)
      self.chart.pack(side="left")
      self.draw_chart_grid()

      self.QUIT = tk.Button(self, text="QUIT", fg="#FF0000", 
                            command=root.destroy)
      self.QUIT["bg"] = "blue"
      self.QUIT.pack(side="bottom")
      self.pack(fill="both", expand=1)

   def add_knit_stitch(self):
      print("v")

   def add_purl_stitch(self):
      print(".")

   def draw_chart_grid(self):
      width = 20
      height = 8
      cell_width = 20
      cell_height = 20
      max_width = width*cell_width
      max_height = height*cell_height
      self.chart.create_rectangle(0, 0, max_width, max_height, width="2")
      for i in range(0, width):
         self.chart.create_line(i*cell_width, 0, i*cell_width, max_height)
      for i in range(0, height):
         self.chart.create_line(0, i*cell_height, max_width, i*cell_height)

root = tk.Tk()
app = KnitPyApp(master=root)
app.mainloop();
