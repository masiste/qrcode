https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys

Checking for existing SSH keys

    $ ls -al ~/.ssh


https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Generating a new SSH key

    Open TerminalTerminalGit Bash.

    $ ssh-keygen -t ed25519 -C "your_email@example.com"

    > Enter a file in which to save the key

    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]


Adding your SSH key to the ssh-agent

    Start the ssh-agent in the background

    $ eval "$(ssh-agent -s)"
    > Agent pid 59566


https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

Adding a new SSH key to your GitHub account

    Copy the SSH public key to your clipboard

    In the upper-right corner of any page, click your profile photo, then click Settings.

    In the user settings sidebar, click SSH and GPG keys.

    Click New SSH key or Add SSH key.

    In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal Mac, you might call this key "Personal MacBook Air".

    Paste your key into the "Key" field.

    Click Add SSH key.

    If prompted, confirm your GitHub password.


https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection

Testing your SSH connection

    Open TerminalTerminalGit Bash.

    Enter the following:

        $ ssh -T git@github.com

        > Hi username! You've successfully authenticated, but GitHub does not
        > provide shell access.

-----------------------------------------------------------
Problem with access from console cmd

    Authentication failed for 'https://github.com/masiste/qrcode.git/'

https://stackoverflow.com/questions/69979522/fatal-authentication-failed-for-when-pushing-to-github-from-visual-studio-cod

I faced this problem.... TO fix it, you should simply follow these steps:

- Go to your github profile settings
- Select Developer section and go to Personal Access token
- Create a new acces Token ( Copy it as soon as it has been generated )
- Then try to push some changes in your repository, you will be asked to put username and password
- For the password, just paste the access token you just copied

----------------------------------------------------------------

config vscode terminal autentication

select icon manage in the main bar

manage > settings > extensions > git > enable terminal autentication
