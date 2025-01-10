# Simple Flask App

1. Run

```bash
uv sync
```

If you do not have `uv` installed, you can install it by running:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create '.env' file (simply copy file .env.sample):

3. Run

```bash
docker compose up d db
```

to create an docker container

4. Development and debugging

   This project contains both Flask and FastAPI.

   To run Flask app:

   - go to "Run and Debug" tab in VSCode and select "Python:Flask" from dropdown menu

   To run FastAPI app:

   - go to "Run and Debug" tab in VSCode and select "API" from dropdown menu

   After selection, press `"Run and Debug"` button or `F5` key on keyboard

5. Create db with command

```bash
flask db upgrade
```

6. In main folder need install node_modules to work with tailwind, run

```bash
yarn
```

7. Unpack signal bot config.


   Get archive with signal bot config (`signal-cli-config.tar.gz`) from the team and unpack it to the root of the project using this command:

   ```bash
   tar -xvzf signal-cli-config.tar.gz
   ```

## Signal bot configuration

   Before you start you need to have a dedicated phone number for the bot. You can use your personal phone number but it's not recommended because it will unregister your Signal app.

1. Launch bot container

   ```bash
   docker compose up bot
   ```

2. Get captcha code. To get the token, go to https://signalcaptchas.org/registration/generate.html

   You need to open the page on the same device that runs the signal-cli register command (or at least a device that has the same external IP address).

   (If the token from that page doesn't work, you can try https://signalcaptchas.org/challenge/generate.html)

   After filling the captcha, the site doesn't immediately show the token but tries to redirect to a signalcaptcha:// url that contains the token.

   After a short moment, a link will appear underneath the captcha called "Open Signal".

3. Register phone number.

   get into the bot container

   ```bash
   docker compose  exec signal bash
   ```

   Get the token by right clicking on it and clicking: copy url. You can paste that directly into:

   ```bash
   signal-cli --config /home/.local/share/signal-cli -u  < phone_number_here > register --captcha < what_you_copied >
   ```

4. Verify phone number

   You will receive a verification code on your phone number. You can paste that directly into:

   ```bash
   signal-cli --config /home/.local/share/signal-cli -a  < phone_number_here > verify < verification_code >
   ```
5. Leave the container

   ```bash
   exit
   ```

Now the bot is ready to use. To send a sample message do:

   ```bash
   $ curl -X POST -H "Content-Type: application/json" 'http://localhost:8080/v2/send' \
     -d '{"message": "Test via Signal API!", "number": "+4412345", "recipients": [ "+44987654" ]}'
   ```

### Update Signal bot setup at stage/production environment (Optional):

1. Create a new archive with the updated signal bot config:

   ```bash
   tar --exclude '*.db' -czvf  signal-cli-config.tar.gz signal-cli-config
   ```
2. Convert the archive to base64:

   ```bash
   base64 -i signal-cli-config.tar.gz -o signal-cli-config.tar.gz.base64
   ```

3. Set the SIGNAL_BOT_CONFIG_BASE64 secret at repo settings in Github to the content of the signal-cli-config.tar.gz.base64 file.


## How to work with translations (i18n)
1. In HTML you need to write text in special brackets
(the text language must be the default language for your project):
```bash
<h1>{{_("Your text")}}</h1>
```
2. Run scripts in this order:
```bash
./translate-compile.sh
```
```bash
./translate-update.sh
```
3. Go to the `messages.po` file and check the text, it should be:
```bash
#: svarog/templates/your-template.html:10 <--- your file path and text line
#, fuzzy <--- this means that you need to check whether the text was compiled correctly
msgid "Your text"
msgstr "" <--- here you need to insert your text in another language
```
**It is important to remove `#, fuzzy`, otherwise the translation won't be applied.**

How it should look after the changes:
```bash
#: svarog/templates/your-template.html:10
msgid "Your text"
msgstr "Ваш текст"
```

4. Repeat `step 2`
5. Restart `debugger`
