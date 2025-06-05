# Host Bedrock Server on Codespace
![image](https://github.com/user-attachments/assets/ded7f18b-e2aa-4b5a-8a92-c1d0a8a7974c)

# Check Server Online Status
![image](https://github.com/user-attachments/assets/6a2b123e-ad52-402b-a6ed-480adca2a57e)
![image](https://github.com/user-attachments/assets/4bf5bc6f-e7bf-4981-91f2-8b02ba933aa7)

# How to Host a Minecraft Bedrock Server on GitHub Codespaces: A Step-by-Step Guide

Minecraft Bedrock Edition offers cross-platform play, and running a dedicated server can provide a stable and customizable environment for players. GitHub Codespaces offers a cloud-based development environment where you can easily host a Minecraft Bedrock server. In this guide, we’ll show you how to set up a Minecraft Bedrock server on GitHub Codespaces, step-by-step, including all the necessary commands.

### Prerequisites

Before you begin, make sure you have the following:

* A GitHub account.
* A GitHub repository where you will host your Minecraft server.
* A GitHub Codespace setup for your repository.

### Step 1: Create a GitHub Repository

First, create a GitHub repository to store the Minecraft Bedrock server files. Here’s how:

1. Navigate to GitHub and log into your account.
2. Click the "New" button on your GitHub dashboard.
3. Fill out the repository name, description, and make it public or private as desired.
4. Once created, clone the repository to your local machine if necessary.

### Step 2: Set Up GitHub Codespace

GitHub Codespaces provides a cloud-based IDE, which we can use to run the server. Follow these steps to create a Codespace for your repository:

1. In your repository on GitHub, click the green **Code** button.
2. Select **Open with Codespaces** and then click **New codespace**.
3. GitHub will create a new Codespace environment where you can run your server. This environment comes with a terminal where you can run commands.

### Step 3: Install Dependencies in Codespace

Once your Codespace is set up, you need to install some dependencies to run the Minecraft Bedrock server.

1. **Open a terminal** in your GitHub Codespace.

2. **Install `wget` and other required tools**:

   ```bash
   sudo apt update
   sudo apt install -y wget unzip screen
   ```

3. **Install Minecraft Bedrock Server**:
   Use the `wget` command to download the latest Minecraft Bedrock Edition server files.

   ```bash
   wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.19.81.01.zip
   ```

   This command will download the latest version of the Minecraft Bedrock server.

4. **Unzip the downloaded file**:

   ```bash
   unzip bedrock-server-1.19.81.01.zip
   ```

   This will extract the contents of the ZIP file to a directory.

### Step 4: Configure the Server

Now, configure the Minecraft server to your liking. You can modify settings such as game mode, maximum players, and other server options.

1. **Navigate to the extracted server directory**:

   ```bash
   cd bedrock-server
   ```

2. **Edit the `server.properties` file** to configure your server settings:

   ```bash
   nano server.properties
   ```

   Adjust settings like the `server-name`, `gamemode`, `difficulty`, and more. Save and close the file once you’ve made your changes (`Ctrl + X`, then `Y` to confirm).

### Step 5: Run the Server in a Screen Session

To keep the Minecraft Bedrock server running continuously on Codespaces, you should run it inside a `screen` session.

1. **Start a new screen session**:

   ```bash
   screen -S minecraft-bedrock
   ```

   This creates a new virtual terminal session for running your server.

2. **Run the Minecraft Bedrock server**:

   Inside the screen session, execute the following command to start the server:

   ```bash
   ./bedrock_server
   ```

   The server will start, and you'll see logs outputting in the terminal. You can now leave this screen session running, and your server will continue to run in the background.

3. **Detach from the screen session**:

   To detach from the screen session (but leave the server running in the background), press:

   ```bash
   Ctrl + A, then D
   ```

   This will return you to the main terminal, while the Minecraft server continues running in the background.

4. **Reattach to the screen session**:

   If you need to check the server’s status or make adjustments, you can reattach to the session with:

   ```bash
   screen -r minecraft-bedrock
   ```

### Step 6: Expose the Server to the Internet (Optional)

To make your Minecraft Bedrock server accessible from the internet, you will need to forward the necessary port (default is 19132 for Bedrock Edition). If you are using GitHub Codespaces, follow these steps:

1. **Expose the port using Codespaces**:
   On GitHub Codespaces, you can expose the server’s port so that it is accessible externally. Go to the **Ports** tab in the Codespace interface and look for port 19132.

2. **Set up port forwarding**:
   If Codespaces does not automatically expose the port, you may need to modify network settings or use a tunneling service like [Playit](https://playit.gg/) (which you seem to be using) to expose the port.

   For example, if you're using Playit, run:

   ```bash
   playit --server 127.0.0.1:19132
   ```

   This command will forward your local server port (19132) to a public endpoint.

### Step 7: Automate Server Start with a Script

If you want to automate the server start process each time you start the Codespace, you can create a shell script.

1. **Create the script**:

   Inside your server directory, create a file called `start_server.sh`:

   ```bash
   nano start_server.sh
   ```

   Add the following content to the script:

   ```bash
   #!/bin/bash
   ./bedrock_server > logs.txt 2>&1
   ```

2. **Make the script executable**:

   ```bash
   chmod +x start_server.sh
   ```

3. **Run the script**:

   You can now start the server by running the script:

   ```bash
   ./start_server.sh
   ```

### Step 8: Monitor and Manage Your Server

While the server is running, you can monitor its logs and activity. For example, you can:

* View the server logs by opening `logs.txt`.
* Reattach to the screen session if you need to issue commands to the server.
* Stop the server by using the `Ctrl + C` command inside the screen session.

### Step 9: Access the Server

To connect to your Minecraft Bedrock server, use the IP address and port exposed by GitHub Codespaces or the Playit tunnel (if you're using one). Open Minecraft Bedrock Edition and enter the IP and port to join.

### Conclusion

With GitHub Codespaces, setting up a Minecraft Bedrock server is simple and allows you to have a persistent cloud-hosted server for your friends or public gameplay. The power of the cloud means that the server runs 24/7 without needing to keep your own machine on all the time. By following this guide, you should be able to create and manage a Minecraft Bedrock server on GitHub Codespaces with ease.

Enjoy your Minecraft world!
