#!/usr/bin/python

import os, sys, commands

archi = sys.argv[1]
curdir = sys.argv[2]
version = sys.argv[3]
abort = False 

release = version
if "+" in version:
    if "snowlinux" not in version:
        abort = True
    release = version.split("+")[0]   
    
if "~" in version:
    release = version.split("~")[0]

if archi == "amd64":
    archi="linux-x86_64"
else:
    archi="linux-i686"

locales = {}
locales['en-US'] = 'en-us'
locales['af'] = 'af'
locales['ar'] = 'ar'
locales['be'] = 'be'
locales['bg'] = 'bg'
locales['bn-BD'] = 'bn-bd'
locales['ca'] = 'ca'
locales['cs'] = 'cs'
locales['da'] = 'da'
locales['de'] = 'de'
locales['el'] = 'el'
locales['en-GB'] = 'en-gb'
locales['eo'] = 'eo'
locales['es-ES'] = 'es'
locales['et'] = 'et'
locales['eu'] = 'eu'
locales['fa'] = 'fa'
locales['fi'] = 'fi'
locales['fr'] = 'fr'
locales['fy-NL'] = 'fy'
locales['gl'] = 'gl'
locales['gu-IN'] = 'gu'
locales['he'] = 'he'
locales['hi-IN'] = 'hi'
locales['hr'] = 'hr'
locales['hu'] = 'hu'
locales['id'] = 'id'
locales['is'] = 'is'
locales['it'] = 'it'
locales['ja'] = 'ja'
locales['kn'] = 'kn'
locales['ko'] = 'ko'
locales['lt'] = 'lt'
locales['lv'] = 'lv'
locales['nb-NO'] = 'nb'
locales['nl'] = 'nl'
locales['nn-NO'] = 'nn'
locales['pl'] = 'pl'
locales['pt-PT'] = 'pt'
locales['pt-BR'] = 'pt-br'
locales['ro'] = 'ro'
locales['ru'] = 'ru'
locales['sk'] = 'sk'
locales['sl'] = 'sl'
locales['sq'] = 'sq'
locales['sr'] = 'sr'
locales['sv-SE'] = 'sv'
locales['th'] = 'th'
locales['tr'] = 'tr'
locales['uk'] = 'uk'
locales['zh-CN'] = 'zh'

for locale in locales:
    if (locale == "en-US"):
        os.system("mkdir -p %s/debian/firefox-l10n-%s/opt/firefox/browser" % (curdir, locales[locale])) 
        os.system("mkdir -p %s/debian/firefox/opt" % curdir)
        os.system("mkdir -p %s/debian/firefox-l10n-%s/opt/firefox" % (curdir, locales[locale]))
        os.chdir("%s/debian/firefox/opt" % curdir)
    else:
        os.system("mkdir -p %s/debian/firefox-l10n-%s/opt" % (curdir, locales[locale]))
        os.chdir("%s/debian/firefox-l10n-%s/opt" % (curdir,locales[locale]))

    if not abort:        
        os.system("wget http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/%s/%s/firefox-%s.tar.bz2" % (archi, locale, release))
        if (not os.path.exists("firefox-%s.tar.bz2" % release)):
            print "FAILED: Could not download http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/%s/%s/firefox-%s.tar.bz2" % (archi, locale, release)
            sys.exit(1)

        os.system("bzip2 -d firefox-%s.tar.bz2" % release)
        os.system("tar xvf firefox-%s.tar" % release)
        os.system("rm firefox-%s.tar" % release)
                
        if (locale == "en-US"):
            os.system("mv firefox/omni.ja %s/debian/firefox-l10n-%s/opt/firefox/omni.ja" % (curdir, locales[locale]))    
            os.system("rm -rf firefox/searchplugins/*")
            os.system("rm -rf firefox/defaults/pref/*")
            os.system("cp %s/searchplugins/* firefox/searchplugins/" % curdir)
            os.system("cp %s/pref/* firefox/defaults/pref/" % curdir)
        else:        
            os.system("mv firefox/omni.ja ./")
            os.system("rm -rf firefox/*")
            os.system("mv omni.ja firefox/")

os.chdir(curdir)
