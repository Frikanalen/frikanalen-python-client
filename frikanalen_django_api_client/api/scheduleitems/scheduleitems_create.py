from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scheduleitem_modify import ScheduleitemModify
from ...types import Response


def _get_kwargs(
    *,
    body: ScheduleitemModify,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/scheduleitems/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScheduleitemModify]:
    if response.status_code == 201:
        response_201 = ScheduleitemModify.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScheduleitemModify]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ScheduleitemModify,
) -> Response[ScheduleitemModify]:
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
        body (ScheduleitemModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleitemModify]
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
    body: ScheduleitemModify,
) -> Optional[ScheduleitemModify]:
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
        body (ScheduleitemModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleitemModify
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ScheduleitemModify,
) -> Response[ScheduleitemModify]:
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
        body (ScheduleitemModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleitemModify]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ScheduleitemModify,
) -> Optional[ScheduleitemModify]:
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
        body (ScheduleitemModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleitemModify
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
