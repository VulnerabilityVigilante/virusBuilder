<!DOCTYPE html>
<html>
<body>
	<h1>Virus Builder 1.0.3</h1>
	<p>Virus Builder is a Python program that lets you create a custom virus file with a custom alert box, as well as the optional functionality of browser spamming. This program is created by VulnerabilityVigilante.</p>
	<h2>Usage</h2>
	<ol>
		<li>Run the <code>virusBuilder.py</code> script to start the program.</li>
		<li>Enter the name of the virus file you want to create (without the file extension).</li>
		<li>Choose whether you want to include a custom alert box in the virus file or not.</li>
		<li>If you choose to include a custom alert box, enter the message you want to display in the box.</li>
		<li>The program will create a new file in your Downloads folder with the name you specified, and add the virus code to it.</li>
	</ol>
	<h2>How it works</h2>
	<p>The program creates a batch file with a few lines of code that will run the cmd command prompt and execute a PowerShell script. It also creates a scheduled task that will run the virus file when the system starts up. If you choose to include a custom alert box or browser spam, the program will append code to the virus file with the message you specified.</p>
	<h2>Disclaimer</h2>
	<p>This program is for educational purposes only. The author does not condone or endorse the creation or distribution of malicious software. Use this program at your own risk. The author is not responsible for any damages or legal consequences that may result from the use of this program.</p>
</body>
</html>
