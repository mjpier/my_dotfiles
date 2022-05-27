# Load settings added with ui
# See <https://github.com/qutebrowser/qutebrowser/blob/master/doc/help/configuring.asciidoc#loading-autoconfigyml>
# See list of userscripts: https://github.com/qutebrowser/qutebrowser/blob/master/misc/userscripts/README.md
# To se all configuration type :set inside qutebrowser
config.load_autoconfig(True)

c.content.blocking.method = 'adblock'
c.content.blocking.adblock.lists = [
        'https://easylist.to/easylist/easylist.txt',
        'https://easylist.to/easylist/easyprivacy.txt',
        'https://easylist.to/easylist/fanboy-social.txt',
        'https://easylist-downloads.adblockplus.org/easylistdutch.txt',
        'https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt',
        'https://www.i-dont-care-about-cookies.eu/abp/',
        'https://secure.fanboy.co.nz/fanboy-cookiemonster.txt',
        'https://secure.fanboy.co.nz/fanboy-annoyance.txt',
        #'https://gitlab.com/curben/urlhaus-filter/-/raw/master/urlhaus-filter.txt',
        'https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt',
        'https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt'
]

# Search engines
c.url.searchengines = {
        "DEFAULT": "https://www.google.fi/search?q={}",
        #"DEFAULT": "https://duckduckgo.com/?q={}",
        "aw": "https://wiki.archlinux.org/?search={}",
        "gw": "https://wiki.gentoo.org/?search-{}",
        "yt": "https://youtube.com/results?search_query={}",
        "w": "https://en.wikipedia.org/?search={}",
        #"g": "https://www.google.fi/search?q={}",
        "dgi": "https://duckduckgo.com/?q=!ddgi {}",
        "tw": "twitter.com/{}",
        "dick": "http://en.wiktionary.org/?search={}",
        "r": "https://reddit.com/r/{}",
}

# Aliases
c.aliases = {
    "w": "session-save",
    "wq": "quit --save",
    "mpv": "spawn -d mpv --profile=H60 {url}",
    'gh': "open -t https://github.com/mjpier",
    'wh': "open -t https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&topRange=1y&sorting=toplist&order=desc&colors=336600&page=1",
    'wt': "open -t https://www.webtoons.com/en/",
    'fb': "open -t https://facebook.com/",
    'ux': "open -t https://www.reddit.com/r/unixporn/",
    'tr': "open -t https://1337x.to/",
    'cc': "open -t https://jonasjacek.github.io/colors/",
    'od': "open -t https://odysee.com/",
    'bc': "open -t https://based.cooking/",
    'ax': "open -t https://animixplay.to/",
    'md': "open -t https://mp3quack.lol/",
    'suck': "open -t http://suckless.org/",
}

# Startpage
c.url.start_pages = ['~/.config/dev/startpage/index.html']
#c.url.start_pages = ['~/.config/qutebrowser/start.html']

# COLORS THEMME
import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

#
dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})


# Enable this if using style2.css in startpage
#c.colors.webpage.darkmode.enabled = True  # This will break my startpage
#c.colors.webpage.preferred_color_scheme = 'dark'
#c.colors.webpage.bg = 'black'

# Not sure how this works for now, i'll test this if i had time lol.
#c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
#c.colors.webpage.darkmode.policy.images = 'smart'
#c.colors.webpage.darkmode.policy.page = 'smart'
#c.colors.webpage.darkmode.threshold.background = 0
#c.colors.webpage.darkmode.threshold.text = 256

# General settings
c.backend = 'webengine'                             # value: webengine, webkit
c.editor.command = ["st", "-e", "nvim '{}'"]
c.scrolling.smooth = False
c.qt.highdpi = False
c.confirm_quit = ['downloads']
c.completion.height = '20%'
c.completion.show = 'always'
c.hints.scatter = True
c.zoom.default = '140%'
c.auto_save.session = False
c.changelog_after_upgrade = 'never'
c.qt.force_software_rendering = 'software-opengl'
c.content.geolocation = 'ask'                       # value: true, false, ask
c.content.prefers_reduced_motion = True             # minimize non-essentials animations and motion in websites.
c.content.cookies.accept = 'all'
c.content.dns_prefetch = True
c.content.autoplay = True
c.content.pdfjs = True
c.content.fullscreen.overlay_timeout = 3000
c.content.fullscreen.window = True

# Tabs
c.tabs.last_close = 'close'
c.tabs.select_on_remove = 'prev'
c.tabs.new_position.unrelated = 'next'
c.tabs.position = 'top'

# Notification
c.content.notifications.enabled = 'ask'             # value: true, false, ask
c.content.notifications.presenter = 'libnotify'     # value: auto, qt, libnotify, systray, messages, herbe(experimental)
c.content.notifications.show_origin = True

# Downloads
c.downloads.location.directory = '~/.config/dl'
c.downloads.location.prompt = False
c.downloads.remove_finished = 1000

# Font and define colors values
c.fonts.default_family = ['Inconsolata']
c.fonts.default_size = '18px'
c.fonts.web.family.cursive = 'Inconsolata'
c.fonts.web.family.sans_serif = 'Inconsolata'
c.fonts.completion.category = 'bold default_size default_family'
c.fonts.contextmenu = '16px default_family'

# Status bar padding
c.statusbar.padding = {
    'top': 5,
    'right': 5,
    'bottom': 5,
    'left': 5,
}


# Mappings
ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'
c.bindings.commands['normal'] = {
'<ctrl-x>': ESC_BIND,
}

config.bind('<ctrl-x>', 'leave-mode')
config.bind("K", "tab-next")
config.bind("J", "tab-prev")
config.bind("O", "set-cmd-text :open {url:pretty}")
config.bind("T", "set-cmd-text :open -t {url:pretty}")
config.bind("t", "set-cmd-text -s :open -t")
config.bind("z+", "zoom-in")
config.bind("z-", "zoom-out")
config.bind("zz", "zoom")
config.bind("h", "scroll-px -300 0")
config.bind("j", "scroll-px 0 300")
config.bind("k", "scroll-px 0 -300")
config.bind("l", "scroll-px 300 0")
config.bind('ya', 'spawn ytubeaudio {url}')
config.bind('yv', 'spawn ytubevideo {url}')
config.bind("<Alt-f>", "hint links spawn --detach mpv --profile=M60 {hint-url}")
config.bind("<Alt-Shift-f>", "hint links spawn --detach mpv --profile=H60 {hint-url}")
#config.bind("<Alt-f>", "hint links spawn --detach mpv --force-window yes {hint-url}")

config.bind('<Escape>', 'leave-mode ;; jseval -q document.activeElement.blur()', mode='insert')
config.bind('<Ctrl-x>', 'leave-mode ;; jseval -q document.activeElement.blur()', mode='insert')

c.bindings.commands['hint'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['caret'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['prompt'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['command'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}

c.bindings.commands['insert'] = {
        # escape hatch
        '<ctrl-x>': 'leave-mode',
}
