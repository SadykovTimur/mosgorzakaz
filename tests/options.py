def pytest_addoption(parser):
    group = parser.getgroup('Mosgorzakaz')

    group.addoption(
        '--browser', dest='browser', metavar='browser', default='chrome', help='Browser. Default option is chrome'
    )

    group.addoption(
        '--ui_url',
        help='A way to override the ui_url for your tests.',
        metavar='ui_url',
        default='10.19.89.65/mosks',
    )

    parser.addoption(
        '--remote_ip',
        help='A way to set remote url of selenoid',
        dest='remote_ip',
        metavar='remote_ip',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid1.c-view.mos.ru',
    )

    parser.addoption(
        '--remote_port',
        help='A way to set remote port of selenoid',
        dest='remote_port',
        metavar='remote_port',
        # default='4444',
        default='80',
    )

    parser.addoption(
        '--remote_ui',
        help='A way to set remote url of selenoid ui',
        dest='remote_ui',
        metavar='remote_ui',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid1.c-view.mos.ru',
    )

    parser.addoption(
        '--wait',
        help='(int) Value waiting of condition in seconds',
        dest='wait',
        metavar='wait',
        type=int,
        default=30,
    )

    parser.addoption(
        '--enable-video',
        action='store',
        dest='enable_video',
        type=bool,
        default=False,
        help='Enable recording video option',
    )

    parser.addoption('--user', action='store', dest='username', type=str, default='DITTestUserPM', help='Username')
    parser.addoption('--password', action='store', dest='password', type=str, default='Y8w1N07p1Ss', help='Password')
