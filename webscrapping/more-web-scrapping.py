##** selenium docs: https://selenium-python.readthedocs.org

from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://automatetheboringstuff.com')

# use a selector to find the element
elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
elem.click() # simulate a click

elems = browser.find_elements_by_css_selector('p') # returns a list of elements that match the selector, p
print(len(elems))

# simulate typing into a search field
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie') # simulate typing into seach field
searchElem.submit() # submit the form

# text element
elem = browser.find_element_by_css_selector('body > div > div > div > div > header > div > div > div > div > div > div > div > div > div > div > div > div > div > div > h1')
print(elem.text)

# simulate clicking the back button
browser.back()

# simulate clicking the forward button
browser.forward()

# simulate clicking the refresh button
browser.refresh()

# simulate clicking the home button
browser.home()

# close the browser
browser.quit()