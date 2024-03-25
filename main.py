#!/usr/bin/env python3

# Guides you through a flow-chart-like flow, and then gives you a summary of what you did.

def main():

    import os, datetime, nodes

    next_step = "A"
    new_summary = []
    
    while next_step != "end":
        current_step = nodes.nodes[next_step]
        while (yesno := input(current_step["text"] + " ").lower()) not in ["yes", "no", "y", "n"]:
            continue
        next_step = current_step[yesno]
        new_summary.append(f"\t <li>{current_step['summary_entry']}</li>" if current_step["summary_entry"] != "" else "")
    
    print("Generating a summary of what you did onto your desktop...")
    date_str = datetime.datetime.now().strftime
    with open(os.path.join(os.path.expanduser('~/Desktop'), f"summary_{date_str('%d%m%Y')}_{date_str('%H%M')}.html"), "w", encoding='utf-8') as f:
        f.write(HTML_file_wrapper().top + "\n".join(new_summary) + HTML_file_wrapper().bottom)



class HTML_file_wrapper:
    def __init__(self):
        self.top = """
        <!doctype html>
            <html>
                <head>
                    <title>Definitely not porn</title>
                    <meta name="The Best Summary of the Job" content="You just lost the game">
                </head>
                <body>
                    <header>
                        <h1 style="color:blue"><b>The <strong>Best</strong> Summary of the Job</b></h1>
                    </header>
                    <p>
                        <ol>
        """
        self.bottom = """
                        </ol>
                    </p>
                </body>
            </html>
        """




if __name__ == "__main__":
    main()
