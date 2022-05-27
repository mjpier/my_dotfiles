#define CMDLENGTH 60
#define DELIMITER "  "
#define CLICKABLE_BLOCKS 0

const Block blocks[] = {
    BLOCK("sb-torrent",     20,     14),
    BLOCK("sb-net",         1,      15),
    BLOCK("sb-xbps",        7200,   16),
    BLOCK("sb-audio",       0,      17),
    BLOCK("sb-mail",        0,      18),
    BLOCK("sb-news",        0,      19),
    BLOCK("sb-forecast",    0,      20),
    BLOCK("sb-mem",         10,     21),
    //BLOCK("sb-gpu",         10,     22),
    BLOCK("sb-cpu",         10,     23),
    //BLOCK("sb-time",        1,      24),
    BLOCK("sb-battery",     5,      27),
    BLOCK("sb-date",        1,      25),
    BLOCK("sb-uptime",      1,      26),
};

