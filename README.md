# PDF Book Club Web Application

## CREDITS
All code and code-related edits have been written and generated by OpenAI's ChatGPT-4 Code Interpreter, with my acting as 'prompter'

## LICENSE
This project is under the GNU General Public License. This means you can use, modify, and distribute this software, but any changes or derived works must also be shared under the same license. For more details, see the full text of the GPL.

## WHAT IT LOOKS LIKE
This is a python app that runs on flask,aand you will host it in your localhost on a web browser. You need to be connected to wi-fi in order for the app to work properly, because in order to generate the bookclub discussions, it needs to make calls to the OpenAI API. Here's examples of what it looks like when it is working:

![Screenshot from 2024-03-31 20-57-28](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/978f3aa5-f132-46f5-95c7-adc909f20d4a)
![Screenshot from 2024-03-31 20-57-46](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/41919a15-fe92-47a3-b816-560a2175e552)

# GETTING STARTED

## STEP 1 - DO YOU HAVE GIT ON YOUR MACHINE?
You will bring the app onto your machine using Github, so first, you need to make sure you have git installed and its ready to retrieve the files

### SETTING UP THE LOCAL REPOSITORY

1. Open your terminal.

2. Create a directory/folder for the project using:
   ```
   mkdir pdf_bookclub
   ```

3. Navigate into the directory you just created:
   ```
   cd pdf_bookclub
   ```

4. Clone the git repository: 
   ```
   git clone git@github.com:garrettstephens11/pdf_bookclub.git
   ```

If you encounter git issues, (or do not have it at all yet) please visit https://chat.openai.com for assistance, and ask Chat GPT "please walk me through setting up git on my machine"

### VERIFYING GIT SETUP

1. Open your terminal anew
2.
   ```
   cd pdf_bookclub
   ```
3. `Check if you are connected to the remote repository.
    ```
   git remote -v
   ```
6. Verify the status of your repository.
    ```
   git status
   ```
8. If local doesn't match remote:
   ```
   git pull origin main
   ```
4. Ensure sync:
   ```
   git pull origin main
   ```
You should see "Everything up-to-date".

## STEP 2 - DO YOU HAVE OPENAI API?
If not, you need to check a few things

1. Visit platform.openai.com
2. Create an account, or sign in if you already have an account
3. Go back to platform.openai.com
4. Check that you have an "Organization" and an "Organization ID". You will need this information to use the API to get PDF Bookclub going
   
![InShot_20240331_213720434](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/e0d273aa-87bc-46d7-9b72-4c84c7c21f41)

5. Check that you have generated a key for OpenAI API

![Screenshot from 2024-03-31 20-55-50](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/cfc487df-b602-4a8b-b8ed-d4fd1f61d184)

6. If you have not generated a key, click the button to generate the key, name it whatever you like, and save it in some text/.txt file, from which you will copy and paste in the future for the app

7. Check that you have a payment card on your Billing account for OpenAI API. For reference, if you use PDF Bookclub for several hours, it should cost you only around ~$1, but you will be able to track your spending via the "usage" tab on platform.openai.com ... 

![Screenshot from 2024-03-31 20-56-33](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/baf78eff-0ed8-4828-93c3-4580f11cee6d)

8. Suggested amount to get started is to select to add $10 to your account's "credit balance". Then you can see how much you use PDF Bookclub and how much you're spending in order to use it 

## STEP 3 - GENERATING AND STORING A "SECRET KEY" ON YOUR MACHINE
Next, we will generate and store what is called a "secret key" for your access to the app on your machine. After this step you will have three things to keep track of (1) your OpenAI API Key (2) your OpenAI Org ID and (3) your "Secret Key"

1. Open your terminal anew (Terminal on MacOS, Command Prompt or PowerShell on Windows, and Terminal in Linux).
2. Make sure you are in the app directory 
   ```
   cd pdf_bookclub
   ```

3. Use the following command to create a new `secret.txt` file:
   ```
   touch secret.txt
   ```

4. Open the `secret.txt` file using a text editor of your choice. For simplicity, you can use `nano` in terminal:
   ```
   nano secret.txt
   ```

5. Insert the following lines, replacing the placeholders with your actual keys:
   ```
   SECRET_KEY=[insert secret key you've generated, which looks like sk-ahfg65334kgf or whatever you've set it as]
   ```

   You have two choices for what your secret key is (1) use the same key as your OpenAI API Key which you've saved into a text file already, or (2) generate a new authentic complex key, save it in a separate text file and then put that complex string in as your secret key. Just make sure you know where the two files are on your machine, (1) the text file that contains your OpenAI API Key and (2) the text file that contains your Secret Key

6. Save and exit (In your terminal in `nano`, press `CTRL+O` to write changes, then `CTRL+X` to exit).

## STEP 4 - DO YOU HAVE PYTHON ON YOUR MACHINE?

1. Open terminal window anew
2. Make sure you're in the app directory
   
   ```
   cd pdf_bookclub
   ```
3. Install if you are on a MacOS - HOMEBREW (MACOS) 
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
4. Install Python
    ```
   brew install python
   ```
5. Check to make sure you have Python, open terminal anew
   ```
   python3 --version
   ```
   
## STEP 5 - INSTALL DEPENDENCIES
   These are the parts that will make the app able to work, it is not uncommon that when you first try to run the app, you will have errors that appear, that are related to the completion of this step... most of them are easy to fix, though

1. Open terminal anew, then go to the app directory
   ```
   cd pdf_bookclub
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Get nltk and punkt set up
    ```
   pip install nltk
   ```
