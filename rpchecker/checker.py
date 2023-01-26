"""Provide checker funtion for the application.

`site_is_online(url:str, timeout: float)` : True if the target URL is online

"""
import asyncio
from http.client import HTTPConnection
from urllib.parse import urlparse
import aiohttp

async def site_is_online_async(url:str, timeout: float) -> bool:
    """ Check the specific site connectivity asynchronously

       Examples:
           >>> site_is_online_async("https://bongdaplus.vn/", 5)
           True
           >>> site_is_online_async("https://www.python.org/", 4)
           True
           >>> site_is_online_async("https://hahadongu.com", 3)
           RuntimeWarning: Enable tracemalloc to get the object allocation traceback

       Args:
           url: A website address
           timeout: waiting time

       Returns:
           True if the target URL is online

       Raises:
           socket.gaierror: [Errno 11001] getaddrinfo failed
       """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error


def site_is_online(url:str, timeout: float) -> bool:
    """ Check the specific site connectivity

    Examples:
        >>> site_is_online("https://bongdaplus.vn/", 5)
        True
        >>> site_is_online("https://www.python.org/", 4)
        True
        >>> site_is_online("https://hahadongu.com", 3)
        Traceback (most recent call last):
        ...
        socket.gaierror: [Errno 11001] getaddrinfo failed

    Args:
        url: A website address
        timeout: waiting time

    Returns:
        True if the target URL is online

    Raises:
        socket.gaierror: [Errno 11001] getaddrinfo failed
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80,443):
        connection = HTTPConnection(host=host, port=port,timeout=timeout)
        try:
            connection.request("HEAD","/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error