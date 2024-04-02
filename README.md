# Getting Started with Streamlit PDF Processor

This guide will help you set up and run a Streamlit app that processes PDF files. The app will split PDFs into individual pages and rename them based on an employee identification number found within the PDF. This guide is designed for beginners and does not assume any prior knowledge of programming or command line interfaces.

## What is Streamlit?

Streamlit is a Python library that allows you to create web applications quickly and easily. It's particularly useful for data scientists and machine learning engineers who want to share their work without needing to know web development. With Streamlit, you can build interactive web apps with just a few lines of Python code.

## What You Need

- A computer with an internet connection.
- Basic knowledge of how to use a computer and navigate through folders.

## Step 1: Install Python

1. **Download Python**: Go to the official Python website (https://www.python.org/) and download the latest version of Python for your operating system (Windows, macOS, or Linux).
2. **Install Python**: Run the installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" during the installation process. This will allow you to run Python from any command line interface.
3. **Install Git**: Go to [git's website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and install Git on your coomputer. It will be used to pull this code into your file system.

## Step 2: Install Streamlit and PyPDF2

1. **Open Command Line Interface**: On Windows, you can search for "cmd" in the Start menu. On macOS, you can search for "Terminal" in Spotlight. On Linux, you can usually open the terminal from your applications menu.
2. **Install Streamlit**: Type the following command and press Enter:
   ```
   pip install streamlit
   ```
3. **Install PyPDF2**: Type the following command and press Enter:
   ```
   pip install PyPDF2
   ```

## Step 3: Download the Streamlit App

1. **Download the App**: You will need to download the Streamlit app script (`pdf_processor.py`) from the source provided. You can do this by visiting the link provided and saving the file to your computer. Do this by running in the command line: `git clone https://github.com/Bryson14/streamlit-app-pdf-extractor.git` into the file directory where you want it copied.
2. **Place the App in a Folder**: Move the downloaded `pdf_processor.py` file into a folder where you want to keep the app.

## Step 4: Run the Streamlit App

1. **Open Command Line Interface**: Open the command line interface again.
2. **Navigate to the App Folder**: Use the `cd` command to change directories to the folder where you saved the `pdf_processor.py` file. For example, if you saved the file in a folder named "StreamlitApp" on your desktop, you would type:
   ```
   cd Desktop/StreamlitApp
   ```
3. **Run the App**: Type the following command and press Enter:
   ```
   streamlit run pdf_processor.py
   ```
4. **Access the App**: Your default web browser should automatically open a new tab with the Streamlit app. If it doesn't, the command line interface will provide a URL that you can copy and paste into your browser.

## Step 5: Using the App

1. **Upload a PDF**: In the Streamlit app, you will see a file uploader. Click on it and select the PDF file you want to process.
2. **Wait for Processing**: The app will process the PDF, splitting it into individual pages and looking for an employee identification number on each page.
3. **View Results**: The app will display the employee identification number found on each page.

## Troubleshooting

- If you encounter any errors, make sure you have followed all the steps correctly.
- If the app doesn't open in your browser, check the command line interface for a URL to access the app.
- If you have any questions or need further assistance, feel free to ask.

## Conclusion

Congratulations! You have successfully set up and run a Streamlit app that processes PDF files. This app is a great example of how Streamlit can be used to create interactive web applications with just a few lines of Python code. If you're interested in learning more about Streamlit or Python, there are many resources available online.

Citations:
[1] https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/
[2] https://dev.to/shaheryaryousaf/building-your-first-streamlit-application-a-beginners-guide-14ki
[3] https://codeforgeek.com/streamlit-in-python/
[4] https://builtin.com/machine-learning/streamlit-tutorial
[5] https://www.datacamp.com/tutorial/streamlit
[6] https://github.com/streamlit/streamlit/blob/develop/README.md
[7] https://www.justintodata.com/streamlit-python-tutorial/
[8] https://medium.com/swlh/a-beginners-guide-to-streamlit-5e0a4e711968
[9] https://medium.com/@vkrntkmrsngh/mastering-streamlit-a-beginners-guide-80d812304a89
[10] https://medium.com/@kolhe.shivam17/beginners-guide-to-streamlit-part-1-2dbfc957b150
[11] https://blog.streamlit.io/how-to-master-streamlit-for-data-science/
[12] https://blog.streamlit.io/streamlit-app-starter-kit-how-to-build-apps-faster/
[13] https://soumodeep60.medium.com/creating-interactive-websites-with-streamlit-a-beginners-guide-a2539722164d
[14] https://streamlit.io/
[15] https://www.makeuseof.com/getting-started-with-streamlit/