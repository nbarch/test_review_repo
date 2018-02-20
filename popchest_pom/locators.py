from selenium.webdriver.common.by import By

#todo пересмотреть локаторы, многие протухли
class SidebarLocators(object):
    POPULAR      = (By.XPATH, '//div[@id="sidenav"]//a[@href="/popular"]')
    TOP          = (By.XPATH, '//div[@id="sidenav"]//a[@href="/top"]')
    RECENT       = (By.XPATH, '//div[@id="sidenav"]//a[@href="/recent"]')
    SERIES       = (By.XPATH, '//div[@id="sidenav"]//a[@href="/series"]')
    CAT_COMEDY   = (By.XPATH, '//div[@id="sidenav"]//a[@href="/c/comedy"]')
    CAT_TECH     = (By.XPATH, '//div[@id="sidenav"]//a[@href="/c/tech"]')
    CAT_POLITICS = (By.XPATH, '//div[@id="sidenav"]//a[@href="/c/politics"]')
    CAT_CINEMA   = (By.XPATH, '//div[@id="sidenav"]//a[@href="/c/cinema"]')
    CAT_GAMING   = (By.XPATH, '//div[@id="sidenav"]//a[@href="/c/gaming"]')
    ADD_FUNDS    = (By.XPATH, '//div[@id="sidenav"]//button')
class HeaderLocators(object):
    MENU_SIDENAV = (By.XPATH, '//button[@type="button""]//i[@class="fa fa-bars"]')
    LOGO         = (By.CSS_SELECTOR, '.navbar-brand')
    SEARCH_INPUT = (By.NAME, 'q')
    LOGIN = {'by': 'By.CSS_SELECTOR', 'value': '#navbar .menu-link.login-link'}
    JOIN = (By.CSS_SELECTOR, '#navbar li.btn-join-us a')
    LEARN  = (By.CSS_SELECTOR, '.btn.btn-border.transition')
    UPLOAD       = (By.CSS_SELECTOR, '.navbar-header ul div.wallet-balance')
    MY_WALLET    = (By.XPATH, '//header//div[@class="wallet-balance  pull-left"]')
    DROPDOWN = (By.CSS_SELECTOR, '.dropdown-menu.dropdown-user')
    DROPDOWN_WATCHED = (By.XPATH, '//header//a[@href="/"]')
    DROPDOWN_MY_VIDEOS = (By.XPATH, '//header//a[@href="/studio"]')
    DROPDOWN_MY_SERIES = (By.XPATH, '//header//a[@href="/"]')
    DROPDOWN_PROFILE = (By.XPATH, '//header//a[@href="/"]')
    DROPDOWN_PASSWORD = (By.XPATH, '//header//a[@href="/"]')
    DROPDOWN_WALLET = (By.XPATH, '//header//a[@href="/"]')
    DROPDOWN_LOGOUT = (By.XPATH, '//header//a[@data-qa="drop-down-menu-link"]')

class FooterLocators(object):
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.menu-link.search-link')
    ABOUT        = (By.CSS_SELECTOR, '#footer-navbar .menu-link[href="/about"]')
    LOGIN_FOOTER = (By.CSS_SELECTOR, '#footer-navbar .menu-link.login-link')
    JOIN_FOOTER  = (By.XPATH, '//div[@id="footer-navbar")/ul/li[4]')
    POP_TOKEN    = (By.XPATH, '//div[@id="footer-navbar")/ul/li[5]')
    LEARN_FOOTER = (By.XPATH, '//div[@id="footer-navbar")/ul/li[6]')
    HELP         = (By.XPATH, '//div[@id="footer-navbar")/ul/li[7]')
    IG           = (By.CSS_SELECTOR, 'instagram')
    FB           = (By.CSS_SELECTOR, 'facebook')
    TW           = (By.CSS_SELECTOR, 'twitter')
