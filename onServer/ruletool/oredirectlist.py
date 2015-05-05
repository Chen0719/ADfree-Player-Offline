[
    {
        "name": "youkuloader",
        "find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/loaders?[^\.]*\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/loader.swf",
        "extra": "adkillrule"
    },
    {
        "name": "youkuplayer",
        "find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/(q?player[^\.]*|\w{13})\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/player.swf",
        "extra": "adkillrule"
    },
    {
        "name": "ku6",
        "find": "http:\/\/player\.ku6cdn\.com\/default\/.*\/(v|player)[^\.]*\.swf",
        "replace": "hostsite/ku6.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou",
        "find": "http:\/\/js\.tudouui\.com\/.*PortalPlayer[^\.]*\.swf",
        "exfind": "narutom",
        "replace": "hostsite/tudou.swf",
        "css": ".player {height: inherit !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_olc",
        "find": "http:\/\/js\.tudouui\.com\/.*olc[^\.]*\.swf",
        "replace": "hostsite/olc_8.swf",
        "extra": "adkillrule"
    },
    {
        "name": "tudou_sp",
        "find": "http:\/\/js\.tudouui\.com\/.*SocialPlayer[^\.]*\.swf",
        "replace": "hostsite/sp.swf",
        "extra": "adkillrule"
    },
    {
        "name": "letv",
        "find": "http:\/\/.*letv[\w]*\.com\/.*\/((?!(Live|seed|Disk|SSDK))(S[\w]{2,3})?(?!Live)[\w]{4}|swf|VLetv)Player[^\.]*\.swf",
        "exfind": "(bili|acfun|(comic|hz)\.letv|duowan)",
        "replace": "hostsite/letv.swf",
        "extra": "adkillrule"
    },
    {
        "name": "letvpccs",
        "find": "http:\/\/www.letv.com\/.*\/playerapi\/pccs_(?!(live|sdk)).*_?(\d+)\.xml",
        "replace": "http://www.letv.com/cmsdata/playerapi/pccs_sdk_20141113.xml",
        "extra": "adkillrule"
    },
    {
        "name": "pplive",
        "find": "http:\/\/player\.pplive\.cn\/ikan\/.*\/player4player2\.swf",
        "replace": "hostsite/player4player2.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pplive_live",
        "find": "http:\/\/player\.pplive\.cn\/live\/.*\/player4live2\.swf",
        "replace": "hostsite/pptv.in.Live.swf",
        "extra": "adkillrule"
    },
    {
        "name": "iqiyi",
        "find": "https?:\/\/www\.iqiyi\.com\/(player\/(\d+\/Player|[a-z0-9]*)|common\/flashplayer\/\d+\/((PPS)?Main|Share)?Player.*_(.|\w{1,3}\d+))\.swf",
        "exfind": "(baidu|61|178)\.iqiyi\.com|weibo|yaku\.tv|bilibili|acfun|(music|tieba)\.baidu",
        "replace": "hostsite/iqiyi5.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pps",
        "find": "https?:\/\/www\.iqiyi\.com\/player\/cupid\/.*\/pps[\w]+.swf",
        "replace": "hostsite/pps.swf",
        "extra": "adkillrule"
    },
    {
        "name": "pps_live",
        "find": "https?:\/\/www\.iqiyi\.com\/common\/.*\/am[^\.]*.swf",
        "replace": "about:blank",
        "extra": "adkillrule"
    },
    {
        "name": "sohu_live",
        "find": "http:\/\/(tv\.sohu\.com\/upload\/swf\/(?!ap).*\d+|(\d+\.){3}\d+(:\d+)?\/.*player)\/(Main|PlayerShell)[^\.]*\.swf",
        "exfind": "(bili|acfun)",
        "replace": "hostsite/sohu_live.swf",
        "extra": "adkillrule"
    },
    {
        "name": "17173_in_Vod",
        "find": "http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFile(Customer)?\.swf",
        "replace": "hostsite/17173.in.Vod.swf",
        "extra": "adkillrule"
    },
    {
        "name": "17173_out_Vod",
        "find": "http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFileFirstpage\.swf",
        "replace": "hostsite/17173.out.Vod.swf",
        "extra": "adkillrule"
    },
    {
        "name": "17173_in_Live",
        "find": "http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream(_firstpage)?\.swf",
        "replace": "hostsite/17173_stream.swf",
        "css": "#livePlayerMin {height: 549px !important;}",
        "extra": "adkillrule"
    },
    {
        "name": "17173_out_Live",
        "find": "http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream_(custom)?Out\.swf",
        "replace": "hostsite/17173.out.Live.swf",
        "extra": "adkillrule"
    },
    {
        "name": "baidu_call",
        "find": "http\:\/\/list\.video\.baidu\.com\/swf\/advPlayer\.swf",
        "replace": "hostsite/baidu.call.swf",
        "extra": "adkillrule"
    }
]
