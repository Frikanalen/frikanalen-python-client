from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video_file import VideoFile
from ...types import Response


def _get_kwargs(
    *,
    body: VideoFile,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/videofiles/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VideoFile]:
    if response.status_code == 201:
        response_201 = VideoFile.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VideoFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VideoFile,
) -> Response[VideoFile]:
    """Video file list

    Query parameters
    ----------------

    HTTP parameters:

    `video_id` - The (parent) video by ID

    `created_time` - when this file entry was created.

    `format__fsname` - the fileformat fsname for this file.

    `integrated_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `truepeak_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        body (VideoFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoFile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: VideoFile,
) -> Optional[VideoFile]:
    """Video file list

    Query parameters
    ----------------

    HTTP parameters:

    `video_id` - The (parent) video by ID

    `created_time` - when this file entry was created.

    `format__fsname` - the fileformat fsname for this file.

    `integrated_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `truepeak_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        body (VideoFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoFile
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VideoFile,
) -> Response[VideoFile]:
    """Video file list

    Query parameters
    ----------------

    HTTP parameters:

    `video_id` - The (parent) video by ID

    `created_time` - when this file entry was created.

    `format__fsname` - the fileformat fsname for this file.

    `integrated_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `truepeak_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        body (VideoFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoFile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: VideoFile,
) -> Optional[VideoFile]:
    """Video file list

    Query parameters
    ----------------

    HTTP parameters:

    `video_id` - The (parent) video by ID

    `created_time` - when this file entry was created.

    `format__fsname` - the fileformat fsname for this file.

    `integrated_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `truepeak_lufs` (includes __gt, __gte, __lt, __lte, __isnull) the overall loudness of the file.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        body (VideoFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoFile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
