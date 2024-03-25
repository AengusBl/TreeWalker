nodes = {
    "A" : {
            "text" : "Are we doing task 1?",
            "yes" : "AA",
            "no" : "AB",
            "summary_entry" : "Checked whether the task was task 1."},
    "AA" : {
            "text" : "Sorry, I can't do task 1 yet. Would you like to quit the process?",
            "yes" : "end", #the keyword the while loop waits for
            "no" : "A",
            "summary_entry" : ""},
            
    "AB" : {
            "text" : "instruction or question",
            "yes" : "ACC", #the keyword the while loop waits for
            "no" : "ABC",
            "summary_entry" : "a short summary of what the user did in the end"}

}

