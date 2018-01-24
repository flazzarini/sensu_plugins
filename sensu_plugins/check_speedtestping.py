from sensu_plugin import SensuPluginCheck
from pyspeedtest import SpeedTest


class SpeedTestPingCheck(SensuPluginCheck):
    def setup(self):
        self.parser.add_argument(
            '-w', dest="warning", type=int, default=30,
            help="Warn when ping is above this setting (ms) (Default: 50)"
        )
        self.parser.add_argument(
            '-c', dest="critical", type=int, default=90,
            help="Critical when ping is above this setting (ms) (Default: 100)"
        )

    def _do_ping(self):
        speedtest = SpeedTest()
        return speedtest.ping()

    def run(self):
        try:
            result = self._do_ping()
        except Exception as exc:
            msg = "Ping to speedtest.net failed - %s" % exc
            self.critical(msg)

        msg = "Ping to speedtest.net took `%s ms`" % result
        if result > self.options.critical:
            self.critical(msg)
        elif result > self.options.warning:
            self.warning(msg)
        else:
            self.ok(msg)


def main():
    SpeedTestPingCheck()