class ForgotPageLocators(object):
    EMAIL_INPUT     = (By.NAME, 'email')
    SUBMIT_BUTTON   = (By.XPATH, '//button[@type="submit"]')
    CREATE_ACC      = (By.XPATH, '//a[@href="/account/signup"][contains(text(),"Create Account")] ')
class LoginPageLocators(object):
    EMAIL       = {'by': 'By.ID', 'value': 'emailInput'}
    PWD         = {'by': 'By.ID', 'value': 'passwordInput'}
    LOG_IN      = {'by': 'By.CSS_SELECTOR', 'value': '.panel-body button.btn'}
    FORGOT_PWD  = {'by': 'By.CLASS_NAME', 'value': 'forgot-password-link'}
    JOIN_TWITTER= {'by': 'By.CLASS_NAME', 'value': 'connect-auth connect-twitter login'}
    JOIN_FB     = {'by': 'By.CLASS_NAME', 'value': 'connect-auth connect-facebook login'}
    TERMS       = {'by': 'By.PARTIAL_LINK_TEXT', 'value': '/terms-of-use'}
    PRIVACY     = {'by': 'By.PARTIAL_LINK_TEXT', 'value': '/privacy-policy'}
    JOIN        = {'by': 'By.XPATH', 'value': '//div[@class="text-center bottom-extra"]//a[@href="/account/signup"]'}
    ALERT       = {'by': 'By.CSS_SELECTOR', 'value': '.alert.alert-danger'}
class MainPageLocators(object):
    MODAL_WATCH_BUTTON  = (By.CSS_SELECTOR, '#welcome-beta .modal-footer button')
    MODAL_CLOSE_BUTTON  = (By.CSS_SELECTOR, '#welcome-beta .modal-header button')
    # The Spotlight section
    SP_AVATAR       = (By.CSS_SELECTOR, '.user-info-box div a img')
    SP_VIDEO        = (By.CSS_SELECTOR, 'div.video-list-item div.video-thumb.big-thumb')
    # Для PLAY BUTTON слишком общий селектор, если надо взаимодействовать с видео из Spotlight,надо брать 1 эл-т массива
    PLAY_BUTTON     = (By.CSS_SELECTOR, 'div.video-thumb-hover-actions.transition > div.play-icon')
    # Creators - массив из 10 эл-тов
    CREATORS = (By.CSS_SELECTOR, '#featured-creators .creator-list div.avatar')

    # Featured videos section
    VIEW_ALL_VIDEOS     = (By.CSS_SELECTOR, '#newest-videos div.heading-section a')
    NEXT_BUTTON         = (By.CSS_SELECTOR, '.flexslider div a.flex-next')
    PREV_BUTTON         = (By.CSS_SELECTOR, '.flexslider div a.flex-prev ')
    VIDEOS              = ()
    # Categories
    VIEW_ALL_CATS       = (By.CSS_SELECTOR, '#explore-categories div a.view-all')
    COMEDY              = (By.CSS_SELECTOR, '.category.transition.category-comedy')
    TECH                = (By.CSS_SELECTOR, '.category.transition.category-tech')
    POLITICS            = (By.CSS_SELECTOR, '.category.transition.category-politics')
    CINEMA              = (By.CSS_SELECTOR, '.category.transition.category-cinema')
    GAMING              = (By.CSS_SELECTOR, '.category.transition.category-gaming')
    LEARN_FOOTER        = (By.CSS_SELECTOR, '#creator-cta div a')
class VideoPageLocators(object):
    LOAD_MORE = (By.CSS_SELECTOR, '.content button')
    GET_USER_VIDEOS = (By.CSS_SELECTOR, '#videos-uploaded li.video-list-item')
    SHARE           = (By.CSS_SELECTOR, '.video-action-bar .share-links .share button')
    LIKE            = (By.CSS_SELECTOR, '.video-action-bar .share-links .vote button')
    SKIP_PREVIEW    = (By.CSS_SELECTOR, '#skip-preview-overlay img')
    CATEGORY        = (By.CSS_SELECTOR, '')
    FOLLOW          = (By.CSS_SELECTOR, '.video-details button')
    PROFILE         = (By.CSS_SELECTOR, '')
    FOOTER_LIKE     = (By.CSS_SELECTOR, '')
    FOOTER_SHARE    = (By.CSS_SELECTOR, '')
    COMMENT_INPUT   = (By.CSS_SELECTOR, '')
    COMMENT_POST    = (By.CSS_SELECTOR, '')
    COMMENT_VOTE    = (By.CSS_SELECTOR, '')
    COMMENT_USER    = (By.CSS_SELECTOR, '')

