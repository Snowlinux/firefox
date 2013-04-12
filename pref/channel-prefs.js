//@line 2 "/~/src/mozilla-release/browser/app/profile/channel-prefs.js"
pref("app.update.channel", "default");

// Use LANG environment variable to choose locale
pref("intl.locale.matchOS", true);

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Prevent EULA dialog to popup on first run
pref("browser.EULA.override", true);

// Default search engine
pref("browser.search.searchEnginesURL", "https://duckduckgo.com/?t=snowlinux&q=");

// Activate the backspace key for browsing back
pref("browser.backspace_action", 0);

// Disable ipv6
pref("network.dns.disableIPv6", true);

// Ignore Mozilla release notes startup pages
pref("browser.startup.homepage_override.mstone", "ignore");

// Homepage
pref("browser.startup.homepage", "https://duckduckgo.com/?t=snowlinux");

// Save tabs before exiting
user_pref("browser.showQuitWarning", true);

