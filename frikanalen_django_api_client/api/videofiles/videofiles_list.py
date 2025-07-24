import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_video_file_list import PaginatedVideoFileList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    format_fsname: Union[Unset, str] = UNSET,
    integrated_lufs: Union[Unset, float] = UNSET,
    integrated_lufs_gt: Union[Unset, float] = UNSET,
    integrated_lufs_gte: Union[Unset, float] = UNSET,
    integrated_lufs_isnull: Union[Unset, bool] = UNSET,
    integrated_lufs_lt: Union[Unset, float] = UNSET,
    integrated_lufs_lte: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    truepeak_lufs: Union[Unset, float] = UNSET,
    truepeak_lufs_gt: Union[Unset, float] = UNSET,
    truepeak_lufs_gte: Union[Unset, float] = UNSET,
    truepeak_lufs_isnull: Union[Unset, bool] = UNSET,
    truepeak_lufs_lt: Union[Unset, float] = UNSET,
    truepeak_lufs_lte: Union[Unset, float] = UNSET,
    video_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created_time_after: Union[Unset, str] = UNSET
    if not isinstance(created_time_after, Unset):
        json_created_time_after = created_time_after.isoformat()
    params["created_time_after"] = json_created_time_after

    json_created_time_before: Union[Unset, str] = UNSET
    if not isinstance(created_time_before, Unset):
        json_created_time_before = created_time_before.isoformat()
    params["created_time_before"] = json_created_time_before

    params["format__fsname"] = format_fsname

    params["integrated_lufs"] = integrated_lufs

    params["integrated_lufs__gt"] = integrated_lufs_gt

    params["integrated_lufs__gte"] = integrated_lufs_gte

    params["integrated_lufs__isnull"] = integrated_lufs_isnull

    params["integrated_lufs__lt"] = integrated_lufs_lt

    params["integrated_lufs__lte"] = integrated_lufs_lte

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["truepeak_lufs"] = truepeak_lufs

    params["truepeak_lufs__gt"] = truepeak_lufs_gt

    params["truepeak_lufs__gte"] = truepeak_lufs_gte

    params["truepeak_lufs__isnull"] = truepeak_lufs_isnull

    params["truepeak_lufs__lt"] = truepeak_lufs_lt

    params["truepeak_lufs__lte"] = truepeak_lufs_lte

    params["video_id"] = video_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/videofiles/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVideoFileList]:
    if response.status_code == 200:
        response_200 = PaginatedVideoFileList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVideoFileList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    format_fsname: Union[Unset, str] = UNSET,
    integrated_lufs: Union[Unset, float] = UNSET,
    integrated_lufs_gt: Union[Unset, float] = UNSET,
    integrated_lufs_gte: Union[Unset, float] = UNSET,
    integrated_lufs_isnull: Union[Unset, bool] = UNSET,
    integrated_lufs_lt: Union[Unset, float] = UNSET,
    integrated_lufs_lte: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    truepeak_lufs: Union[Unset, float] = UNSET,
    truepeak_lufs_gt: Union[Unset, float] = UNSET,
    truepeak_lufs_gte: Union[Unset, float] = UNSET,
    truepeak_lufs_isnull: Union[Unset, bool] = UNSET,
    truepeak_lufs_lt: Union[Unset, float] = UNSET,
    truepeak_lufs_lte: Union[Unset, float] = UNSET,
    video_id: Union[Unset, int] = UNSET,
) -> Response[PaginatedVideoFileList]:
    """Video file list

    Args:
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        format_fsname (Union[Unset, str]):
        integrated_lufs (Union[Unset, float]):
        integrated_lufs_gt (Union[Unset, float]):
        integrated_lufs_gte (Union[Unset, float]):
        integrated_lufs_isnull (Union[Unset, bool]):
        integrated_lufs_lt (Union[Unset, float]):
        integrated_lufs_lte (Union[Unset, float]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        truepeak_lufs (Union[Unset, float]):
        truepeak_lufs_gt (Union[Unset, float]):
        truepeak_lufs_gte (Union[Unset, float]):
        truepeak_lufs_isnull (Union[Unset, bool]):
        truepeak_lufs_lt (Union[Unset, float]):
        truepeak_lufs_lte (Union[Unset, float]):
        video_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVideoFileList]
    """

    kwargs = _get_kwargs(
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        format_fsname=format_fsname,
        integrated_lufs=integrated_lufs,
        integrated_lufs_gt=integrated_lufs_gt,
        integrated_lufs_gte=integrated_lufs_gte,
        integrated_lufs_isnull=integrated_lufs_isnull,
        integrated_lufs_lt=integrated_lufs_lt,
        integrated_lufs_lte=integrated_lufs_lte,
        limit=limit,
        offset=offset,
        ordering=ordering,
        truepeak_lufs=truepeak_lufs,
        truepeak_lufs_gt=truepeak_lufs_gt,
        truepeak_lufs_gte=truepeak_lufs_gte,
        truepeak_lufs_isnull=truepeak_lufs_isnull,
        truepeak_lufs_lt=truepeak_lufs_lt,
        truepeak_lufs_lte=truepeak_lufs_lte,
        video_id=video_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    format_fsname: Union[Unset, str] = UNSET,
    integrated_lufs: Union[Unset, float] = UNSET,
    integrated_lufs_gt: Union[Unset, float] = UNSET,
    integrated_lufs_gte: Union[Unset, float] = UNSET,
    integrated_lufs_isnull: Union[Unset, bool] = UNSET,
    integrated_lufs_lt: Union[Unset, float] = UNSET,
    integrated_lufs_lte: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    truepeak_lufs: Union[Unset, float] = UNSET,
    truepeak_lufs_gt: Union[Unset, float] = UNSET,
    truepeak_lufs_gte: Union[Unset, float] = UNSET,
    truepeak_lufs_isnull: Union[Unset, bool] = UNSET,
    truepeak_lufs_lt: Union[Unset, float] = UNSET,
    truepeak_lufs_lte: Union[Unset, float] = UNSET,
    video_id: Union[Unset, int] = UNSET,
) -> Optional[PaginatedVideoFileList]:
    """Video file list

    Args:
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        format_fsname (Union[Unset, str]):
        integrated_lufs (Union[Unset, float]):
        integrated_lufs_gt (Union[Unset, float]):
        integrated_lufs_gte (Union[Unset, float]):
        integrated_lufs_isnull (Union[Unset, bool]):
        integrated_lufs_lt (Union[Unset, float]):
        integrated_lufs_lte (Union[Unset, float]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        truepeak_lufs (Union[Unset, float]):
        truepeak_lufs_gt (Union[Unset, float]):
        truepeak_lufs_gte (Union[Unset, float]):
        truepeak_lufs_isnull (Union[Unset, bool]):
        truepeak_lufs_lt (Union[Unset, float]):
        truepeak_lufs_lte (Union[Unset, float]):
        video_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVideoFileList
    """

    return sync_detailed(
        client=client,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        format_fsname=format_fsname,
        integrated_lufs=integrated_lufs,
        integrated_lufs_gt=integrated_lufs_gt,
        integrated_lufs_gte=integrated_lufs_gte,
        integrated_lufs_isnull=integrated_lufs_isnull,
        integrated_lufs_lt=integrated_lufs_lt,
        integrated_lufs_lte=integrated_lufs_lte,
        limit=limit,
        offset=offset,
        ordering=ordering,
        truepeak_lufs=truepeak_lufs,
        truepeak_lufs_gt=truepeak_lufs_gt,
        truepeak_lufs_gte=truepeak_lufs_gte,
        truepeak_lufs_isnull=truepeak_lufs_isnull,
        truepeak_lufs_lt=truepeak_lufs_lt,
        truepeak_lufs_lte=truepeak_lufs_lte,
        video_id=video_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    format_fsname: Union[Unset, str] = UNSET,
    integrated_lufs: Union[Unset, float] = UNSET,
    integrated_lufs_gt: Union[Unset, float] = UNSET,
    integrated_lufs_gte: Union[Unset, float] = UNSET,
    integrated_lufs_isnull: Union[Unset, bool] = UNSET,
    integrated_lufs_lt: Union[Unset, float] = UNSET,
    integrated_lufs_lte: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    truepeak_lufs: Union[Unset, float] = UNSET,
    truepeak_lufs_gt: Union[Unset, float] = UNSET,
    truepeak_lufs_gte: Union[Unset, float] = UNSET,
    truepeak_lufs_isnull: Union[Unset, bool] = UNSET,
    truepeak_lufs_lt: Union[Unset, float] = UNSET,
    truepeak_lufs_lte: Union[Unset, float] = UNSET,
    video_id: Union[Unset, int] = UNSET,
) -> Response[PaginatedVideoFileList]:
    """Video file list

    Args:
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        format_fsname (Union[Unset, str]):
        integrated_lufs (Union[Unset, float]):
        integrated_lufs_gt (Union[Unset, float]):
        integrated_lufs_gte (Union[Unset, float]):
        integrated_lufs_isnull (Union[Unset, bool]):
        integrated_lufs_lt (Union[Unset, float]):
        integrated_lufs_lte (Union[Unset, float]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        truepeak_lufs (Union[Unset, float]):
        truepeak_lufs_gt (Union[Unset, float]):
        truepeak_lufs_gte (Union[Unset, float]):
        truepeak_lufs_isnull (Union[Unset, bool]):
        truepeak_lufs_lt (Union[Unset, float]):
        truepeak_lufs_lte (Union[Unset, float]):
        video_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVideoFileList]
    """

    kwargs = _get_kwargs(
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        format_fsname=format_fsname,
        integrated_lufs=integrated_lufs,
        integrated_lufs_gt=integrated_lufs_gt,
        integrated_lufs_gte=integrated_lufs_gte,
        integrated_lufs_isnull=integrated_lufs_isnull,
        integrated_lufs_lt=integrated_lufs_lt,
        integrated_lufs_lte=integrated_lufs_lte,
        limit=limit,
        offset=offset,
        ordering=ordering,
        truepeak_lufs=truepeak_lufs,
        truepeak_lufs_gt=truepeak_lufs_gt,
        truepeak_lufs_gte=truepeak_lufs_gte,
        truepeak_lufs_isnull=truepeak_lufs_isnull,
        truepeak_lufs_lt=truepeak_lufs_lt,
        truepeak_lufs_lte=truepeak_lufs_lte,
        video_id=video_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    format_fsname: Union[Unset, str] = UNSET,
    integrated_lufs: Union[Unset, float] = UNSET,
    integrated_lufs_gt: Union[Unset, float] = UNSET,
    integrated_lufs_gte: Union[Unset, float] = UNSET,
    integrated_lufs_isnull: Union[Unset, bool] = UNSET,
    integrated_lufs_lt: Union[Unset, float] = UNSET,
    integrated_lufs_lte: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    truepeak_lufs: Union[Unset, float] = UNSET,
    truepeak_lufs_gt: Union[Unset, float] = UNSET,
    truepeak_lufs_gte: Union[Unset, float] = UNSET,
    truepeak_lufs_isnull: Union[Unset, bool] = UNSET,
    truepeak_lufs_lt: Union[Unset, float] = UNSET,
    truepeak_lufs_lte: Union[Unset, float] = UNSET,
    video_id: Union[Unset, int] = UNSET,
) -> Optional[PaginatedVideoFileList]:
    """Video file list

    Args:
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        format_fsname (Union[Unset, str]):
        integrated_lufs (Union[Unset, float]):
        integrated_lufs_gt (Union[Unset, float]):
        integrated_lufs_gte (Union[Unset, float]):
        integrated_lufs_isnull (Union[Unset, bool]):
        integrated_lufs_lt (Union[Unset, float]):
        integrated_lufs_lte (Union[Unset, float]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        truepeak_lufs (Union[Unset, float]):
        truepeak_lufs_gt (Union[Unset, float]):
        truepeak_lufs_gte (Union[Unset, float]):
        truepeak_lufs_isnull (Union[Unset, bool]):
        truepeak_lufs_lt (Union[Unset, float]):
        truepeak_lufs_lte (Union[Unset, float]):
        video_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVideoFileList
    """

    return (
        await asyncio_detailed(
            client=client,
            created_time_after=created_time_after,
            created_time_before=created_time_before,
            format_fsname=format_fsname,
            integrated_lufs=integrated_lufs,
            integrated_lufs_gt=integrated_lufs_gt,
            integrated_lufs_gte=integrated_lufs_gte,
            integrated_lufs_isnull=integrated_lufs_isnull,
            integrated_lufs_lt=integrated_lufs_lt,
            integrated_lufs_lte=integrated_lufs_lte,
            limit=limit,
            offset=offset,
            ordering=ordering,
            truepeak_lufs=truepeak_lufs,
            truepeak_lufs_gt=truepeak_lufs_gt,
            truepeak_lufs_gte=truepeak_lufs_gte,
            truepeak_lufs_isnull=truepeak_lufs_isnull,
            truepeak_lufs_lt=truepeak_lufs_lt,
            truepeak_lufs_lte=truepeak_lufs_lte,
            video_id=video_id,
        )
    ).parsed
