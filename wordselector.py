import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Word Selector')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)  
        # add input panel      
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)   
        # add a post button     
        my_btn = wx.Button(panel, label='Post')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)  
        # a dialogue
        my_post = wx.Frame(panel,style=wx.CAPTION)   
        panel.SetSizer(my_sizer)        
        self.Show()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("welcome to word selector")
        #label

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
       
        if not value:
            wx.MessageBox("You did not enter anything")
            print("You didn't enter anything!")
        else:
             # importing package
         from better_profanity import profanity
             #Text to be censored
         text = self.text_ctrl.GetValue()
            # do censoring
        censored = profanity.censor(text, '*')
            #view output
        wx.MessageBox(censored)
        print(censored)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
