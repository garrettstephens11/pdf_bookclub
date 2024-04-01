# PDF Book Club Web Application

## CREDITS
All code and code-related edits have been written and generated by OpenAI's ChatGPT-4 Code Interpreter.

## LICENSE
This project is under the GNU General Public License. This means you can use, modify, and distribute this software, but any changes or derived works must also be shared under the same license. For more details, see the full text of the GPL.

## EXAMPLES OF WHAT THE WORKING APP LOOKS LIKE
This is a python app that runs on flask,aand you will host it in your localhost on a web browser. You need to be connected to wi-fi in order for the app to work properly, because in order to generate the bookclub discussions, it needs to make calls to the OpenAI API. Here's examples of what it looks like when it is working:

![Screenshot from 2024-03-31 20-57-28](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/978f3aa5-f132-46f5-95c7-adc909f20d4a)
![Screenshot from 2024-03-31 20-57-46](https://github.com/garrettstephens11/pdf_bookclub/assets/132736118/41919a15-fe92-47a3-b816-560a2175e552)

## GETTING STARTED
Get this thing up and running on your machine from scratch

## GENERATING AND STORING A SECRET KEY

1. Navigate to the terminal (Terminal on MacOS, Command Prompt or PowerShell on Windows, and Terminal in Linux).

2. Use the following command to create a new `secret.txt` file:
   ```
   touch secret.txt
   ```

3. Open the `secret.txt` file using a text editor of your choice. For simplicity, you can use `nano` in terminal:
   ```
   nano secret.txt
   ```

4. Insert the following lines, replacing the placeholders with your actual keys:
   ```
   OPENAI_API_KEY=[insert api key you've generated]
   SECRET_KEY=[insert secret key you've generated]
   ```

5. Save and exit (In `nano`, press `CTRL+O` to write changes, then `CTRL+X` to exit).

## ENVIRONMENT VARIABLES

Before using the web app, you must set the following environment variables. If these aren't set, you will receive a 500 error when running the app:

```
export SECRET_KEY=<YourSecretKey>
export OPENAI_API_KEY=<YourAPIKey>
export OPENAI_ORG_ID=<YourOrgID>
```

Replace the values inside the angle brackets <> with your actual saved values.

## SETTING UP THE LOCAL REPOSITORY

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

If you encounter git issues, please visit https://chat.openai.com for assistance.

## VERIFYING GIT SETUP

Follow the given steps in the terminal:

1. `git remote -v` - Check if you are connected to the remote repository.
2. `git status` - Verify the status of your repository.
3. If local doesn't match remote:
   ```
   git pull origin main
   ```
4. Ensure sync:
   ```
   git pull origin main
   ```

You should see "Everything up-to-date".

## INSTALLING DEPENDENCIES

Depending on your OS:

**Windows:**
```
pip install Flask [other libraries]
```

**MacOS/Linux:**
```
pip3 install Flask [other libraries]
```

Replace `[other libraries]` with any other dependencies you need.

## USING THE WEB APP

1. In your terminal, navigate to the directory of the project:
   ```
   cd path_to_directory/pdf_bookclub
   ```

2. Run:
   ```
   python3 app.py
   ```

## ABOUT THE APP

This Flask/Jinja web app lets users upload a PDF. Upon upload, the PDF's text is segmented by token number. Each segment has a "generate discussion" button which uses OpenAI's ChatGPT-4 API to stimulate a discussion based on that segment. Note: Clicking "generate discussion" is estimated to cost ~$0.10 per generation from your API account.

Users can also relate passages to their terms using an input box. The "format text ~3" button sends segments to OpenAI's ChatGPT-4 for reformatting, which costs ~$0.10. The "format text (rough)" option doesn't use the API and is free. After selecting "format text (rough)", sentences are highlighted for readability. The right arrow key lets users navigate these sentences.

Enjoy PDF Book Club!
