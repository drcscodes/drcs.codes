## Install WSL2 (Windows 10/11)

If you are using Windows 10 or 11, install WSL2, the Windows Subsystem for Linux, Version 2.  WSL2 provides a very nice Linux environment, including a full Linux kernel and distribution of yoru choosing (I will use the latest Ubuntu in demonstrations).  You can install the Windows version of Python and all the other tools used in this course, but Python is primarily a Linux/Unix technology and all course demonstrations on Windows will use WSL2.

Install WSL2 (See detailed instructions at https://docs.microsoft.com/en-us/windows/wsl/install-win10#simplified-installation-for-windows-insiders.  Note that Windows 10 with all updates from 2021-07-29 and later should support the simplified install.)

1. Start PowerShell in admin mode by typing Windows+R, typing `powershell` in the text box, and running it with Ctrl-Enter.
2. On the PowerShell command line, enter `wsl --install`.
3. Install Windows Terminal: https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701

Now you have WSL installed.  In a WSL terminal window, proceed with the Ubuntu steps below.

- `sudo apt install python3`
