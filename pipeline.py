import subprocess # used to execute another python script inside a python script

def run_pipeline():
    print("Starting the Forum Analyzer Pipeline\n")

    print("Fetching forum data\n", flush=True)
    subprocess.run(["python","scraper/fetch_data.py"]) # basically runs the python fetch_data.py command internally

    print("Performing analysis\n", flush=True)
    subprocess.run(["python","analyzer/analyze.py"])

# calling the function only when the script is run directly
if __name__=="__main__":
    run_pipeline()