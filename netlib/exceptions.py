"""
We try to be very hygienic regarding the exceptions we throw:
Every Exception netlib raises shall be a subclass of NetlibException.


See also: http://lucumr.pocoo.org/2014/10/16/on-error-handling/
"""


class NetlibException(Exception):
    """
    Base class for all exceptions thrown by netlib.
    """
    def __init__(self, message=None):
        super().__init__(message)


class Disconnect:
    """Immediate EOF"""


class HttpException(NetlibException):
    pass


class HttpReadDisconnect(HttpException, Disconnect):
    pass


class HttpSyntaxException(HttpException):
    pass


class TcpException(NetlibException):
    pass


class TcpDisconnect(TcpException, Disconnect):
    pass


class TcpReadIncomplete(TcpException):
    pass


class TcpTimeout(TcpException):
    pass


class TlsException(NetlibException):
    pass


class InvalidCertificateException(TlsException):
    pass


class Timeout(TcpException):
    pass