class ProfilePageLocators(VideoPageLocators):
    # Profile input text fields
    PROFILE = {
        'AVATAR'     : ['By.CSS_SELECTOR', '.avatar-wrap img'],
        'EMAIL'      : ['By.ID', 'emailInput'],
        'FIRST_NAME' : ['By.ID', 'firstnameInput'],
        'LAST_NAME'  : ['By.ID', 'lastnameInput'],
        'BIO'        : ['By.ID', 'aboutMe'],
        'WEBSITE'    : ['By.ID', 'websiteInput'],
        'YOUTUBE'    : ['By.ID', 'youtubeChannelId']
    }
    USERNAME            = (By.NAME, 'username')
    NEW_PWD             = (By.NAME, 'newPassword')
    CONF_NEW_PWD        = (By.NAME, 'confirmNewPassword')
    BTC_ADDR            = (By.NAME, 'payoutAddress')
    COINBASE            = (By.LINK_TEXT, '/auth/coinbase')
    # This button is used in: Update profile, update password, update wallet
    UPDATE      = (By.CSS_SELECTOR, '.panel-footer button')

    CONNECT_TW          = (By.LINK_TEXT, '/auth/twitter')
    CONNECT_FB          = (By.LINK_TEXT, '/auth/facebook')
    CONNECT_COINBASE    = (By.LINK_TEXT, '/auth/coinbase')
    CONNECT_GOOGLE      = (By.LINK_TEXT, '/auth/google')
    # эти два внизу не обработаны
    FOLLOW              = (By.CSS_SELECTOR, '.user-info-box button')
    SUBSCRIBE_YOUTUBE   = (By.CSS_SELECTOR, '#yt-subscribe')
class WalletPageLocators(object):
    ADD_FUNDS           = (By.CSS_SELECTOR, 'div.wallet-reload-btn')
    REFUND_BUTTON       = (By.CSS_SELECTOR, '.refund-button')
    PAY_5               = ('By.XPATH', '//*[@id="panel-first"]//button[1]')
    PAY_10              = ('By.XPATH', '//*[@id="panel-first"]//button[2]')
    PAY_20              = ('By.XPATH', '//*[@id="panel-first"]//button[3]')


class UploadVideoLocators(ProfilePageLocators):
    RESEND          = (By.LINK_TEXT, 'Resend confirmation')
    DROPZONE        = (By.CSS_SELECTOR, '.dropzone')
    UPDATE          = (By.CSS_SELECTOR, '.retry')
    TITLE           = ('By.NAME', 'title')
    DESCRIPTION     = ('By.NAME', 'description')
    PRICING_5       = ('By.CSS', '.price-options li[value="5")')
    PRICING_25      = ('By.CSS', '.price-options li[value="25"]')
    PRICING_99      = ('By.CSS', '.price-options li[value="99"]')
    UPLOAD_BUTTON   = (By.CSS_SELECTOR, '.actions>button')
    SELECT_FROM_VID = (By.CSS_SELECTOR, '.actions span button')
    BACK_BUTTON     = (By.CSS_SELECTOR, '.clear a')
    PUBLISH_BUTTON  = (By.CSS_SELECTOR, '.clear input[name="save-publish"]')
    DRAFT_BUTTON    = (By.CSS_SELECTOR, '.clear input[name="save-draft"]')

class StudioPageLocators(object):
    # PUBLISHED
    # DRAFT
    # SEARCH_VIDEO
    # SORT_DROPDOWN
    #
    pass