4. Then start a python session
   ```
   python3
   ```
5. Then for punkt...
   ```
   import nltk
   nltk.download('punkt')
   ```
6. This will open the NLTK Downloader, a graphical interface that might appear in a new window depending on your system settings. If it doesn't open a GUI, it will run in the terminal. From there, it will download the punkt package, which includes a pre-trained tokenizer for several languages.

   Exit Python Shell: After the download is complete, you can exit the Python shell by typing exit() or pressing Ctrl+D.
   
## STEP 6 - ENVIRONMENT VARIABLES

This is by far the biggest cause for errors when trying to run the app. Before using the web app, you must set the following environment variables. You would likely have to do this step everytime you restart your machine, or change wi-fis or things like that... If these exports aren't set, you will receive a 500 error when running the app:

```
export SECRET_KEY=<YourSecretKey, might look like sk-gah827656ajhhah>
export OPENAI_API_KEY=<YourAPIKey, might look like sk-gah827656ajhhah>
export OPENAI_ORG_ID=<YourOrgID, might look like org-abnfhg782fjna>
```

Replace the values inside the angle brackets <> with your actual saved values.

## STEP 7 - USING THE WEB APP
It's not unusual that there might be an error or two here, but you should be just about there. Let's test it:

1. In your terminal, navigate to the directory of the project:
   ```
   cd pdf_bookclub
   ```

2. Run:
   ```
   python3 app.py
   ```
3. Success looks something like this in your terminal:

![InShot_20240331_231027227](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/b685043c-445b-4043-b58f-6ed84b7f8cb7)

4. Going to the browser to use the app
   In the terminal it should have two lines that say "Running on..." those web links, that look something like http://127.0.0.1:4000 ... you highlight that link and right click it and select "open link" to navigate to the web page where the app should be running

5. If the webpage doesn't show and says "Internal Server Error", there is likely an error in "setting" the environment variables, the step where you did "export SECRET_KEY=.... etc.". In your terminal, it should say more about what is causing the error. If it says anything about keys, try doing the 3 export commands again:

```
export SECRET_KEY=<YourSecretKey, might look like sk-gah827656ajhhah>
export OPENAI_API_KEY=<YourAPIKey, might look like sk-gah827656ajhhah>
export OPENAI_ORG_ID=<YourOrgID, might look like org-abnfhg782fjna>
```
6. If the webpage shows, great! You should be able to click the button to upload your pdf. Then you click "generate". Then, the next page should show the text, separated into what are called "segments". The images at the top of this readme file show what this should look like...

If you click the "format text (rough)" button it will format the text into a readible format, with a blue highlight, and you can push the right arrow on your keyboard to have the highlighted text move along as you read the text. 

If you go to the bottom of any Segment, and click the "generate discussion" button, and then you get an "error" response, there could be a couple things happening... (1) another key error, check your terminal to see (2) there's something wrong with your connection to OpenAI API, this could be due to billing, or something like that


## ABOUT THE APP

This Flask/Jinja web app lets users upload a PDF. Upon upload, the PDF's text is segmented by token number. Each segment has a "generate discussion" button which uses OpenAI's ChatGPT-4 API to stimulate a discussion based on that segment. Note: Clicking "generate discussion" is estimated to cost ~$0.10 per generation from your API account.

Users can also relate passages to their terms using an input box. You can do things such as (1) copy and paste a segment of the text if you want your Bookclub partners to relate their discussion primarily to that section, or type in custom things to have your Bookclub partners draw parallels between the words you input and the segment of text they've read.

### Blue Cursor

The blue cursor appears when you click "format text (rough)" and is meant to help you keep track of where you are while you read. Now, when you go and click, "generate discussion" a new blue cursor appears in the text that displays the Bookclub discussion. That is now the cursor that your right arrow key is controlling. So if you ever notice the blue cursor stopped working, it is almost always because you've generated a new blue cursor somewhere else on the webpage. 

Enjoy PDF Book Club!
