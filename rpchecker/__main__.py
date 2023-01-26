"""Provide functions to run your site connectivity application

The module contains the following functions to run the main:
- `_get_websites_urls(user_args:any) -> List[str]`: Return a list of websites urls
_ `read_urls_from_file(file:str) -> List[str]`: Return a list of urls from a file
_ `asynchronous_check(urls:List[str],time_out:float) -> None`: Display the results of asynchronous option
_ `synchronous_check(urls:List,timeout:float) -> None`: Display the results of asynchronous option

"""


import sys
from typing import List
import logging
from logging import config
import doctest
import pathlib
import json
from rpchecker.checker import site_is_online,site_is_online_async
from rpchecker.cli import display_check_result, read_user_cli_args
import asyncio

# TODO: Create logger
with open('log_config.json') as json_file:
    log_config = json.load(json_file)
config.dictConfig(log_config)
logger = logging.getLogger('project')


# TODO: Create main
def main():
    """ Run RP Checker"""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        logger.error("No URLs to check!")
        sys.exit(1)
    time_out = float(input("Enter time out: "))
    if user_args.asynchronous:
        asyncio.run(_asynchronous_check(urls,time_out))
    else:
        _synchronous_check(urls,timeout)


# TODO: Get urls
def _get_websites_urls(user_args:any) -> List[str]:
    """ Get url of each websites
    Examples:
        Can not give you example due to my stupid head

    Args:
        user_args: the arguments provided by user in command line

    Returns:
        A list of websites urls
    """
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file:str) -> List[str]:
    """ Get URLs from a file

    Examples:
        Can not give you example due to my stupid head
    Args:
        file: a file name

    Returns:
        A list of urls from a file

    """
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            logger.error("Empty input file!")
    else:
        logger.error("Input file not found")
    return []


# TODO: Check asynchronously
async def _asynchronous_check(urls:List[str],time_out:float) -> None :
    """
    Examples:
        Can not give you example due to my lazyness
    Args:
        urls: a list
        timeout: waiting time
    """
    async def _check(url:str,time_out:float):
        error = ""
        try:
            result = await site_is_online_async(url,time_out)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

    await asyncio.gather(*(_check(url,time_out) for url in urls))

# TODO: Check synchronously
def _synchronous_check(urls:List[str],timeout:float) -> None:
    """
    Examples:
        Can not give you example due to my lazyness
    Args:
        urls: a list
        timeout: waiting time
    """
    for url in urls:
        error = ""
        try:
            result = site_is_online(url,timeout)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)


if __name__ == "__main__":
    #doctest.testmod()
    main()