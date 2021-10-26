# This is a project intending to test the typing speed of Selenium

You need to install the latest web driver [Chrome web driver](https://sites.google.com/chromium.org/driver/)

## Trying to grab all the words to type

If you try to grab all the words to type, you will be able to grab around 20 of them, the rest of the words will be empty strings!

## Solution

Grabbing all the words is successful! I used the requests-html library to parse the selenium object "driver.page_source".

There is a something that I don't understand yet, when this line is removed

`wordsContainer.find_elements(By.TAG_NAME, "span")`

the words cannot be reached (we have an empty div), the above code seems useless at the first glance, but it's crucial to getting the words.
