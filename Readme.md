# Typing Speed Test Using Selenium

This is a program that automates the simple English typing test on [https://10fastfingers.com/](https://10fastfingers.com/) using [Selenium](https://www.selenium.dev/).

The program is for learning purposes only.

## Usage

Install the needed Python modules from the `requirements.txt` file using the following command:

`pip install -r requirements.txt`

In order to be able to run Selenium, you have to install a web driver compatible with your browser.

The program is built to run with Chrome, so install the latest web driver [Chrome web driver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version.

To check your browser's version, go to "Help -> About Google Chrome"

![About Chrome](./images/about-chrome.png)

The version is 95

![Chrome Version](./images/chrome-version.png)

After installing the driver and exporting it, you need the path to where it is located, this path needs to be in the code.

You have to copy the path and CHANGE THE CODE at line eleven to

`PATH = "yourpath"`

> If you don't follow these instructions the code will not run!

Check this blog for an explanation of the code [https://ahmadhamze.github.io](https://ahmadhamze.github.io/posts/automation/selenium-speed-test/)

## License

Copyright &copy; 2021 Ahmad Hamze

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
