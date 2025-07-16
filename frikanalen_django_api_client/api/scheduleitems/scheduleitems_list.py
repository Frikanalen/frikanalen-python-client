from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_scheduleitem_read_list import PaginatedScheduleitemReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/scheduleitems/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedScheduleitemReadList]:
    if response.status_code == 200:
        response_200 = PaginatedScheduleitemReadList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedScheduleitemReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Response[PaginatedScheduleitemReadList]:
    r"""Video events schedule

    Query parameters
    ----------------

    `date` - Date expressed in the format YYYY-MM-DD (eg. 2020-12-31), or
             \"today\".  Default is today, Europe/Oslo time.

    `days` - Number of days schedule requested. Default is 7 days.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `surrounding` - Fetch the first event before and after the given
                    period

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedScheduleitemReadList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Optional[PaginatedScheduleitemReadList]:
    r"""Video events schedule

    Query parameters
    ----------------

    `date` - Date expressed in the format YYYY-MM-DD (eg. 2020-12-31), or
             \"today\".  Default is today, Europe/Oslo time.

    `days` - Number of days schedule requested. Default is 7 days.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `surrounding` - Fetch the first event before and after the given
                    period

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedScheduleitemReadList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Response[PaginatedScheduleitemReadList]:
    r"""Video events schedule

    Query parameters
    ----------------

    `date` - Date expressed in the format YYYY-MM-DD (eg. 2020-12-31), or
             \"today\".  Default is today, Europe/Oslo time.

    `days` - Number of days schedule requested. Default is 7 days.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `surrounding` - Fetch the first event before and after the given
                    period

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedScheduleitemReadList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Optional[PaginatedScheduleitemReadList]:
    r"""Video events schedule

    Query parameters
    ----------------

    `date` - Date expressed in the format YYYY-MM-DD (eg. 2020-12-31), or
             \"today\".  Default is today, Europe/Oslo time.

    `days` - Number of days schedule requested. Default is 7 days.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `surrounding` - Fetch the first event before and after the given
                    period

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-starttime`.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedScheduleitemReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
