def android_get_desired_capabilities():
    return {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "deviceName": "127.0.0.1:62001",
        "udid": "127.0.0.1:62001",
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',

        # 'autoGrantPermissions': True,
        # 'automationName': 'uiautomator2',
        # 'newCommandTimeout': 500,
        # 'noSign': True,
        # 'platformName': 'Android',
        # 'platformVersion': '10',
        # 'resetKeyboard': True,
        # 'systemPort': 8301,
        # 'takesScreenshot': True,
        # 'udid': '11bd127d',
        # 'appPackage': 'com.ajaxsystems',
        # 'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
