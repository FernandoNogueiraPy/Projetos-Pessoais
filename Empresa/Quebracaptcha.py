frames = chrome.find_elements(By.TAG_NAME,'iframe')
    chrome.switch_to.frame(frames[0])
    time.sleep(1)
    
    chrome.find_element(By.CLASS_NAME,'recaptcha-checkbox-border').click()

    time.sleep(3)

    chrome.switch_to.default_content()
    frames=chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_g_recaptcha"]/div/div/iframe')
    chrome.switch_to.frame(frames)

    time.sleep(1)

    frame_button = chrome.find_elements(By.TAG_NAME,'iframe')
    chrome.switch_to.frame(frame_button[0])
    chrome.find_element(By.ID,"recaptcha-audio-button").click()