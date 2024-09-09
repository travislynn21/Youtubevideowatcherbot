from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def check_video_playing(driver):
    try:
        # Locate the video element
        video = driver.find_element(By.TAG_NAME, 'video')

        # Check if the video is playing
        is_playing = driver.execute_script("return arguments[0].paused === false;", video)
        return is_playing
    except Exception as e:
        print(f"An error occurred while checking video status: {e}")
        return False

def restart_browser(url):
    iteration = 0
    while True:
        iteration += 1
        print(f"Iteration: {iteration}")

        # Initialize the WebDriver (e.g., Chrome)
        driver = webdriver.Chrome()

        try:
            # Open the webpage with the video
            driver.get(url)

            # Wait for the page to load
            time.sleep(5)

            # Check if the video is playing
            if check_video_playing(driver):
                print("The video is playing.")
            else:
                print("The video is not playing.")
        finally:
            # Close the browser
            driver.quit()

# Example usage
restart_browser("https://www.example.com")
